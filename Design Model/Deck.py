#!/usr/bin/python
#-*- coding: utf-8 -*-

from Card import Card

class Deck:
    def __init__(self):
        self.card = Card("2", "S")

    def fn_shuffle(self, ):
        pass

    def fn_deal(self, ):
        print('한장을 주었습니다.')
        return self.card

