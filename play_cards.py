#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Fred")
print(d1)

d2 = CardDeck("Rita")
print(d2)

# print(d1._dealer)
# print(d2._dealer)

# print(d1.get_dealer())
# d1.set_dealer('Bob')

print(d1.dealer)
d1.dealer = "Bob"

print(d1.color)
print(d1.dealer)

try:
    d1.dealer = 5.7
except TypeError as err:
    print(err)

d1.shuffle()
print(d1.cards)
print()
for i in range(5):
    print(d1.draw())

print(len(d1))
print(d1)
print(repr(d1))

d3 = d1 + d2

print(d3)
print(d1[-1])
print(d1.draw())

print(d1.get_ranks())
print(CardDeck.get_ranks())

j1 = JokerDeck("Fred")
print(j1)
print(len(j1))
j1.shuffle()
print(j1.draw())
print(j1.cards)

