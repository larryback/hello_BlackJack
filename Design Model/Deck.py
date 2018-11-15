#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
# from Card import Card

class Deck:
    def __init__(self):
        self.__init_deck__()

    def __init_deck__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        self.fn_shuffle()

    def fn_shuffle(self, ):
        random.shuffle(self.deck)

    def fn_deal(self, n):
        self.cards = []
        if len(self.deck) < n:
            self.__init_deck__()
            self.fn_shuffle()

        for i in range(n):
            card = self.deck.pop()
            if card == 11: card = "J"
            if card == 12: card = "Q"
            if card == 13: card = "K"
            if card == 14: card = "A"
            self.cards.append(card)
            
        return self.cards
