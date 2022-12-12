from tkinter import *
from tkinter import ttk
import view.role_window # Should not be in role_window
import view.game_window
import game.game
from game.blackjack import playBlackjack, checkResult

def reWindow(last_window, current_user, player, dealer, action, bet, game):
    view.role_window.closeWindow(last_window)

    player_hand, dealer_hand, result = checkResult(game, current_user, action)
    player_value = sum(player_hand)
    dealer_value = sum(dealer_hand)

    app = Tk()
    app.title('Play blackjack')

    Label(app, text='Blackjack').grid(row=0,column=0)
    Label(app, text='Player hand:').grid(row=1,column=0)
    Label(app, text='Card1: '+str(player_hand[0])).grid(row=1, column=1)
    Label(app, text='Card2: '+str(player_hand[1])).grid(row=1, column=2)
    Label(app, text='Card3: '+str(player_hand[2])).grid(row=1,column=3)
    Label(app, text='Dealer hand:').grid(row=2,column=0)
    Label(app, text='Card1: '+str(dealer_hand[0])).grid(row=2, column=1)
    Label(app, text='Card2: '+str(dealer_hand[1])).grid(row=2, column=2)
    Label(app, text='Card3: '+str(dealer_hand[2])).grid(row=2,column=3)
    Label(app, text='Player get: '+str(player_value)).grid(row=3,column=0)
    Label(app, text='Dealer get: '+str(dealer_value)).grid(row=3,column=1)
    if (result == 1):
        #winGame(bet) 
        Label(app, text='Congratulations you win!').grid(row=4,column=0)
    elif (result == 0): 
        #loseGame(bet)
        Label(app, text='Nice try kid').grid(row=4,column=0)
    else: 
        #tieGame(bet)
        Label(app, text='It a tie!').grid(row=4,column=0)

    Button(app, text='Back',command=lambda: view.game_window.blackjackMainWindow(app,current_user)).grid(row=5,column=2)

    app.geometry('400x200')
    app.mainloop

def playWindow(last_window, current_user, bet, game):
    view.role_window.closeWindow(last_window)

    game = playBlackjack(game, current_user, bet)
    
    player_hand, dealer_hand = game.play()

    app = Tk()
    app.title('Play blackjack')

    Label(app, text='Blackjack').grid(row=0,column=0)
    Label(app, text='Player hand:').grid(row=1,column=0)
    Label(app, text='Card1: '+str(player_hand[0])).grid(row=1, column=1)
    Label(app, text='Card2: '+str(player_hand[1])).grid(row=1, column=2)
    Label(app, text='Card3: -').grid(row=1,column=3)
    Label(app, text='Dealer hand:').grid(row=2,column=0)
    Label(app, text='Card1: *').grid(row=2, column=1)
    Label(app, text='Card2: *').grid(row=2, column=2)
    Label(app, text='Card3: -').grid(row=2,column=3)

    Button(app, text='Hit',command=lambda: reWindow(app, current_user, player_hand, dealer_hand,1, bet, game)).grid(row=3,column=0)
    Button(app, text='Stay',command=lambda: reWindow(app, current_user, player_hand, dealer_hand,2, bet, game)).grid(row=3,column=1)
    # Button(app, text='Hit',command=lambda: game.game.checkDealer(1, player_hand, dealer_hand)).grid(row=3,column=0)
    # Button(app, text='Stay',command=lambda: game.game.checkDealer(2, player_hand, dealer_hand)).grid(row=3,column=1)
    Button(app, text='Back',command=lambda: view.game_window.blackjackMainWindow(app,current_user)).grid(row=5,column=2)

    app.geometry('400x200')
    app.mainloop


