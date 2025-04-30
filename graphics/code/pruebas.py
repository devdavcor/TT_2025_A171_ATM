import tkinter
from tkinter import *

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
    v_1.withdraw()

# Ventana principal
v_main = Tk()
v_main.title("Corona Banking Central Server")
v_main.configure(bg="white")
centrar_ventana(v_main, 1000, 600)
v_main.resizable(True, True)

# Cambiar ícono
icono = PhotoImage(file="../resources/icon.png")
v_main.iconphoto(False, icono)

# Crear cuadrícula de celdas que ocupan toda la ventana
filas = 24
columnas = 20

for r in range(filas):
    v_main.grid_rowconfigure(r, weight=1)
    for c in range(columnas):
        v_main.grid_columnconfigure(c, weight=1)
        celda = Label(v_main, text=f"{r},{c}", bg="white", fg="black", relief="ridge", font=("Consolas", 8))
        celda.grid(row=r, column=c, sticky="nsew", padx=1, pady=1)

# Botones ubicados en una celda específica
#b_main = Button(v_main, text="Mostrar", command=show_window, bg="green", fg="white")
#b_main.grid(row=9, column=6, columnspan=3, sticky="nsew")

#b_main_1 = Button(v_main, text="Ocultar", command=hide_window, bg="red", fg="white")
#b_main_1.grid(row=9, column=11, columnspan=3, sticky="nsew")

#cuadro_texto = Entry(v_main, bg="white", fg="black", font=("Arial", 12))
#cuadro_texto.grid(row=5, column=5, columnspan=5, rowspan=1, sticky="nsew")


# Ventana emergente
v_1 = Toplevel()
v_1.withdraw()

v_main.mainloop()
