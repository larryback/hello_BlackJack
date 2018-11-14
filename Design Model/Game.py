#!/usr/bin/python
#-*- coding: utf-8 -*-

from Dealer import Dealer
from Player import Player
from Deck   import Deck

class Game:
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck   = Deck()

    def fn_start(self, ):
        print("두장의 카드를 나누어 준다.")
        self.player.fn_deal() # player's first card
        self.dealer.fn_deal(False) # dealer's first card
        self.player.fn_deal() # player's second card
        self.dealer.fn_deal() # dealer's second card
        pass

    def fn_stop(self, ):
        pass

    def fn_judge(self, ):
        pass

