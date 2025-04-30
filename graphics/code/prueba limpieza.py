import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk

# === Funciones ===
def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def show_window():
    v_1.deiconify()

def hide_window():
    v_1.deiconify()
    v_1.withdraw()

# === Ventana principal ===
v_main = Tk()
v_main.title("Corona Banking Central Server")
v_main.configure(bg="black")
centrar_ventana(v_main, 1000, 600)
v_main.resizable(False, False)

# === Fondo e ícono ===
base_path = os.path.dirname(__file__)
ruta_imagen = os.path.join(base_path, "..", "resources", "f_sc_6.jpg")
fondo = Image.open(ruta_imagen)
imagen_fondo = ImageTk.PhotoImage(fondo)

label_fondo = tk.Label(v_main, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

icono = PhotoImage(file="../resources/icon.png")
v_main.iconphoto(False, icono)

# === Configuración de la cuadrícula ===
filas = 24
columnas = 20
for r in range(filas):
    v_main.grid_rowconfigure(r, weight=1)
for c in range(columnas):
    v_main.grid_columnconfigure(c, weight=1)

# === Etiquetas de texto ===
label_main = Label(
    v_main, text="Corona Banking Central Server",
    bg="#195959", fg="white", font=("Arial", 18, "bold")
)
label_main.grid(row=3, column=6, columnspan=8, rowspan=1, sticky="nsew")

label_a = Label(
    v_main, text="Please, enter your credentials below",
    bg="#195959", fg="white", font=("Arial", 16)
)
label_a.grid(row=7, column=8, columnspan=4, rowspan=1, sticky="nsew")

label_1 = Label(
    v_main, text="User: ",
    bg="#195959", fg="white", font=("Arial", 14)
)
label_1.grid(row=10, column=7, columnspan=3, rowspan=1, sticky="nsew")

label_2 = Label(
    v_main, text="Password: ",
    bg="#195959", fg="white", font=("Arial", 14)
)
label_2.grid(row=13, column=7, columnspan=3, rowspan=1, sticky="nsew")

# === Entradas de texto ===
inputText1 = StringVar()
inputText2 = StringVar()

entry1 = Entry(v_main, textvariable=inputText1, width=18)
entry1.grid(row=10, column=10, columnspan=3, rowspan=1, sticky="nsew")

entry2 = Entry(v_main, textvariable=inputText2, width=18)
entry2.grid(row=13, column=10, columnspan=3, rowspan=1, sticky="nsew")

# === Botones ===
b_main = Button(
    v_main, text="Ingresar", command=show_window,
    bg="#667371", fg="white", font=("Arial", 14)
)
b_main.grid(row=18, column=6, columnspan=3, rowspan=1, sticky="nsew")

b_main_1 = Button(
    v_main, text="Cerrar", command=hide_window,
    bg="#667371", fg="white", font=("Arial", 14)
)
b_main_1.grid(row=18, column=11, columnspan=3, rowspan=1, sticky="nsew")

# === Ventana emergente ===
v_1 = Toplevel()
v_1.withdraw()

# === Loop principal ===
v_main.mainloop()
