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

        while True:
            self.player.fn_hit_or_stay()
            if self.player.state == 'h':
                self.player.fn_deal(self.deck)
                continue
            else:
                break
        
        ### dealer 17 < ?? auto hit or 17 > &&  < 21 ?? auto stay or 21 > die
        ###

        if self.player.state == 'stay' and self.dealer.state == 'stay':
            self.fn_judge(self)

    def fn_stop(self):
        pass

    def fn_judge(self):
        pass

