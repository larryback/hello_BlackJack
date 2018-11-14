#!/usr/bin/python
#-*- coding: utf-8 -*-

from Deck import Deck

class Player:
    def __init__(self):
        self.name = 'Player'
        self.cards = []

    def fn_hit(self, ):
        pass

    def fn_stay(self, ):
        pass

    def fn_hit_or_stay(self, ):
        pass

    def fn_deal(self, deck, show=True):
        """
        show : True (default) 카드를 보여준다
               False 보여주지 않는다
        """
        card = deck.fn_deal()
        self.cards.append(card)
    
        print("{}가 카드를 받았습니다.".format(self.name))
        if show:
            print("카드는 {} - {}입니다.".format(self.cards[0].suit, self.cards[0].face))

    def card_1(self, ):
        pass

