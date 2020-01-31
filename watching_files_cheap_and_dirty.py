#!/usr/bin/env python
import os
import time

files_to_look_for = {
    'ham': False,
    'spam': False,
    'toast': False,
}

while True:
    for file_name in files_to_look_for:
        if os.path.exists(file_name):
            if files_to_look_for[file_name]:
                continue
            #  process file
            print("processing", file_name)
            files_to_look_for[file_name] = True
    time.sleep(1)
