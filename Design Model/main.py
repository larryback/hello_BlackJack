#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys, os
from Game import Game

if __name__ == '__main__':
    
    ### 화면을 지운다.
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

    print("Welcom to Black Jack.")
    while True:
        blackjack = Game()
        blackjack.fn_start()

        ans = input('Are you continue (yes or no) ? ')
        if ans != 'yes':
            break
    
    print("Bye !, See you again.")


