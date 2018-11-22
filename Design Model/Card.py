#!/usr/bin/python
#-*- coding: utf-8 -*-

class Card():
	def __init__(self, rank, suit, points):
		self.rank = rank
		self.suit = suit
		self.points = points

	def __repr__(self):
		return self.suit + self.rank

	def getpoint(self):
		return int(self.points)

	def getrank(self):
		return str(self.rank)
