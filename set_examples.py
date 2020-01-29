#!/usr/bin/env python

folder1 = ['foo.txt', 'spam.txt', 'ham.txt', 'eggs.txt']
folder2 = ['foo.txt', 'bar.txt', 'blah.txt', 'spam.txt']

f1 = set(folder1)
f2 = set(folder2)

print("common:", f1 & f2)
print("not common:", f1 ^ f2)
print("both:", f1 | f2)
print("just f1:", f1 - f2)
print("just f2:", f2 - f1)

print('foo.txt' in f1)

food = ['spam', 'spam', 'spam', 'spam', 'eggs', 'spam']

unique_food = set(food)
print(unique_food)
