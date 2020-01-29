#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

print(sorted(fruits), '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(sorted(nums), '\n')

print(sorted(fruits, reverse=True), '\n')
print(sorted(nums, reverse=True), '\n')



print(sorted(fruits, key=str.lower), '\n')


def ignore_case(fruit):
    return fruit.lower()

print(sorted(fruits, key=ignore_case), '\n')


print(sorted(fruits, key=len), '\n')

def len_and_name(f):
    return len(f), f.lower()

print(sorted(fruits, key=len_and_name), '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(person):
    return person[1], person[0]

for first_name, last_name, product, dob in sorted(people, key=by_dob):
    print(first_name, last_name, dob)
print()

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YYZ': 'Toronto',
    'YOW': 'Ottawa',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YYC': 'Calgary',
    'IAD': 'Dulles',
}


def by_name(airport):
    return airport[1]

for abbr, name in sorted(airports.items(), key=by_name):
    print(abbr, name)
print()

# print(airports.items())


for abbr, name in sorted(airports.items(), key=lambda a: a[1]):
    print(abbr, name)
print()

#  lambda PARAM ...: RETURN-VALUE
