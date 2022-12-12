from tkinter import *
from tkinter import ttk
import view.role_window # Should not be in role_window
import view.game_window
import game.game

def playWindow(last_window, current_user):
    view.role_window.closeWindow(last_window)

    player_hand, dealer_hand = game.game.beginGame()

    app = Tk()
    app.title('Play blackjack')

    player_card3 = StringVar()
    dealer_card3 = StringVar()
    player_card3.set("Card3-")
    dealer_card3.set("-")

    Label(app, text='Blackjack').grid(row=0,column=0)
    Label(app, text='Player hand:').grid(row=1,column=0)
    Label(app, text='Card1: '+str(player_hand[0])).grid(row=1, column=1)
    Label(app, text='Card2: '+str(player_hand[1])).grid(row=1, column=2)
    Label(app, textvariable=player_card3).grid(row=1,column=3)
    Label(app, text='Dealer hand:').grid(row=2,column=0)
    Label(app, text='Card1: '+str(dealer_hand[0])).grid(row=2, column=1)
    Label(app, text='Card2: '+str(dealer_hand[1])).grid(row=2, column=2)
    Label(app, textvariable=dealer_card3).grid(row=2,column=3)

    Button(app, text='Back',command=lambda: view.game_window.blackjackMainWindow(app,current_user)).grid(row=5,column=2)

    app.geometry('400x200')
    app.mainloop