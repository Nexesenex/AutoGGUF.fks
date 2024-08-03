from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import os
import sys
import psutil
import subprocess
import time
import signal
import json
import platform
import requests
import zipfile
import traceback
from datetime import datetime
from imports_and_globals import open_file_safe

class QuantizationThread(QThread):
    output_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str)
    finished_signal = pyqtSignal()
    error_signal = pyqtSignal(str)
    model_info_signal = pyqtSignal(dict)

    def __init__(self, command, cwd, log_file):
        super().__init__()
        self.command = command
        self.cwd = cwd
        self.log_file = log_file
        self.process = None
        self.model_info = {}

    def run(self):
        try:
            self.process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                       text=True, cwd=self.cwd)
            with open_file_safe(self.log_file, 'w') as log:
                for line in self.process.stdout:
                    line = line.strip()
                    self.output_signal.emit(line)
                    log.write(line + '\n')
                    log.flush()
                    self.status_signal.emit("In Progress")
                    self.parse_model_info(line)
            self.process.wait()
            if self.process.returncode == 0:
                self.status_signal.emit("Completed")
                self.model_info_signal.emit(self.model_info)
            else:
                self.error_signal.emit(f"Process exited with code {self.process.returncode}")
            self.finished_signal.emit()
        except Exception as e:
            self.error_signal.emit(str(e))

    def parse_model_info(self, line):
        if "llama_model_loader: loaded meta data with" in line:
            parts = line.split()
            self.model_info['kv_pairs'] = parts[6]
            self.model_info['tensors'] = parts[9]
        elif "general.architecture" in line:
            self.model_info['architecture'] = line.split('=')[-1].strip()
        elif line.startswith("llama_model_loader: - kv"):
            key = line.split(':')[2].strip()
            value = line.split('=')[-1].strip()
            self.model_info.setdefault('kv_data', {})[key] = value
        elif line.startswith("llama_model_loader: - type"):
            parts = line.split(':')
            if len(parts) > 1:
                quant_type = parts[1].strip()
                tensors = parts[2].strip().split()[0]
                self.model_info.setdefault('quantization_type', []).append(f"{quant_type}: {tensors} tensors")

    def terminate(self):
        if self.process:
            os.kill(self.process.pid, signal.SIGTERM)
            self.process.wait(timeout=5)
            if self.process.poll() is None:
                os.kill(self.process.pid, signal.SIGKILL)

