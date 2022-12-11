from tkinter import *
from tkinter import ttk
import random

def playRPS(chosen, bet):
    #Rock = 1 Paper = 2 Scissor = 3
    rng = random.randint(1,3)
    result = 0 #-1=draw 0=lose 1=win

    if (chosen == rng):
        #prize = bet
        result = -1
        return result
    
    if (chosen == 1):
        if (rng == 3):
            #winGame(bet)
            result = 1
            print('win', chosen, rng)
        else:
            #loseGame(bet)
            print('lose', chosen, rng)
    
    if (chosen == 2):
        if (rng == 1):
            #winGame(bet)
            result = 1
            print('win', chosen, rng)
        else:
            #loseGame(bet)
            print('lose', chosen, rng)

    if (chosen == 3):
        if (rng == 2):
            result = 1
            #winGame(bet)
            print('win', chosen, rng)
        else:
            #loseGame(bet)
            print('lose', chosen, rng)
    return result