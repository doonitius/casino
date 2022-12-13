from tkinter import *
from tkinter import ttk
import view.main_menu 
import view.game_window
from game.blackjack import playBlackjack, checkResult
from controller.game_controller import removeGameFromList

def reWindow(last_window, current_user, player, dealer, action, bet, game):
    view.main_menu.closeWindow(last_window)

    player_hand, dealer_hand, result = checkResult(game, current_user, action)
    player_value = sum(player_hand)
    dealer_value = sum(dealer_hand)

    app = Tk()
    app.title('Play blackjack')

    Label(app, text='Blackjack Play Phase',foreground="#1A57FF",font=14).grid(column=0,row=0,pady=(10,30),columnspan = 2)
    Label(app, text='Player hand:',foreground="#FF6600").grid(row=1,column=0,pady=(0,10),columnspan = 2,padx=(20,0),sticky = W)
    Label(app, text='Card 1: '+str(player_hand[0])).grid(row=2, column=0,padx=(30,10),sticky = W)
    Label(app, text='Card 2: '+str(player_hand[1])).grid(row=2, column=1,padx=(30,10),sticky = W)
    Label(app, text='Card 3: '+str(player_hand[2])).grid(row=2,column=2,padx=(30,10),sticky = W)
    Label(app, text='Dealer hand:',foreground="#FF6600").grid(row=3,column=0,pady=(20,10),columnspan = 2,padx=(20,0),sticky = W)
    Label(app, text='Card 1: '+str(dealer_hand[0])).grid(row=4, column=0,padx=(30,10),sticky = W)
    Label(app, text='Card 2: '+str(dealer_hand[1])).grid(row=4, column=1,padx=(30,10),sticky = W)
    Label(app, text='Card 3: '+str(dealer_hand[2])).grid(row=4,column=2,padx=(30,10),sticky = W)
    Label(app, text='Player point: '+str(player_value)).grid(row=5,column=0,pady=(30,10),columnspan = 2)
    Label(app, text='Dealer point: '+str(dealer_value)).grid(row=6,column=0,columnspan = 2)
    if (result == 1):
        #winGame(bet) 
        Label(app, text='Congratulations you win!',foreground="green",font=14).grid(row=7,column=0,pady=(30,10),columnspan = 2,sticky = W,padx=(30,0))

    elif (result == 0): 
        #loseGame(bet)
        Label(app, text='Nice try kid',foreground="#FF0000",font=14).grid(row=7,column=0,pady=(30,10),columnspan = 2,sticky = W,padx=(30,0))

    else: 
        #tieGame(bet)
        Label(app, text='It is a tie!',foreground="#1A57FF",font=14).grid(row=7,column=0,pady=(30,10),columnspan = 2,sticky = W,padx=(30,0))

    removeGameFromList(game.getGameId())
    Button(app, text='Back', bg='black', fg='white', height=1, width=10,command=lambda: view.game_window.blackjackMainWindow(app,current_user)).grid(row=8,column=0,padx=(10,0),pady=(20,0))

    app.geometry('400x500')
    app.mainloop

def playWindow(last_window, current_user, bet, game):
    view.main_menu.closeWindow(last_window)

    game = playBlackjack(game, current_user, bet)
    
    player_hand, dealer_hand = game.play()

    app = Tk()
    app.title('Play blackjack')


    Label(app, text='Blackjack Play Phase',foreground="#1A57FF",font=14).grid(column=0,row=0,pady=(10,30),columnspan = 2)
    Label(app, text='Player hand:',foreground="#FF6600").grid(row=1,column=0,pady=(0,10),columnspan = 2,padx=(20,0),sticky = W)
    Label(app, text='Card 1: '+str(player_hand[0])).grid(row=2, column=0,padx=(30,10),sticky = W)
    Label(app, text='Card 2: '+str(player_hand[1])).grid(row=2, column=1,padx=(30,10),sticky = W)
    Label(app, text='Card 3: -').grid(row=2,column=2,padx=(30,10),sticky = W)
    Label(app, text='Dealer hand:',foreground="#FF6600").grid(row=3,column=0,pady=(20,10),columnspan = 2,padx=(20,00),sticky = W)
    Label(app, text='Card 1: ??').grid(row=4, column=0,padx=(30,10),sticky = W)
    Label(app, text='Card 2: ??').grid(row=4, column=1,padx=(30,10),sticky = W)
    Label(app, text='Card 3: ??').grid(row=4,column=2,padx=(30,10),sticky = W)

    Label(app, text='Player current point: '+ str( int(player_hand[0]) + int(player_hand[1]) )).grid(row=5,column=0,pady=(30,10),columnspan = 2)

    Button(app, text='Hit',bg='#25AEF3',height=1, width=10,command=lambda: reWindow(app, current_user, player_hand, dealer_hand,1, bet, game)).grid(row=6,column=0,pady=(20,20),columnspan = 2,padx=(0,40))
    Button(app, text='Stay',bg='#25AEF3',height=1, width=10,command=lambda: reWindow(app, current_user, player_hand, dealer_hand,2, bet, game)).grid(row=6,column=1,pady=(20,20),columnspan = 2)

    Button(app, text='Back', bg='black', fg='white', height=1, width=10,command=lambda: view.game_window.blackjackMainWindow(app,current_user)).grid(row=7,column=0,padx=(10,0),pady=(20,0))

    app.geometry('400x500')
    app.mainloop


