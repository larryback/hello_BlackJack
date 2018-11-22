#!/usr/bin/python
#-*- coding: utf-8 -*-

from random import choice
from Card import Card

class Deck():
	def __init__(self, size=1):
		#init card element ranks and values pair dictionary
		rank = {'A':11, '2': 2, '3':3, '4':4, '5':5, '6':6,'7': 7,'8':8 ,'9':9 , '10':10, 'J':10, 'Q':10, 'K':10} 
		suit = ['S', 'C', 'D', 'H']

		#create deck list
		self.deck = []
		for s in suit:
			for key in rank:
				self.deck.append(Card(str(key), s, rank[key]))
				
		#create shoe dictionary
		self.reset_shoe(size)

		#print(list(self.shoe))

	def reset_shoe(self, size = 1):
		self.shoe = {}
		for card in self.deck:
			self.shoe[card] = size
	
	def deal_card(self):
		'''deals a card from the deck'''
		onecard = choice(list(self.shoe.keys()))  

		if self.shoe[onecard] == 0:
			return self.deal_card()
		else:
			self.shoe[onecard] -= 1
			
		return onecard