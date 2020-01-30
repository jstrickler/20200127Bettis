#!/usr/bin/env python
import os
from datetime import datetime

#  current_dir, dir_list, file_list = os.walk(??)

target = "."
# target = os.path.abspath(".")

all_python_files = []

for curr_dir, dir_list, file_list in os.walk(target):
    if '.git' in dir_list:
        dir_list.remove('.git')
    print(curr_dir)
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            raw_ts = os.path.getmtime(file_path)
            ts = datetime.fromtimestamp(raw_ts).date()
            file_entry = ts, file_path
            all_python_files.append(file_entry)

for timestamp, file_path in sorted(all_python_files, reverse=True):
    print(timestamp, file_path)

