from tkinter import Tk, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import random
from code.classes.Window import Window
from code.classes.login_class import Login
import os

def try_login():
    username = server_app.user.get()  # Accede a la entrada de usuario desde el objeto 'server_app'
    passwd = server_app.password.get()  # Accede a la entrada de contraseña desde el objeto 'server_app'
    result = login_instance.start_login(username, passwd)

    if result:
        messagebox.showinfo("Login", f"Welcome, {result}!")
        main_window.withdraw ()
        open_menu_window()  # Llama a la función para abrir el siguiente menú
    else:
        messagebox.showerror("Login", "User or password incorrect.")