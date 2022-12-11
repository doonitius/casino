from tkinter import *
from tkinter import ttk
from model.game import Game  # test
#from view.role_window import userMenuWindow
import view.message_box
from game.rps import playRPS

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

def gameResult(result):
    if (result == 1): view.message_box.winGameMes()
    elif (result == 0): view.message_box.loseGameMes()
    else: view.message_box.drawGameMes()

# put in controller
def validateRPS(chosen, bet):
    check_chosen = checkInt(chosen)
    check_bet = checkInt(bet)

    if (check_chosen and check_bet):
        result = playRPS(int(chosen), int(bet))
        gameResult(result)
    else: 
        view.message_box.inputRPSError()
    
# Test db
def create_db_for_rps(): 
    rps_game = Game('g001', 'rps', 'Rock paper Sissor', 100)
    return rps_game

def closeWindow(app):
    app.destroy()

def rps_main_window(last_window, current_user):
    closeWindow(last_window)

    game_info = create_db_for_rps()

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

    #validateInt should be in controller
    Button(app, text='Play', command= lambda: validateRPS(player_chosen.get(), player_bet.get())).grid(row=4,column=0)
    #Button(app, text='Back',command=lambda: userMenuWindow(app,current_user)).grid(column=2,row=4)

    app.geometry('400x200')
    app.mainloop