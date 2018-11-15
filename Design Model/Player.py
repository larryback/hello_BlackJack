#!/usr/bin/python
#-*- coding: utf-8 -*-

from Deck import Deck

class Player:
    def __init__(self):
        self.name = 'Player'
        self.cards = []
        self.state = 'stay' # or 'hit'

    def fn_hit(self, ):
        pass

    def fn_stay(self, ):
        pass

    def fn_hit_or_stay(self, ):
        while True:
            ans = input("Do you hit or stay ('h' or 's') ? ")
            if 'h' in ans:
                self.state = 'hit'
                break
            elif 's' in ans:
                self.state = 'stay'
                break

    def fn_deal(self, deck, show=True):
        """
        show : True (default) 카드를 보여준다
               False 보여주지 않는다
        """
        self.cards = deck.fn_deal(1)
    
        if show:    print(self.name, self.cards)
        else:       print(self.name, 'hidden', self.cards)


