import tkinter
from tkinter import *
import os
import sys



#funciones

def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()  # Actualiza antes de posicionar
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")


def show_window():
    v_1.deiconify()

def hide_window():
    v_1.withdraw()

#Ventana principal
v_main = tkinter.Tk()
v_main.title("Corona Banking Central Server")
v_main.configure(bg="black")
centrar_ventana(v_main, 1000, 600)
v_main.resizable(False, False)

# Cambiar ícono
icono = PhotoImage(file="../resources/icon.png")
  # Asegúrate de tener este archivo en la misma carpeta
v_main.iconphoto(False, icono)

#Ventana emergente
v_1 = tkinter.Toplevel()
v_1.withdraw()

#Botones
b_main = tkinter.Button(v_main, text="Mostrar", command=show_window)
#b_main.pack()
b_main.place(x=50, y=100)

b_main_1 = tkinter.Button(v_main, text="Ocultar", command=hide_window )
b_main_1.pack()

v_main.mainloop()





