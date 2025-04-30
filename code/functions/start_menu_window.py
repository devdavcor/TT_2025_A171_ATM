from tkinter import Tk, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import random
from code.classes.Window import Window
from code.classes.login_class import Login
import os

from code.functions.try_login import try_login
from code.functions.start_menu_window import start_menu_window

def start_menu_window():
    # Crear una nueva ventana Toplevel para el menú
    menu_window = tk.Toplevel(main_window)
    server_app_menu = Window(menu_window)
    server_app_menu.create_label(
        text="Start Server",
        row=6,
        column=6,
        columnspan=8,
        rowspan=1,
        bg="#195959",
        fg="white",
        font=("Arial", 16)
    )
    server_app_menu.create_button(
        text="Start Server",
        command=start_server,  # Llama a la función try_login
        row=12,
        column=8,
        columnspan=4,
        rowspan=2,
        bg="#D9CFCC",
        fg="#0D2626",
        font=("Arial", 14)
    )

    def close_window() :
        # Cierra la ventana actual sin afectar otras ventanas
        server_app_menu.root.destroy ()
        # 'server_app_menu.root' es la ventana donde se encuentra el botón "Back"

    # Creación del botón Back
    server_app_menu.create_button (
        text="Back",
        command=close_window,  # Llama a la función close_window para cerrar solo la ventana actual
        row=22,
        column=18,
        columnspan=1,
        rowspan=1,
        bg="#BFA980",  # Color del botón
        fg="#0D2626",
        font=("Arial", 14)
    )
