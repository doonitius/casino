from controller.user_controller import addUserToList, showUserList
from controller.account_controller import accountDeposit, accountGetBalance, accountWithdraw
from controller.transaction_controller import showTransactionLog
from controller.game_controller import addGameToList, showGameList, getGame, removeGameFromList
from game.rps import createRPS, playRPS
from game.highlow import createHighlow, playHighLow
from game.roulette import createRoulette
from game.blackjack import createBlackJack

addUserToList('jade', '8888', 0)

current_user =1
game_id = 1
showUserList()

print("hellow")

print(accountGetBalance(current_user))

accountDeposit(current_user, 100, 'Deposit')

print(accountGetBalance(current_user))

accountWithdraw(current_user, 50, 'Withdraw')

print(accountGetBalance(current_user))

for transaction in showTransactionLog(current_user):
    print(transaction.displayTransaction())

for game in showGameList():
    print(game.getName(), game.getDesc())

createRPS()

for game in showGameList():
    print(game.getGameId(), game.getName(), game.getDesc())

game = getGame(game_id)

print(game.getName(), game.getDesc())

playRPS(game, current_user,  1, 50)

for transaction in showTransactionLog(current_user):
    print(transaction.displayTransaction())

print("current balance", accountGetBalance(current_user))

createHighlow()

for game in showGameList():
    print(game.getGameId(), game.getName(), game.getDesc())

createRoulette()
createBlackJack()

for game in showGameList():
    print(game.getGameId(), game.getName(), game.getDesc())

