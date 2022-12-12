from tkinter import *
from tkinter import ttk
import random
from view.blackjack import playWindow

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

def playHighLow(value, bet):
    result = 0 #-1=draw 0=lose 1=win
    #High=1 Low=2
    rng = random.randint(1,12)

    if (value == 1):
        if (rng > 6 and rng <= 12):
            #winGame(bet)
            result = 1
            print('win', value, rng)
        else:
            #loseGame(bet)
            print('lose', value, rng)
    else:
        if (rng > 0 and rng <= 6):
            #winGame(bet)
            result = 1
            print('win', value, rng)
        else:
            #loseGame(bet)
            print('lose', value, rng)
    return result

def playRoulette(value, bet, chosen):
    #value 1=red 2=black 3=even 4=odd 5=number
    result = 0 #-1=draw 0=lose 1=win

    redNumList = [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36]
    blackNumList = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35]

    rng = random.randint(1,36)
    in_red = False
    print(rng)

    for num in redNumList:
        if (rng == num):
            in_red = True

    if (value == 1 and in_red):
        result = 1
    elif (value == 2 and not in_red):
        result = 1
    elif (value == 3 and (rng % 2 == 0)):
        print(rng % 2)
        result = 1
    elif (value == 4 and (rng % 2 != 0)):
        print(rng % 2)
        result = 1
    elif (value == 5 and rng == chosen):
        print(chosen, rng)
        result = 1

    # if (result ==1):
    #     #winGame(bet)
    # else:
    #     #lostGame(bet)

    return result

def playBlackjack(bet, app, current_user):
    playWindow(app, current_user)

def beginGame():
    player_hand = []
    dealer_hand = []

    for i in range(0,2):
        player_random = randomNumberForBlackjack()
        dealer_random = randomNumberForBlackjack()
        player_hand.append(player_random)
        dealer_hand.append(dealer_random)
    
    return player_hand, dealer_hand

def randomNumberForBlackjack():
    return random.randint(1,10)