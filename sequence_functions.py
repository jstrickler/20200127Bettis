#!/usr/bin/env python

a = [9, 18, 4, 56, 1, 2, 3]
b = "Mark", "Zuckerberg", "Facebook", 'Spam', 'Ham'
c = "Wombat"

print(len(a), len(b), len(c))
print(sum(a))
print(min(a), min(b), min(c))
print(max(a), max(b), max(c))
print(sorted(a), sorted(b), sorted(c))
print(reversed(a), reversed(b), reversed(c))
print(enumerate(a), enumerate(b), enumerate(c))


for i, thing in enumerate(b):
    print(i, thing)

e = enumerate(b)
print(list(e))
print(list(e))

print(reversed(b))
for x in reversed(b):
    print(x)


with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        print(raw_line)
print()

for i in range(1, 6):
    print(i * '*')
print()

r = range(3)
print(r)
for i in r:
    print("WOMBAT!")

# range(STOP)  range(START, STOP) range(START, STOP, STEP)

for i in r:
    print("WOMBAT!")

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

start = 3
stop = 11
print(fruits[start:stop])

s = slice(start, stop)
print(fruits[s])
