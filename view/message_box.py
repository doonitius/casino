from tkinter import *
from tkinter import messagebox
from controller.account_controller import accountGetBalance
import view.game_window

def loginError():
    messagebox.showerror('Login Error', 'Invalid username or password')

def balanceMes(current_user):
    balance = accountGetBalance(current_user)
    messagebox.showinfo('Balance', 'Your balance: '+str(balance))


def inputError():
    messagebox.showerror('Input Error', 'Invalid type')

def winGameMes():
    messagebox.showinfo('Result', 'Congratulations you win')

def loseGameMes():
    messagebox.showinfo('Result', 'Unlucky you lose')

def drawGameMes():
    messagebox.showinfo('Result', 'It a tie')
