from model.game import RPS, HighLow, ColorRoulette, BlackJack
from controller.object_controller import getGameList, id_generator, updateGameList

def showGameList():
    game_list = getGameList()

    return game_list.getGameList()

def getGame(game_id):
    game = getGameList()
    current_game = game.getGameByID(game_id)

    return current_game

def addGameToList(game_name, desc):
    game_list = getGameList()
    game_id = id_generator(game_list.getGameList())

    match game_name:
        case 'RPS':
            print("creating RPS")
            newGame = RPS(game_id, game_name, desc, 0)
        case 'HighLow':
            print("creating Highlow")
            newGame = HighLow(game_id, game_name, desc, 0)
        case 'Color Roulette':
            print("creating Color Roulette")
            newGame = ColorRoulette(game_id, game_name, desc, 0)
        case 'Black Jack':
            print("creating Black Jack")
            newGame = BlackJack(game_id, game_name, desc, 0)

    game_list.addGameToList(newGame)
    updateGameList(game_list)
    print("added game successfully")
    return game_id

def removeGameFromList(game_id):
    game_list = getGameList()
    current_game = game_list.getGameList().pop(game_id-1)
    name = current_game.getName()
    del current_game
    updateGameList(game_list)
    print(name, "closed")