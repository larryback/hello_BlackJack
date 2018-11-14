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
        pass

    def fn_stop(self, ):
        pass

    def fn_judge(self, ):
        pass

