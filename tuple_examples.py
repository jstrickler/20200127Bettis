#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

person = ('Bill', 'Gates', 'Microsoft', '1955-10-28')

print(person)

print(person[0], person[1])
print(len(person), person[:2])

first_name, last_name, product, dob = person

#  var-list = iterable

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
    ('John', 'Strickler', '1956-10-31'),
]

print(people[0])
print(people[0][0])
print(people[0][0][0])
print(people[-1][-1])
print()

for first_name, last_name, *product, dob in people:
    # first_name, last_name, product, dob = next(people)
    print(first_name, last_name, product)
print()

the_time = '11:22:37'
hour, minute, second = the_time.split(':')

data = [('A', 5), ('C', 3), ('F', 22), ('H', 9)]

for letter, number in data:
    print(letter * number)
print()
print('spam' * 10)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)

