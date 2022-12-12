from tkinter import *
from tkinter import ttk
import view.role_window
import view.message_box
from game.game import playRPS, playHighLow, playRoulette, playBlackjack
from game.rps import playRPS
from controller.account_controller import accountGetBalance
from controller.game_controller import getGame
from game.rps import createRPS

# put in controller 
def checkInt(value):
    try:
        int_player_chosen = int(value)
    except ValueError:
        # print("not a valid integer", value)
        return False
    else:
        # print("value is", int_player_chosen)
        return True

# put in controller
def gameResult(result):
    if (result == 1): view.message_box.winGameMes()
    elif (result == 0): view.message_box.loseGameMes()
    else: view.message_box.drawGameMes()


def getBalance(current_user):
    print("current balance", accountGetBalance(current_user))

# put in controller
def validateRPS(chosen, bet, game, current_user):
    check_chosen = checkInt(chosen)
    check_bet = checkInt(bet)

    if (check_chosen and check_bet):
        if (int(chosen) < 1 or int(chosen) > 3):
            view.message_box.inputError()
        else:
            result = playRPS(game, current_user, int(chosen), int(bet))
            gameResult(result)
    else: 
        view.message_box.inputError()

# Maybe abtract validate game from bet and choice that player make
def validateHighLow(value, bet):
    check_bet = checkInt(bet)

    if (check_bet):
        result = playHighLow(value, int(bet))
        gameResult(result)
    else:
        view.message_box.inputError()

# put in controller
def validateRoulette(value, bet, chosen):
    check_bet = checkInt(bet)
    check_chosen = checkInt(chosen)
    
    if (check_chosen and chosen == -1):
        if (check_bet):
            result = playRoulette(value, int(bet), int(chosen))
            gameResult(result)
        else:
            view.message_box.inputError()
    else:
        if (check_bet and check_chosen and (int(chosen) >= 1 and int(chosen) <= 36)):
            result = playRoulette(value, int(bet), int(chosen))
            gameResult(result)
        else:
            view.message_box.inputError()

def validateBlackjack(bet,app,current_user):
    check_bet = checkInt(bet)

    if (check_bet):
        result = playBlackjack(int(bet), app, current_user)
        #gameResult(result)
    else:
        view.message_box.inputError()

def closeWindow(app):
    app.destroy()

def rpsMainWindow(last_window, current_user):
    closeWindow(last_window)
    game_id = createRPS()
    game = getGame(game_id)
    app = Tk()
    app.title('RPS game @menu')

    Label(app, text='Welcome to RPS game').grid(row=0,column=0)
    Label(app, text='Choose your option:').grid(row=1,column=0)
    Label(app, text='1.Rock  2.Paper  3.Scissor').grid(row=2,column=0)
    Label(app, text='Enter your bet:').grid(row=3,column=0)

    player_chosen = Entry(app)
    player_bet = Entry(app)

    player_chosen.grid(row=2,column=1)
    player_bet.grid(row=3,column=1)

    Button(app, text='Play', command= lambda: validateRPS(player_chosen.get(), player_bet.get(), game, current_user)).grid(row=4,column=0)
    Button(app, text='Back',command=lambda: view.role_window.userMenuWindow(app,current_user)).grid(column=2,row=4)
    Button(app, text='Balance', command= lambda: getBalance(current_user)).grid(row=5,column=0)

    app.geometry('400x200')
    app.mainloop

def highLowMainWindow(last_window, current_user):
    closeWindow(last_window)
    app = Tk()
    app.title('High Low Game @menu')

    Label(app, text='Welcome to High Low Game').grid(row=0,column=0)
    Label(app, text='Number start from 1 to 12').grid(row=1,column=0)
    Label(app, text='High is from 7 to 12  Low is from 1 to 6').grid(row=2,column=0)
    Label(app, text='Guess the result:').grid(row=3,column=0)
    Label(app, text='Enter your bet:').grid(row=5,column=0) 

    player_bet = Entry(app)
    player_bet.grid(row=5,column=1)

    Button(app, text='High', command= lambda: validateHighLow(1,player_bet.get())).grid(row=4,column=0)
    Button(app, text='Low', command= lambda: validateHighLow(2, player_bet.get())).grid(row=4,column=1)
    Button(app, text='Back',command=lambda: view.role_window.userMenuWindow(app,current_user)).grid(row=6,column=0)


    app.geometry("400x200")
    app.mainloop

def rouletteMainWindow(last_window, current_user):
    closeWindow(last_window)

    app = Tk()
    app.title('Roulette game @menu')

    Label(app, text='Welcome to Roulette game').grid(row=0,column=0)
    Label(app, text='Option that you can bet:').grid(row=1,column=0)
    Label(app, text='Or enter number from 1-36').grid(row=4,column=0)
    Label(app, text='Enter your bet').grid(row=5,column=0)


    player_chosen = Entry(app)
    player_bet = Entry(app)

    player_chosen.grid(row=4,column=1)
    player_bet.grid(row=5,column=1)

    Button(app, text='1.Red', command= lambda: validateRoulette(1, player_bet.get(), -1)).grid(row=2,column=0)
    Button(app, text='2.Black', command= lambda: validateRoulette(2, player_bet.get(), -1)).grid(row=2,column=1)
    Button(app, text='3.Even', command= lambda: validateRoulette(3, player_bet.get(), -1)).grid(row=3,column=0)
    Button(app, text='4.Odd', command= lambda: validateRoulette(4, player_bet.get(), -1)).grid(row=3,column=1)
    Button(app, text='Play with number', command= lambda: validateRoulette(5, player_bet.get(), player_chosen.get())).grid(row=6,column=0)
    Button(app, text='Back',command=lambda: view.role_window.userMenuWindow(app,current_user)).grid(column=1,row=6)

    app.geometry('400x200')
    app.mainloop

def spinMainWindow(last_window, current_user):
    closeWindow(last_window)

    app = Tk()
    app.title('Spin game @menu')

    Label(app, text='Welcome to Spin game').grid(row=0,column=0)

    #Button(app, text='Play', command= lambda: validateRPS(player_chosen.get(), player_bet.get())).grid(row=4,column=0)
    Button(app, text='Back',command=lambda: view.role_window.userMenuWindow(app,current_user)).grid(column=2,row=4)

    app.geometry('400x200')
    app.mainloop

def slotMainWindow(last_window, current_user):
    closeWindow(last_window)

    app = Tk()
    app.title('Slot game @menu')

    Label(app, text='Welcome to Slot game').grid(row=0,column=0)

    #Button(app, text='Play', command= lambda: validateRPS(player_chosen.get(), player_bet.get())).grid(row=4,column=0)
    Button(app, text='Back',command=lambda: view.role_window.userMenuWindow(app,current_user)).grid(column=2,row=4)

    app.geometry('400x200')
    app.mainloop

def blackjackMainWindow(last_window, current_user):
    closeWindow(last_window)

    app = Tk()
    app.title('Blackjack game @menu')

    Label(app, text='Welcome to Blackjack game').grid(row=0,column=0)
    Label(app, text='Enter your bet').grid(row=1,column=0)
    
    player_bet = Entry(app)

    player_bet.grid(row=1,column=1)

    Button(app, text='Play', command= lambda: validateBlackjack(player_bet.get(), app, current_user)).grid(row=2,column=0)
    Button(app, text='Back',command=lambda: view.role_window.userMenuWindow(app,current_user)).grid(column=1,row=2)

    #Button(app, text='Back',command=lambda: userMenuWindow(app,current_user)).grid(column=2,row=4)

    app.geometry('400x200')
    app.mainloop