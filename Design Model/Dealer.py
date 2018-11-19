#!/usr/bin/python
#-*- coding: utf-8 -*-

from Player import Player

class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []
