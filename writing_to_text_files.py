#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

MODE = 'w'

with open('fruitdata.txt', MODE) as fruit_out:
    for fruit in fruits:
        fruit_out.write(fruit + '\n')


with open('DATA/tyger.txt') as tyger_in:
    with open('tyger_upper.txt', 'w') as tyger_out:
        for line in tyger_in:
            if 'y' in line:
                tyger_out.write(line.upper())
