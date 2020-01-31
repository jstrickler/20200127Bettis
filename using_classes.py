#!/usr/bin/env python
import re
from datetime import date


rx = re.compile(r'^\d+$')

print(rx.search('12345'))

x = date(2019, 9, 22)
print(x)
print(type(x))

m = 5

m = int(5)

s = "wombat"

s = str("wombat")


print(s.upper())


date.
