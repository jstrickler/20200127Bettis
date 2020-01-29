#!/usr/bin/env python
from pprint import pprint
letter_counts = {}

with open('DATA/words.txt') as words_in:
    for line in words_in:
        first_letter = line[0]

        if first_letter not in letter_counts:
            letter_counts[first_letter] = 0

        letter_counts[first_letter] += 1

        # letter_counts[first_letter] = letter_counts[first_letter] + 1

pprint(letter_counts)
