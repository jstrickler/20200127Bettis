#!/usr/bin/env python
import sys
from nnl.steam.bettislib import propel, design


propel()
design()

# bettislib.design()

# sys.modules['bettislib'].design()  weird and maybe bad

for path in sys.path:
    print(path)

