from controller.game_controller import addGameToList
from controller.account_controller import accountDeposit, accountWithdraw
from game.bet_helper import placeBet

def createHighlow():
    return addGameToList('HighLow', 'Number will random from 1-12 and you have to choose high or low we get from random number')

def playHighLow(highlow, current_user, user_value, user_bet):
    accountWithdraw(current_user, user_bet, 'Place Bet')
    highlow = placeBet(highlow, user_bet)
    result = highlow.play(user_value)
    match result:
        case 0:
            print("You lose kak")
            price = highlow.lostGame()
        case 1:
            print("Uwu YoU WiN")
            price = highlow.winGame()
            accountDeposit(current_user,price, 'Win HighLow')
    return result