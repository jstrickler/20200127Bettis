#!/usr/bin/env python

x = 100  # GLOBAL variable

if x > 50:
    name = "Bonzo"

def spam():
    animal = "wombat"   # LOCAL variable
    print(animal)
    return animal

x = spam()

print(name)
print(x)

