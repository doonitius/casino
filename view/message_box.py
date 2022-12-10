from tkinter import *
from tkinter import messagebox
from view.role_window import select_role

def login_error():
    messagebox.showerror('Login Error', 'Invalid username or password')

def login_success(app):
    select_role(app)
