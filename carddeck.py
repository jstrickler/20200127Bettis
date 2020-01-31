#!/usr/bin/env python
from dataclasses import dataclass
import random

@dataclass
class Card:
    rank: str
    suit: str

    def __str__(self):
        return '{}/{}'.format(
            self.rank, self.suit
        )

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self._dealer = dealer
        self._build_deck()


    def _build_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards


    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    # getter property
    @property
    def dealer(self):
        return self._dealer

    # setter property
    @dealer.setter
    def dealer(self, value: str):
        if isinstance(value, str):
            self._dealer = value
        else:
            raise TypeError("Dealer must be a string")

    @property
    def color(self):
        return "BLUE"



    # dealer = property(dealer)

    @property
    def back_image(self):
        return self._back_image

    @back_image.setter
    def back_image(self, value):
        self._back_image = value

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_name = type(self).__name__
        return "{}({},{})".format(
            my_name,
            self.dealer,
            len(self)
        )

    def __repr__(self):
        my_name = type(self).__name__
        return '{}("{}")'.format(
            my_name,
            self.dealer,
        )

    def __add__(self, other):
        tmp = type(self)(self.dealer)
        tmp._cards = self.cards + other.cards
        return tmp

    def __getitem__(self, index):
        return self._cards[index]


    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @staticmethod
    def bark():
        print("Woof! Woof!")

