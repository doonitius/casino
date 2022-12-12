from tkinter import *
from tkinter import messagebox
from view.role_window import selectRole

def loginError():
    messagebox.showerror('Login Error', 'Invalid username or password')

def loginSuccess(app, current_user):
    selectRole(app,current_user)

def inputError():
    messagebox.showerror('Input Error', 'Invalid type')

def winGameMes():
    messagebox.showinfo('Result', 'Congratulations you win')

def loseGameMes():
    messagebox.showinfo('Result', 'Unlucky you lose')

def drawGameMes():
    messagebox.showinfo('Result', 'It a tie')
