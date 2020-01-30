#!/usr/bin/env python
import os    # os.path


FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print("file path:", file_path)

print(os.path.dirname(file_path))
print(os.path.dirname(FILE_NAME))
print(os.path.basename(file_path))
print(os.path.basename(FILE_NAME))
print(os.path.splitext(file_path))
print(os.path.splitext(FILE_NAME))

print(os.path.abspath(file_path))
print(os.path.exists(file_path))
print(os.path.exists('/zoo/marsupials/wombat'))

print(os.stat(file_path))

doomed_file = 'tyger_upper.txt'
if os.path.exists(doomed_file):
    os.remove(doomed_file)

raw_timestamp = os.path.getmtime(file_path)
from datetime import datetime

timestamp = datetime.fromtimestamp(raw_timestamp)
print(timestamp)

all_files = os.listdir(FOLDER)
print("all files:")
print(all_files)
