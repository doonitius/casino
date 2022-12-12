from tkinter import *
from tkinter import ttk
import random
from model.game import Game, RPS
from controller.game_controller import addGameToList
from controller.account_controller import accountDeposit, accountWithdraw

def createRPS():
    return addGameToList('RPS', 'Rock Paper Scissor')



def placeBet(rps, bet):
    rps.userBet(bet)
    return rps

def playRPS(rps,current_user, user_choose, user_bet):
    accountWithdraw(current_user, user_bet, 'Place Bet')
    rps = placeBet(rps, user_bet)
    result = rps.play(user_choose)
    match result:
        case 0:
            print("You lose haah")
            price = rps.lostGame()
        case -1:
            print("Damn draw")
            price = rps.drawGame()
            accountDeposit(current_user, price, 'Draw RPS')
        case 1:
            print("wow you win")
            price = rps.winGame()
            accountDeposit(current_user, price, 'Win RPS')
    return result


# def playRPS(chosen, bet):
#     #Rock = 1 Paper = 2 Scissor = 3
