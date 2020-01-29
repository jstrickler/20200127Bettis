#!/usr/bin/env python

# mary_in = open('DATA/mary.txt')
# mary_in.close()

# with open('DATA/mary.txt') as mary_in:
#     print(mary_in.closed)
#
# print(mary_in.closed)

# read each line into a string
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

# read entire file into a string
with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("COOKED:")
    print(contents)
print('-' * 60)

# read into list of strings (with NL)
with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)

# read into list of strings (without NL)
with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)

with open('DATA/noisewords.txt') as noise_in:
    noise_words = [w.rstrip() for w in noise_in]
    print(noise_words)
print('-' * 60)

try:
    with open('DATA/quacks.txt') as quacks_in:
        pass
except IOError as err:
    print(err)

