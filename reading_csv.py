#!/usr/bin/env python
import csv

with open('DATA/presidents.csv') as potus_in:
    rdr = csv.reader(potus_in)
    for row in rdr:
        print(row)

with open('DATA/knights.txt') as knights_in:
    with open('knights.csv', 'w') as knights_out:
        wtr = csv.writer(knights_out)
        for raw_line in knights_in:
            fields = raw_line.rstrip().split(':')
            wtr.writerow(fields)


