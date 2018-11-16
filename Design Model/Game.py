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
            state = self.player.fn_hit_or_stay()

            if state == 'hit':
                self.player.fn_deal(self.deck)
                continue
            else: break
        
        ### dealer 17 < ?? auto hit or 17 > &&  < 21 ?? auto stay or 21 > die
        ###
        while True:
            score = self.check_total_score(self.dealer)
            if(score < 17):
                self.player.fn_deal(self.deck)
                continue
            else: break

        if self.player.state == 'stay' and self.dealer.state == 'stay':
            self.fn_judge(self)

    def check_total_score(self, gamer):
        score = 0
        for card in gamer.cards:
            if card in "JQK":
                card = 10

            elif card == "A":
                ans = input("Do you select 1 or 11 ?") # TODO::
                card = int(ans)

            score += card
        
        return score

    def fn_stop(self):
        pass

    def fn_judge(self):
        dealer_score = self.check_total_score(self.dealer)
        player_score = self.check_total_score(self.player)

        print('Now, Start judged !!!')
        if(dealer_score > 21): print('WIN the player!!!')
        if(player_score > 21): print('WIN the dealer!!!')
        if(player_score > dealer_score): print('WIN the player!!!')
        else:print('WIN the dealer!!!')
        
        self.fn_stop()

