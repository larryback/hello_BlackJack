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

<<<<<<< HEAD
        ans = input('Are you continue (yes or no) ? ')
        if ans != 'yes':
            break
    
=======
        ans = raw_input("Are you continue the game('y' or 'n') ? ")
        if 'n' in ans:
            break;
    hasattr
>>>>>>> 0b27893d67eb3c38adb28ec19bd1fc62fbd85220
    print("Bye !, See you again.")


