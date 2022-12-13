from controller.game_controller import addGameToList
from controller.account_controller import accountDeposit, accountWithdraw
from game.bet_helper import placeBet

def createBlackJack():
    return addGameToList('Black Jack', 'Player random 2 cards. "Bust" is to exceed the Blackjack value (Lose) "hit" for ask more card "stay" for stand this 2 cards')

def playBlackjack(blackjack, current_user, user_bet):
    accountWithdraw(current_user, user_bet, 'Place Bet')
    blackjack = placeBet(blackjack, user_bet)
    return blackjack

def checkResult(blackjack, current_user, action):
    player_hand, dealer_hand, result = blackjack.checkDealer(action)

    match result:
        case 0:
            print("haha loser")
            price = blackjack.lostGame()
        case 1:
            print("Damn you cheater")
            price = blackjack.winGame()
            accountDeposit(current_user, price, 'Win BlackJack')
        case -1:
            print("Good but not enough")
            price = blackjack.drawGame()
            accountDeposit(current_user, price, 'Draw BlackJack')

    return player_hand, dealer_hand, result

