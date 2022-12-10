from tkinter import *
from tkinter import messagebox

def login_error():
    messagebox.showerror('Login Error', 'Invalid username or password')

def login_success():
    messagebox.showinfo('Login Success', 'Welcome to Jade Noi 888')
