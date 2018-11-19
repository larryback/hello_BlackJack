#!/usr/bin/python
#-*- coding: utf-8 -*-

from Dealer import Dealer
from Player import Player
from Deck   import Deck

class Game:
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck   = Deck(1)

    def initial_cards(self):
        self.player.hand.append(self.deck.deal_card())
        self.dealer.hand.append(self.deck.deal_card())
        self.player.hand.append(self.deck.deal_card())
        self.dealer.hand.append(self.deck.deal_card())
        return [self.dealer.hand, self.player.hand]

    def fn_start(self):
        self.initial_cards()
        print("dealer : ", self.dealer.hand)
        print("player : ", self.player.hand)

        while True:
            if input("Hit or Stay ?") == 'h':
                self.hit_player_cards()
                print("dealer : ", self.dealer.hand)
                print("player : ", self.player.hand)
            else:
                break;

        self.hit_dealer_cards()

        dealer_score = self.hand_points(self.dealer.hand)
        print(dealer_score)

        player_score = self.hand_points(self.player.hand)
        print(player_score)

    def hit_player_cards(self):
        total = self.hand_points(self.player.hand)
        if total < 21:
            self.player.hand.append(self.deck.deal_card())
        else:
            print('dealer WIN!!!')

        return [self.dealer.hand, self.player.hand]

    def hit_dealer_cards(self):
        while True:
            total = self.hand_points(self.dealer.hand)
            if total > 21:
                print('player WIN!!!')
                break
            if total < 17:
                self.dealer.hand.append(self.deck.deal_card())
                print(self.dealer.hand)
                total = self.hand_points(self.dealer.hand)
            else:
                break
                
        return [self.dealer.hand, self.player.hand]


    def hand_points(self, hand):
        total = 0
        for cards in hand:
            total += cards.getpoint()

        if total > 21:
            for cards in hand:
                if cards.getrank() == 'A':
                    total -= 10
                    if total <= 21:
                        break
        return total



