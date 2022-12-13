from game.bet_helper import placeBet
from controller.game_controller import addGameToList
from controller.account_controller import accountDeposit, accountWithdraw

def createRoulette():
    return addGameToList('Color Roulette', 'Wheel of fortune that random 1 number out. Player will guess what the number will be or color it will be')

def playRoulette(roulette, current_user, user_choose, user_bet, user_number):
    accountWithdraw(current_user, user_bet, 'Place Bet')
    roulette = placeBet(roulette, user_bet)
    result = roulette.play(user_choose, user_number)
    match result:
        case 0:
            print("you lost lele")
            price = roulette.lostGame()
        case 1:
            print("You win wa yedke")
            price = roulette.winGame()
            accountDeposit(current_user, price, 'Win Color Roulette')
    return result
