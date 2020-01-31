#!/usr/bin/env python
from subprocess import run, PIPE, CalledProcessError
from glob import glob  # to expand filename wildcards
import shlex  #  for shlex.split()

cmd = "netstat -an"

# insecure on non-Windows platforms
# run(cmd, shell=True)

cmd_words = shlex.split(cmd)
print("cmd_words:", cmd_words)
try:
    proc = run(cmd_words, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err)
    print(err.returncode)
else:
    stdout = proc.stdout.decode()
    for line in stdout.splitlines():
        if "ESTAB" in line:
            print(line)

    print(proc.stderr.decode())




