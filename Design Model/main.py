#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys, os
from Game import Game

if __name__ == '__main__':
    
    ### 화면을 지운다.
    # if os.name == 'nt': os.system('cls')
    # else: os.system('clear')
    
    print("Welcom to Black Jack.")
    while True:
        Game().fn_start()

        ans = input("Are you continue the game('y' or 'n') ? ")
        if 'n' in ans:
            break;
    hasattr
    print("Bye !, See you again.")
<<<<<<< HEAD
    
=======


>>>>>>> dc5802272e10c2534f1bb86679c1f0f8f35411e4
