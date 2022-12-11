class GameBoard:
    def __init__(self):
        self.__gameList = []

    def getGameList(self):
        return self.__gameList

    def getGameByID(self, game_id):
        return self.__gameList[game_id]

    def addGameToList(self, game):
        return self.__gameList.append(game)

class Game:
    def __init__(self, game_id, name, desc, money_pool):
        self.__game_id = game_id
        self.__name = name
        self.__desc = desc
        self.__money_pool = money_pool

    def getName(self):
        return self.__name

    def getDesc(self):
        return self.__desc

    def getMoneyPool(self):
        return self.__money_pool

    def setName(self, name):
        self.__name = name

    def setDesc(self, desc):
        self.__desc = desc

    def setMoneyPool(self, money_pool):
        self.__money_pool = money_pool

class Spin(Game):
    def __init__(self, game_id, name, desc, money_pool, possible_multiply):
        super().__init__(self, game_id, name, desc, money_pool)
        self.__possible_multiply = possible_multiply

    def playSpin(self):
        pass

class ColorRoulette(Game):
    def __init__(self, game_id, name, desc, money_pool, possible_color):
        super().__init__(self, game_id, name, desc, money_pool)
        self.__possible_color = possible_color

    def playRoulette(self):
        pass

class HighLow(Game):
    def __init__(self, game_id, name, desc, money_pool):
        super().__init__(self, game_id, name, desc, money_pool)
        self.__possible_number = int

    def playHighLow(self):
        pass

class Slot(Game):
    def __init__(self, game_id, name, desc, money_pool, possible_face):
        super().__init__(self, game_id, name, desc, money_pool)
        self.__possible_face = possible_face

    def playSlot(self):
        pass

class RPS(Game):
    def __init__(self, game_id, name, desc, money_pool):
        super().__init__(self, game_id, name, desc, money_pool)
        self.__choice = int

    def playRPC(self):
        pass

class PlayGame(Game):
    def playGame(self):
        pass
    def winGame(self):
        pass

    def lostGame(self):
        pass

    def userBet(self, player_bet):
        self.__player_bet = player_bet