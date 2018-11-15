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
        self.player.fn_deal(self.deck) # player's first card
        self.dealer.fn_deal(self.deck) # dealer's first card
        self.player.fn_deal(self.deck) # player's second card
        self.dealer.fn_deal(self.deck, False) # dealer's second card

        ### loop...
        self.player.fn_hit_or_stay()
        if self.player.state:
            pass
        ###
        pass

    def fn_stop(self, ):
        pass

    def fn_judge(self, ):
        pass

