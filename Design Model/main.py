#!/usr/bin/python
#-*- coding: utf-8 -*-

#yimport sys, os
from Game import Game

if __name__ == '__main__':
    
    ### 화면을 지운다.
    # if os.name == 'nt': os.system('cls')
    # else: os.system('clear')
    
    print("Welcom to Black Jack.")
    while True:
        game = Game()
        game.fn_start()

        ans = input("Do you continue the game('y' or 'n') ? ")
        if 'y' in ans:
            game.deck.reset_shoe()
        
        else:
            break
    print("Bye !, See you again.")
    
