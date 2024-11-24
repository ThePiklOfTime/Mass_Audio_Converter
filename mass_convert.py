#!/usr/bin/env python3
import subprocess
import os
import json
from argparse import ArgumentParser
import sys

parser = ArgumentParser(
    description='Converts all files in current directory and subdirectories with the specified codec (default: alac) into the specified codec (default: flac).'
)
parser.add_argument('-i', '--input', help="Input codec (wav, alac, flac). Default: alac.", default="alac")
parser.add_argument('-o', '--output', help="Output codec (wav, alac, flac). Default: flac.", default="flac")
parser.add_argument('-d', '--delete', help="Delete original files after conversion.", action='store_true', default=False)
validInput = ['alac', 'flac', 'wav']
args = parser.parse_args()

if not args.input in validInput or not args.output in validInput:
    sys.exit("Error: Supported formats are alac, flac, and wav.")

if args.input == args.output:
    sys.exit("Error: Input and output codecs cannot be the same.")

input_extensions = {'wav': '.wav', 'alac': '.m4a', 'flac': '.flac'}
codec_names = {'wav': 'pcm_s16le', 'alac': 'alac', 'flac': 'flac'}

file_extension = input_extensions[args.input]
codec_name = codec_names[args.input]
file_extension_out = input_extensions[args.output]
codec_name_out = codec_names[args.output]

for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if filename.endswith(file_extension):
            filepath = os.path.join(dirpath, filename)
            fbrobe_command = ['ffprobe', '-show_streams', '-select_streams', 'a', '-v', 'quiet', '-print_format', 'json', filepath]
            try:
                file_info = subprocess.run(fbrobe_command, capture_output=True, check=True, text=True)
                file_info_dict = json.loads(file_info.stdout)
                if 'streams' not in file_info_dict or not file_info_dict['streams']:
                    print(f"No audio streams found in {filename}")
                    continue
                if file_info_dict['streams'][0]['codec_name'] == codec_name:
                    print(f"Encoding {filename} from {args.input} to {args.output}...")
                    filepath_without_codec = filepath.removesuffix(file_extension)
                    ffmpeg_command = ['ffmpeg', '-i', filepath, '-c:a', codec_name_out, f'{filepath_without_codec}{file_extension_out}']
                    subprocess.run(ffmpeg_command, check=True)
                    print(f"Successfully converted {filename}.")
                    if args.delete:
                        os.remove(filepath)
                        print(f"Deleted original file: {filename}")
            except subprocess.CalledProcessError as e:
                print(f"Error processing {filename}: {e}")
