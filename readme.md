# Recursive Lossless Audio File Converter

This is a simple script I created to batch-convert a large collection of music files from one lossless codec to another. It recursively scans directories, converts files to the desired codec, and optionally deletes the original files after conversion.

## Features
- Supports **wav**, **alac**, and **flac** formats for both input and output.
- Recursively processes files in the current directory and all subdirectories.
- Optional deletion of original files after conversion.
- Uses `ffmpeg` and `ffprobe` for high-quality audio processing.

## Requirements
- **Operating System**: Works on Linux and Unix-based systems (e.g., macOS).
- **Dependencies**:
  - `ffmpeg` and `ffprobe`: Must be accessible via `PATH`.
  - Python 3.x: A supported version of Python 3 must be installed and accessible via `PATH`.

## Installation
1. Ensure you have the required dependencies installed.
   - On Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install ffmpeg python3
     ```
   - On macOS with Homebrew:
     ```bash
     brew install ffmpeg python
     ```
2. Clone or download this repository to your system.
3. Make the script executable:
   ```bash
   chmod +x mass_convert.py
   ```

## Usage
1. Verify that Python 3 is available by running:
   ```bash
   python3 --version
   ```
   If `python3` is not found, try `python --version`. If only `python` works, edit the first line of the script to replace `python3` with `python`.

2. Run the script:
   ```bash
   ./mass_convert.py -i <input_codec> -o <output_codec> [-d]
   ```
   Replace `<input_codec>` and `<output_codec>` with one of `wav`, `alac`, or `flac`.

### Options
- `-i, --input`: Specifies the codec of the input files. Defaults to `alac`.
- `-o, --output`: Specifies the codec for the output files. Defaults to `flac`.
- `-d, --delete`: Deletes original files after successful conversion.

### Examples
- Convert all `.m4a` (ALAC) files to `.flac`:
  ```bash
  ./mass_convert.py -i alac -o flac
  ```
- Convert `.flac` files to `.wav` and delete the original files:
  ```bash
  ./mass_convert.py -i flac -o wav -d
  ```

## Notes
- The script skips files that are already in the desired codec.
- If you encounter any issues, ensure the required tools (`ffmpeg`, `ffprobe`) are installed and accessible.

## Limitations
- Currently supports only Linux/Unix-based systems. It might work on windows, but this requires further testing.
- Assumes all audio files use standard file extensions (`.wav`, `.m4a`, `.flac`).

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

Feel free to fork and improve this script for your own needs!# Recursive Lossless Audio File Converter

This is a simple script I created to batch-convert a large collection of music files from one lossless codec to another. It recursively scans directories, converts files to the desired codec, and optionally deletes the original files after conversion.

## Features
- Supports **wav**, **alac**, and **flac** formats for both input and output.
- Recursively processes files in the current directory and all subdirectories.
- Optional deletion of original files after conversion.
- Uses `ffmpeg` and `ffprobe` for high-quality audio processing.

## Requirements
- **Operating System**: Works on Linux and Unix-based systems (e.g., macOS).
- **Dependencies**:
  - `ffmpeg` and `ffprobe`: Must be accessible via `PATH`.
  - Python **3.9 or later**: Required due to modern syntax features (`removesuffix` and more).

## Installation
1. Ensure you have the required dependencies installed.
   - On Ubuntu/Debian:
     ```bash
     sudo apt update
     sudo apt install ffmpeg python3
     ```
   - On macOS with Homebrew:
     ```bash
     brew install ffmpeg python
     ```
2. Clone or download this repository to your system.
3. Make the script executable:
   ```bash
   chmod +x mass_convert.py
   ```

## Usage
1. Verify that Python 3.9+ is available by running:
   ```bash
   python3 --version
   ```
   If your version is older than 3.9, please upgrade Python.

2. Run the script:
   ```bash
   ./mass_convert.py -i <input_codec> -o <output_codec> [-d]
   ```
   Replace `<input_codec>` and `<output_codec>` with one of `wav`, `alac`, or `flac`.

### Options
- `-i, --input`: Specifies the codec of the input files. Defaults to `alac`.
- `-o, --output`: Specifies the codec for the output files. Defaults to `flac`.
- `-d, --delete`: Deletes original files after successful conversion.

### Examples
- Convert all `.m4a` (ALAC) files to `.flac`:
  ```bash
  ./mass_convert.py -i alac -o flac
  ```
- Convert `.flac` files to `.wav` and delete the original files:
  ```bash
  ./mass_convert.py -i flac -o wav -d
  ```

## Notes
- The script skips files that are already in the desired codec.
- If you encounter any issues, ensure the required tools (`ffmpeg`, `ffprobe`) are installed and accessible.

## Limitations
- Currently supports only Linux/Unix-based systems.
- Assumes all audio files use standard file extensions (`.wav`, `.m4a`, `.flac`).

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

Feel free to fork and improve this script for your own needs!

