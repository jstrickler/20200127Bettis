#!/usr/bin/env python
from carddeck import CardDeck, Card

class JokerDeck(CardDeck):

    def _build_deck(self):
        super()._build_deck()
        j1 = Card("Joker1", "Joker")
        j2 = Card("Joker2", "Joker")
        self._cards.append(j1)
        self._cards.append(j2)
