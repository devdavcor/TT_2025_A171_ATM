import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os
import random
from .login_class import Login


class LoginWindow :
    def __init__(self, master) :
        self.master = master
        self.master.title ( "Corona Banking Central Server" )
        self.master.configure ( bg="black" )
        self.centrar_ventana ( self.master, 1000, 600 )
        self.master.resizable ( False, False )

        # Background image
        self.set_background ()

        # Configuración de la cuadrícula
        self.configurar_grid ()

        # Agregar widgets a la ventana principal
        self.create_widgets ()

    def centrar_ventana(self, ventana, ancho, alto) :
        ventana.update_idletasks ()
        pantalla_ancho = ventana.winfo_screenwidth ()
        pantalla_alto = ventana.winfo_screenheight ()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        ventana.geometry ( f"{ancho}x{alto}+{x}+{y}" )

    def set_background(self) :
        base_path = os.path.dirname ( __file__ )
        random_number = random.randint ( 1, 10 )
        background_path = os.path.abspath (
            os.path.join ( base_path, "..", "..", "graphics", "resources", f"f_sc_{random_number}.jpg" )
        )

        background_image = Image.open ( background_path )
        background_photo = ImageTk.PhotoImage ( background_image )

        background_label = tk.Label ( self.master, image=background_photo )
        background_label.place ( x=0, y=0, relwidth=1, relheight=1 )
        background_label.image = background_photo  # Necesario para mantener la referencia

        # Icono
        icon_path = os.path.abspath ( os.path.join ( base_path, "..", "..", "graphics", "resources", "icon.png" ) )
        icon = PhotoImage ( file=icon_path )
        self.master.iconphoto ( False, icon )

    def configurar_grid(self) :
        filas = 24
        columnas = 20
        for r in range ( filas ) :
            self.master.grid_rowconfigure ( r, weight=1 )
        for c in range ( columnas ) :
            self.master.grid_columnconfigure ( c, weight=1 )

    def create_widgets(self) :
        label_main = Label (
            self.master, text="Corona Banking Central Server",
            bg="#195959", fg="white", font=("Arial", 18, "bold")
        )
        label_main.grid ( row=3, column=6, columnspan=8, rowspan=1, sticky="nsew" )

        label_a = Label (
            self.master, text="Please, enter your credentials below",
            bg="#195959", fg="white", font=("Arial", 16)
        )
        label_a.grid ( row=7, column=8, columnspan=4, rowspan=1, sticky="nsew" )

        label_1 = Label (
            self.master, text="User: ",
            bg="#195959", fg="white", font=("Arial", 14)
        )
        label_1.grid ( row=10, column=7, columnspan=3, rowspan=1, sticky="nsew" )

        label_2 = Label (
            self.master, text="Password: ",
            bg="#195959", fg="white", font=("Arial", 14)
        )
        label_2.grid ( row=13, column=7, columnspan=3, rowspan=1, sticky="nsew" )

        # Entradas de texto
        self.inputText1 = StringVar ()
        self.inputText2 = StringVar ()

        self.entry1 = Entry ( self.master, textvariable=self.inputText1, width=18 )
        self.entry1.grid ( row=10, column=10, columnspan=3, rowspan=1, sticky="nsew" )

        self.entry2 = Entry ( self.master, textvariable=self.inputText2, width=18, show="*" )
        self.entry2.grid ( row=13, column=10, columnspan=3, rowspan=1, sticky="nsew" )

        # Botones
        b_main = Button (
            self.master, text="Ingresar", command=self.authentication,
            bg="#667371", fg="white", font=("Arial", 14)
        )
        b_main.grid ( row=18, column=6, columnspan=3, rowspan=1, sticky="nsew" )

        b_main_1 = Button (
            self.master, text="Cerrar", command=self.hide_window,
            bg="#667371", fg="white", font=("Arial", 14)
        )
        b_main_1.grid ( row=18, column=11, columnspan=3, rowspan=1, sticky="nsew" )

    def authentication(self) :
        base_path = os.path.dirname ( __file__ )
        parquet_path = os.path.abspath ( os.path.join ( base_path, "..", "..", "db", "usuarios.parquet" ) )
        login_system = Login ( parquet_path )
        a = self.inputText1.get ()
        b = self.inputText2.get ()

        # Cerrar cualquier ventana previa con el mismo título
        for widget in tk._default_root.winfo_children () :
            if isinstance ( widget, Toplevel ) and widget.title () == "Login message" :
                widget.destroy ()

        # Ventana emergente
        v_1 = Toplevel ( self.master )
        v_1.withdraw ()
        v_1.title ( "Login message" )
        v_1.geometry ( "250x150" )
        self.centrar_ventana ( v_1, 250, 150 )
        v_1.resizable ( False, False )

        random_number_v_1 = random.randint ( 1, 10 )
        background_path_random_number_v_1 = os.path.abspath (
            os.path.join ( base_path, "..", "..", "graphics", "resources", f"f_sc_{random_number_v_1}.jpg" ) )
        background_image_v1 = Image.open ( background_path_random_number_v_1 )
        background_photo_v1 = ImageTk.PhotoImage ( background_image_v1 )
        background_label_v1 = tk.Label ( v_1, image=background_photo_v1 )
        background_label_v1.image = background_photo_v1  # Necesario para mantener la referencia
        background_label_v1.place ( x=0, y=0, relwidth=1, relheight=1 )

        if not a or not b :
            label_hello = Label ( v_1, text="Please fill both fields!", bg="#195959", fg="white", font=("Arial", 10) )
            label_hello.place ( relx=0.5, rely=0.5, anchor="center" )
            v_1.deiconify ()
            return  # Salir si los campos están vacíos

        auth_aux = login_system.start_login ( a, b )

        if auth_aux != False :
            message = 'Login Success!'
        else :
            message = 'Login Failed!'

        label_hello = Label ( v_1, text=message, bg="#195959", fg="white", font=("Arial", 10) )
        label_hello.place ( relx=0.5, rely=0.5, anchor="center" )
        v_1.deiconify ()

    def hide_window(self) :
        self.master.withdraw ()


# Ventana principal
if __name__ == "__main__" :
    root = Tk ()
    login_window = LoginWindow ( root )
    root.mainloop ()
