#!/usr/bin/env python
from datetime import date

today = date.today()
print(today)

james_bd = date(2014, 8, 1)
print(james_bd)

diff = today - james_bd
print(diff)

age_years, age_days = divmod(diff.days, 365)

print(age_years, age_days)


print(date.isoweekday(today))
print(date.weekday(today))

