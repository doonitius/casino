from abc import ABC, abstractmethod
import random

class GameBoard:
    def __init__(self):
        self.__gameList = []

    def getGameList(self):
        return self.__gameList

    def getGameByID(self, game_id):
        return self.__gameList[game_id-1]

    def addGameToList(self, game):
        self.__gameList.append(game)

class Game:
    def __init__(self, game_id, name, desc, money_pool):
        self.__game_id = game_id
        self.__name = name
        self.__desc = desc
        self.__money_pool = money_pool

    def getGameId(self):
        return self.__game_id

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

    @abstractmethod
    def winGame(self):
        pass

    @abstractmethod
    def lostGame(self):
        pass

    @abstractmethod
    def userBet(self):
        pass

    @abstractmethod
    def play(self):
        pass


class Spin(Game):
    def __init__(self, game_id, name, desc, money_pool):
        Game.__init__(self, game_id, name, desc, money_pool)
        self.__possible_multiply = float

    def play(self):
        pass

    def getMultiply(self):
        return self.__possible_multiply

    def setMultiply(self, possible_multiply):
        self.__possible_multiply = possible_multiply

class ColorRoulette(Game):
    def __init__(self, game_id, name, desc, money_pool):
        Game.__init__(self, game_id, name, desc, money_pool)

    def play(self, user_value, choose_number):
        #value 1=red 2=black 3=even 4=odd 5=number
        result = 0 #-1=draw 0=lose 1=win

        redNumList = [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36]
        blackNumList = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35]

        rng = random.randint(1, 36)
        in_red = False
        print("Roulette: " , rng)

        in_red = rng in redNumList

        match user_value:
            case 1:
                if in_red: result = 1
            case 2:
                if not in_red: result = 1
            case 3:
                if rng % 2 == 0: result = 1
            case 4:
                if rng % 2 != 0: result = 1
            case 5:
                if rng == choose_number: result = 1
        return result

    def winGame(self):
        return self.__player_bet * 2

    def lostGame(self):
        return float(0)

    def drawGame(self):
        pass

    def userBet(self, player_bet):
        self.__player_bet = float(player_bet)

class HighLow(Game):
    def __init__(self, game_id, name, desc, money_pool):
        Game.__init__(self, game_id, name, desc, money_pool)
        self.__possible_number = int

    def play(self, user_value):
        rng = random.randint(1,12)
        result = 0
        #high = 1 low =2
        match user_value:
            case 1:
                if rng > 6 and rng <= 12: result = 1
            case 2:
                if rng > 6 and rng <= 12: result = 1
        return result

    def winGame(self):
        return self.__player_bet * 2

    def lostGame(self):
        return float(0)

    def drawGame(self):
        pass

    def userBet(self, player_bet):
        self.__player_bet = float(player_bet)

class Slot(Game):
    def __init__(self, game_id, name, desc, money_pool, possible_face):
        Game.__init__(self, game_id, name, desc, money_pool)
        self.__possible_face = possible_face

    def play(self):
        pass

class RPS(Game):
    def __init__(self, game_id, name, desc, money_pool):
        Game.__init__(self, game_id, name, desc, money_pool)
        # self.__choice = int

    def play(self, user_choose):
        rng = random.randint(1, 3)
        result = 0
        #rock = 1 paper = 2 scissor = 3

        #case draw
        if user_choose == rng : result = -1

        #case player win
        if user_choose == 1 and rng == 3 : result = 1

        #case player win
        if user_choose == 2 and rng == 1 : result = 1

        #case player win
        if user_choose == 3 and rng == 2 : result = 1

        return int(result)

    def winGame(self):
        return self.__player_bet * 1.5

    def lostGame(self):
        return float(0)

    def drawGame(self):
        return self.__player_bet

    def userBet(self, player_bet):
        self.__player_bet = float(player_bet)

class BlackJack(Game):
    def __init__(self,  game_id, name, desc, money_pool, dealerHand, playerHand, winCondition):
        Game.__init__(self, dealerHand, playerHand, winCondition)
        self.__dealerHand =dealerHand
        self.__playerHand =playerHand
        self.__winCondition = winCondition

    def play(self):
        pass

    def hit():
        pass

    def stay():
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