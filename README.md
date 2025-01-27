![AutoGGUF-banner](https://github.com/user-attachments/assets/0f74b104-0541-46a7-9ac8-4a3fcb74b896)

# AutoGGUF - automated GGUF model quantizer

<!-- Project Status -->
[![GitHub release](https://img.shields.io/github/release/leafspark/AutoGGUF.svg)](https://github.com/leafspark/AutoGGUF/releases)
[![GitHub last commit](https://img.shields.io/github/last-commit/leafspark/AutoGGUF.svg)](https://github.com/leafspark/AutoGGUF/commits)
[![CI/CD Status](https://img.shields.io/badge/CI%2FCD-passing-brightgreen)]()

<!-- Project Info -->
[![Powered by llama.cpp](https://img.shields.io/badge/Powered%20by-llama.cpp-green.svg)](https://github.com/ggerganov/llama.cpp)
[![Platform Compatibility](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-blue)]()
[![GitHub license](https://img.shields.io/github/license/leafspark/AutoGGUF.svg)](https://github.com/leafspark/AutoGGUF/blob/main/LICENSE)
![GitHub top language](https://img.shields.io/github/languages/top/leafspark/AutoGGUF.svg)

<!-- Repository Stats -->
![GitHub stars](https://img.shields.io/github/stars/leafspark/AutoGGUF.svg)
![GitHub forks](https://img.shields.io/github/forks/leafspark/AutoGGUF.svg)
![GitHub release (latest by date)](https://img.shields.io/github/downloads/leafspark/AutoGGUF/latest/total?color=green)
![GitHub repo size](https://img.shields.io/github/repo-size/leafspark/AutoGGUF.svg)
![Lines of Code](https://tokei.rs/b1/github/leafspark/AutoGGUF?category=code)

<!-- Contribution -->
[![Issues](https://img.shields.io/github/issues/leafspark/AutoGGUF)](https://github.com/leafspark/AutoGGUF/issues)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/leafspark/AutoGGUF/pulls)

The most comprehensive GUI tool for GGUF model quantization. Stop wrestling with command lines - quantize, merge, and optimize your models with just a few clicks.

## Features

- 📩 Download and manage llama.cpp backends
- 🗃️ Select and quantize GGUF models
- 📐 Configure quantization parameters
- 💻 Monitor system resources during quantization
- ⏳ Parallel quantization + imatrix generation
- 🎉 LoRA conversion and merging
- 📁 Preset saving and loading
- 8️⃣ AutoFP8 quantization
- 🪓 GGUF splitting and merging
- 🌐 HTTP API for automated monitoring

## Why AutoGGUF?
- Fast: Saves time on manual configuration
- Simple: Clean UI, no terminal needed
- Powerful: Handles models up to infinite size, only limited by your RAM 
- Resource-aware: Optimized memory management and efficient UI library

![AutoGGUF-v1 8 1-showcase-blue](https://github.com/user-attachments/assets/b136ccc3-5983-4266-9e66-00cebf3ca590)

## Quick Start

### Cross-platform
1. `git clone https://github.com/leafspark/AutoGGUF`
2. `cd AutoGGUF`
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python src/main.py
   ```
   or use the `run.bat` script.

macOS and Ubuntu builds are provided with GitHub Actions, you may download the binaries in the releases section.

### Windows (for the impatient)
Standard builds:
1. Download the latest release
2. Extract all files to a folder
3. Run `AutoGGUF-x64.exe`
4. Any necessary folders will be automatically created

Setup builds:
1. Download setup variant of latest release
2. Extract all files to a folder
3. Run the setup program
4. The .GGUF extension will be registered with the program automatically
5. Run the program from the Start Menu or desktop shortcuts

After launching the program, you may access its local server at port 7001 (set `AUTOGGUF_SERVER` to "enabled" first)

### Verifying Releases

#### Linux/macOS:
```bash
gpg --import AutoGGUF-v1.5.0-prerel.asc
gpg --verify AutoGGUF-v1.9.1-Windows-avx2.zip.sig AutoGGUF-v1.9.1-Windows-avx2.zip
sha256sum -c AutoGGUF-v1.9.1.sha256
```

#### Windows (PowerShell):
```powershell
# Import the public key
gpg --import AutoGGUF-v1.5.0-prerel.asc

# Verify the signature
gpg --verify AutoGGUF-v1.9.1-Windows-avx2.zip.sig AutoGGUF-v1.9.1-Windows-avx2.zip

# Check SHA256
$fileHash = (Get-FileHash -Algorithm SHA256 AutoGGUF-v1.9.1-Windows-avx2.zip).Hash.ToLower()
$storedHash = (Get-Content AutoGGUF-v1.9.1.sha256 | Select-String AutoGGUF-v1.9.1-Windows-avx2.zip).Line.Split()[0]
if ($fileHash -eq $storedHash) { "SHA256 Match" } else { "SHA256 Mismatch" }
```

Release keys are identical to ones used for commiting.

## Building

### Cross-platform
```bash
pip install -U pyinstaller
./build.sh RELEASE | DEV
cd build/<type>/dist/
./AutoGGUF
```

### Windows
```bash
pip install -U pyinstaller
build RELEASE | DEV
```
Find the executable in `build/<type>/dist/AutoGGUF-x64.exe`.

You can also use Nuitka, which may result in a slower build but a faster output executable:
```bash
build_optimized RELEASE | DEV
```

## Localizations

View the list of supported languages at [AutoGGUF/wiki/Installation#configuration](https://github.com/leafspark/AutoGGUF/wiki/Installation#configuration) (LLM translated, except for English).

More languages will be updated as soon as possible!

To use a specific language, set the `AUTOGGUF_LANGUAGE` environment variable to one of the listed language codes (note: some languages may not be fully supported yet, those will fall back to English).

## Issues

- Some inconsistent logging
- Missing translations

## Planned Features

- Time estimation for quantization
- Quantization file size estimate
- Perplexity testing
- bitsandbytes

Due to my limited availability and a lack of time, I won't be actively developing new features for this project as much. While I'll continue to publish builds from time to time, I strongly recommend running from source if you want to stay up to date with the latest changes. I'm still committed to keeping dependencies updated weekly and making small maintenance fixes to ensure everything runs smoothly. If you run into any problems or notice issues, please don't hesitate to let me know - I appreciate your feedback and will do my best to address them.

## Support

- SSL module cannot be found error: Install OpenSSL or run from source using `python src/main.py` with the `run.bat` script (`pip install requests`)
- Check out the [Wiki](https://github.com/leafspark/AutoGGUF/wiki) for advanced usage and configuration

## Contributing

Fork the repo, make your changes, and ensure you have the latest commits when merging. Include a changelog of new features in your pull request description. Read `CONTRIBUTING.md` for more information.

## Stargazers

[![Star History Chart](https://api.star-history.com/svg?repos=leafspark/AutoGGUF&type=Date)](https://star-history.com/#leafspark/AutoGGUF&Date)
