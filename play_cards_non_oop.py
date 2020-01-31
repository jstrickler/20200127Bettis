#!/usr/bin/env python
import random

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = 'Clubs Diamonds Hearts Spades'.split()

def make_cards():
    cards = []
    for suit in SUITS:
        for rank in RANKS:
            card = rank, suit
            cards.append(card)
    return cards

def shuffle_cards(cards):
    random.shuffle(cards)

def draw(cards):
    card = cards.pop()
    return card

d1 = make_cards()
shuffle_cards(d1)

c1 = draw(d1)
print(c1)
print(d1)

#----------------------------------------
d1 = CardDeck()
d1.shuffle()
print(d1.cards)
c = d1.draw()

