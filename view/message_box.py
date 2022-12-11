from tkinter import *
from tkinter import messagebox
from view.role_window import selectRole

def loginError():
    messagebox.showerror('Login Error', 'Invalid username or password')

def loginSuccess(app, current_user):
    selectRole(app,current_user)
