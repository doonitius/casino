from tkinter import *
from tkinter import ttk
import view.main_menu
import view.message_box
from controller.account_controller import accountGetBalance, checkBalance
from controller.game_controller import getGame, removeGameFromList
from game.rps import createRPS, playRPS
from game.highlow import createHighlow, playHighLow
from game.roulette import createRoulette, playRoulette
from game.blackjack import createBlackJack, playBlackjack
from view.blackjack import playWindow
from PIL import ImageTk, Image

def checkInt(value):
    try:
        int_player_chosen = int(value)
    except ValueError:
        # print("not a valid integer", value)
        return False
    else:
        # print("value is", int_player_chosen)
        return True

def backToMenu(app, current_user, game_id):
    removeGameFromList(game_id)
    view.main_menu.userMenuWindow(app, current_user)

def gameResult(result):
    if (result == 1): view.message_box.winGameMes()
    elif (result == 0): view.message_box.loseGameMes()
    else: view.message_box.drawGameMes()

def getBalance(current_user):
    print("current balance", accountGetBalance(current_user))

def validateRPS(chosen, bet, game, current_user):
    check_chosen = checkInt(chosen)
    check_bet = checkInt(bet)

    if (check_chosen and check_bet):
        if (int(chosen) < 1 or int(chosen) > 3):
            view.message_box.inputError()
        else:
            valid = checkBalance(bet, current_user)
            if (not valid):
                view.message_box.lowAmountError(accountGetBalance(current_user), bet)
            else:
                result = playRPS(game, current_user, int(chosen), int(bet))
                gameResult(result)
    else: 
        view.message_box.inputError()

def validateHighLow(value, bet, game, current_user):
    check_bet = checkInt(bet)

    if (check_bet):
        valid = checkBalance(bet, current_user)
        if (not valid):
            view.message_box.lowAmountError(accountGetBalance(current_user), bet)
        else:
            result = playHighLow(game, current_user, value, int(bet))
            gameResult(result)
    else:
        view.message_box.inputError()

def validateRoulette(value, bet, chosen, game, current_user):
    check_bet = checkInt(bet)
    check_chosen = checkInt(chosen)
    
    if (check_chosen and chosen == -1):
        if (check_bet):
            valid = checkBalance(bet, current_user)
            if (not valid):
                view.message_box.lowAmountError(accountGetBalance(current_user), bet)
            else:
                result = playRoulette(game, current_user, value, int(bet), int(chosen))
                gameResult(result)
        else:
            view.message_box.inputError()
    else:
        if (check_bet and check_chosen and (int(chosen) >= 1 and int(chosen) <= 36)):
            valid = checkBalance(bet, current_user)
            if (not valid):
                view.message_box.lowAmountError(accountGetBalance(current_user), bet)
            else:
                result = playRoulette(game, current_user, value, int(bet), int(chosen))
                gameResult(result)
        else:
            view.message_box.inputError()

def validateBlackjack(bet,app,current_user, game):
    check_bet = checkInt(bet)

    if (check_bet):
        valid = checkBalance(bet, current_user)
        if (not valid):
            view.message_box.lowAmountError(accountGetBalance(current_user), bet)
        else:
            playWindow(app, current_user, float(bet), game)
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
    tabControl = ttk.Notebook(app)

    tab_play = ttk.Frame(tabControl)
    tab_des = ttk.Frame(tabControl)

    tabControl.add(tab_play, text='Play')
    tabControl.add(tab_des, text='Description')
    tabControl.pack(expand=1, fill="both")
    

    ttk.Label(tab_play, text='Welcome to RPS game',foreground="#1A57FF",font=14).grid(column=0,row=0,pady=(10,30),columnspan = 2)
    ttk.Label(tab_play, text='Guess option:\n\nInput: 1, 2, 3\n(1) - Rock  \n(2) - Paper  \n(3) - Scissor').grid(row=1,column=0,pady=(0,20))
    ttk.Label(tab_play, text='Enter your guess:').grid(row=2,column=0,sticky = W,padx=(30,10),pady=(0,20))
    ttk.Label(tab_play, text='Enter your bet:').grid(row=4,column=0,sticky = W,padx=(30,10))

    player_chosen = Entry(tab_play)
    player_bet = Entry(tab_play)

    player_chosen.grid(row=2,column=1,pady=(0,20))
    player_bet.grid(row=4,column=1)

    Button(tab_play, text='Play',bg='#25AEF3',height=1, width=20, command= lambda: validateRPS(player_chosen.get(), player_bet.get(), game, current_user)).grid(row=5,column=1,pady=(20,20))
    Button(tab_play, text='Back', bg='black', fg='white', height=1, width=10, command=lambda: backToMenu(
        app, current_user, game_id)).grid(column=0, row=6,sticky = W,padx=(10,0))
    Button(tab_play, text='view balance',bg='white',height=1, width=10, command= lambda: getBalance(current_user)).grid(row=4,column=2,padx=(20,0))

    ttk.Label(tab_des, text='Description of RPS game').grid(row=0,column=0)
    ttk.Label(tab_des, text=game.getDesc()).grid(row=1,column=0)

    app.geometry('400x500')
    app.mainloop

def highLowMainWindow(last_window, current_user):
    closeWindow(last_window)
    game_id = createHighlow()
    game = getGame(game_id)
    app = Tk()
    app.title('High Low Game @menu')
    tabControl = ttk.Notebook(app)

    tab_play = ttk.Frame(tabControl)
    tab_des = ttk.Frame(tabControl)

    tabControl.add(tab_play, text='Play')
    tabControl.add(tab_des, text='Description')
    tabControl.pack(expand=1, fill="both")

    ttk.Label(tab_play, text='Welcome to High Low Game',foreground="#1A57FF",font=14).grid(column=0,row=0,pady=(10,30),columnspan = 2)
    
    ttk.Label(tab_play, text='Guess option:\n\nInput: number from 1 to 12\n(number 1-6) - guess result as Low\n(number 7-12) - guess result as High').grid(row=1,column=0,pady=(0,20),columnspan = 2)
    
    ttk.Label(tab_play, text='Enter your bet:').grid(row=3,column=0,sticky = W,padx=(30,10))

    player_bet = Entry(tab_play)
    player_bet.grid(row=3,column=1)

    Button(tab_play, text='view balance',bg='white',height=1, width=10, command= lambda: getBalance(current_user)).grid(row=3,column=2,padx=(20,0))


    Button(tab_play, text='High',bg='#25AEF3',height=1, width=10, command= lambda: validateHighLow(1,player_bet.get(), game, current_user)).grid(row=4,column=0,pady=(20,40),padx=(60,0))
    ttk.Label(tab_play, text='--- OR ---').grid(row=4,column=1,pady=(20,40))
    Button(tab_play, text='Low',bg='#25AEF3',height=1, width=10, command=lambda: validateHighLow(2, player_bet.get(), game, current_user)).grid(row=4, column=2,pady=(20,40),padx=(0,60))
    Button(tab_play, text='Back', bg='black', fg='white', height=1, width=10, command=lambda: backToMenu(
        app, current_user, game_id)).grid(row=5, column=0,padx=(10,0))

    ttk.Label(tab_des, text='Description of Highlow game').grid(row=0,column=0)
    ttk.Label(tab_des, text=game.getDesc()).grid(row=1,column=0)
    app.geometry('400x500')
    app.mainloop

def rouletteMainWindow(last_window, current_user):
    closeWindow(last_window)
    game_id = createRoulette()
    game = getGame(game_id)
    app = Tk()
    app.title('Roulette game @menu')
    tabControl = ttk.Notebook(app)

    tab_play = ttk.Frame(tabControl)
    tab_des = ttk.Frame(tabControl)

    tabControl.add(tab_play, text='Play')
    tabControl.add(tab_des, text='Description')
    tabControl.pack(expand=1, fill="both")

    ttk.Label(tab_play, text='Welcome to Roulette game',foreground="#1A57FF",font=14).grid(column=0,row=0,pady=(10,30),columnspan = 2)
    ttk.Label(tab_play, text='Guess option:\n\nSelect: Red or BLack\nSelect: Even or Odd\nInput: number 1-36\n\n(Red or Black) - guess result color\n(Even or Odd) - guess result number type\n(number 1-36) - guess result specific number').grid(row=1,column=0,pady=(0,20),columnspan = 2)

    ttk.Label(tab_play, text='Enter your bet:').grid(row=2,column=0,sticky = W,padx=(30,10),pady=(0,35))
    Button(tab_play, text='view balance',bg='white',height=1, width=10, command= lambda: getBalance(current_user)).grid(row=2,column=2,padx=(20,0),pady=(0,35))
    
    player_chosen = ttk.Entry(tab_play)
    player_bet = ttk.Entry(tab_play)

    player_chosen.grid(row=5,column=1,pady=(0,20))
    player_bet.grid(row=2,column=1,pady=(0,35))

    ttk.Label(tab_play, text='guess color:').grid(row=3,column=0,sticky = W,padx=(30,10),pady=(0,20))
    Button(tab_play, text='Red',bg='#FF2323',height=1, width=10, command= lambda: validateRoulette(1, player_bet.get(), -1, game, current_user)).grid(row=3,column=1,pady=(0,20))
    Button(tab_play, text='Black',bg='#000000',height=1, width=10,fg='white', command= lambda: validateRoulette(2, player_bet.get(), -1, game, current_user)).grid(row=3,column=2,pady=(0,20))
    
    ttk.Label(tab_play, text='guess number type:').grid(row=4,column=0,sticky = W,padx=(30,10),pady=(0,20))
    Button(tab_play, text='Even',bg='#BBBBBB',height=1, width=10, command= lambda: validateRoulette(3, player_bet.get(), -1, game, current_user)).grid(row=4,column=1,pady=(0,20))
    Button(tab_play, text='Odd',bg='#BBBBBB',height=1, width=10, command= lambda: validateRoulette(4, player_bet.get(), -1, game, current_user)).grid(row=4,column=2,pady=(0,20))
    
    ttk.Label(tab_play, text='guess specific number:').grid(row=5,column=0,sticky = W,padx=(30,10),pady=(0,20))
    Button(tab_play, text='Play',bg='#25AEF3',height=1, width=10, command= lambda: validateRoulette(5, player_bet.get(), player_chosen.get(), game, current_user)).grid(row=5,column=2,pady=(0,20))
    
    Button(tab_play, text='Back', bg='black', fg='white', height=1, width=10, command=lambda: backToMenu(
        app, current_user, game_id)).grid(row=6, column=0,padx=(10,0),pady=(20,0))

    ttk.Label(tab_des, text='Description of Roulette game').grid(row=0,column=0)
    ttk.Label(tab_des, text=game.getDesc()).grid(row=1,column=0)

    app.geometry('400x500')
    app.mainloop

def blackjackMainWindow(last_window, current_user):
    closeWindow(last_window)
    game_id = createBlackJack()
    game = getGame(game_id)
    app = Tk()
    app.title('Blackjack game @menu')
    tabControl = ttk.Notebook(app)

    tab_play = ttk.Frame(tabControl)
    tab_des = ttk.Frame(tabControl)

    tabControl.add(tab_play, text='Play')
    tabControl.add(tab_des, text='Description')
    tabControl.pack(expand=1, fill="both")

    ttk.Label(tab_play, text='Welcome to Blackjack game',foreground="#1A57FF",font=14).grid(column=0,row=0,pady=(10,30),columnspan = 2)
    ttk.Label(tab_play, text='Guess option:\n\nSelect: Hit and Stay\n\n(Hit) - ask for more card\n(Stay) - stand with cards in hand').grid(row=1,column=0,pady=(0,20),columnspan = 2)
    ttk.Label(tab_play, text='Enter your bet:').grid(row=2,column=0,sticky = W,padx=(30,10),pady=(0,35))
    Button(tab_play, text='view balance',bg='white',height=1, width=10, command= lambda: getBalance(current_user)).grid(row=2,column=2,padx=(20,0),pady=(0,35))
    
    player_bet = ttk.Entry(tab_play)

    player_bet.grid(row=2,column=1,pady=(0,35))

    Button(tab_play, text='Play',bg='#25AEF3',height=1, width=20, command= lambda: validateBlackjack(player_bet.get(), app, current_user, game)).grid(row=3,column=1)
    # Button(tab_play, text='Back', command=lambda: backToMenu(
    #     app, current_user, game_id)).grid(column=1, row=2)

    Button(tab_play, text='Back', bg='black', fg='white', height=1, width=10, command=lambda: backToMenu(
        app, current_user, game_id)).grid(row=4, column=0,padx=(10,0),pady=(20,0))

    app.geometry('400x500')
    app.mainloop