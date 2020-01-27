#!/usr/bin/env python

actor = "John Wayne"
value = 23/17
thing = 555

print(actor)
print(value)
print(thing)
print(actor, value, thing)
print()
print()
print("wheeeeee!")

print(actor, value, thing, sep=',')
print(actor, value, thing, sep=':')
print(actor, value, thing, sep='==')
print(actor, value, thing, sep='')

print(actor, end=' ')
print(value)

print(value)
print("value is {:.3f}".format(value))

print("=> {} => {}".format(value, thing))

animal = "wombat"
print("|{:20}|".format(animal))
print("|{:>20}|".format(animal))
print("|{:^20}|".format(animal))

big_num = 2309203948230984
print("{:,d}".format(big_num))

print(f"value is {value:.3f}")
print(f"{thing} {value:.3f}")

