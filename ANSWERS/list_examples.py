#!/usr/bin/env python
import sys

list1 = list()  # new empty list
list2 = ['a', 'b', 'c']
list3 = []
word_string = 'wombat tractor koala'
words = word_string.split()
print(words)

places = ['Munhall', 'Homestead', 'McKeesport']

print(places)
print(places[0], places[-1], places[2])
# print(places[3]) # error!

places.append('West Homestead')
places.append('Boston')
places.append('Confluence')
print(places)

places.insert(0, "Southside")
places.insert(4, 'Ohiopyle')
print(places)

more_places = ['Sewickley', 'Beaver Falls', 'Rochester']

places.extend(more_places)

print(places)

# L.append(obj)
# L.insert(where, obj)
# L.extend(iterable)

del places[9]
print(places)

places.remove('Confluence')
print(places)

x = places.pop()
print(x)
print(places)

x = places.pop(1)
print(x)
print(places)

# del L[n]
# L.remove(value)
# L.pop()  L.pop(index)

places[1] = 'Squirrel Hill'

print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(fruits[0], fruits[5], fruits[-2], '\n')

# SLICES
# A[n]  A[start:stop]  A[start:]  A[:stop]
# A[start:stop:step]

print(fruits[0:3], '\n')
print(fruits[:3], '\n')
print(fruits[2:6], '\n')
print(fruits[10:], '\n')
print(fruits[-5:], '\n')
print(fruits[-10:-5], '\n')

actor = 'Chris Hemsworth'
print(actor[:5])
print(actor[6:9])
print(actor[-5:])

for fruit in fruits:
    # fruit = next(fruits)
    print(fruit)

# for VAR in ITERABLE:
#    ....VAR....

for ch in actor:
    print(ch)

for fruit in fruits[:10]:
    print(fruit)

for file_name in sys.argv[1:]:
    print(file_name)

s = ":wombat:"
s2 = s[1:-1]
print(s2)

print(s.strip(':'))

x = """

struct foo {
   int x;
   float y;
   char *doodle;
}

"""

