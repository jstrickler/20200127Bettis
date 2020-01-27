#!/usr/bin/env python
with open('DATA/noisewords.txt') as noisewords_in:
    noise_words = {w.rstrip() for w in noisewords_in}
    noise_words.add('a')  # not in file for some reason

if __name__ == '__main__':
    print(noise_words)

