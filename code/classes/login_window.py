import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
from login_class import *
import random

# === Funciones ===
def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def authentication():
    base_path = os.path.dirname(__file__)
    parquet_path = os.path.abspath(os.path.join(base_path, "..", "..", "db", "usuarios.parquet"))
    login_system = Login(parquet_path)
    a = inputText1.get()
    b = inputText2.get()

    # === Cerrar cualquier ventana previa con el mismo título ===
    for widget in tk._default_root.winfo_children():
        if isinstance(widget, Toplevel) and widget.title() == "Login message":
            widget.destroy()

    # === Ventana emergente ===
    v_1 = Toplevel()
    v_1.withdraw()
    v_1.title("Login message")
    v_1.geometry("250x150")
    centrar_ventana(v_1, 250, 150)
    v_1.resizable(False, False)

    random_number_v_1 = random.randint(1, 10)
    background_path_random_number_v_1 = os.path.abspath(
        os.path.join(base_path, "..", "..", "graphics", "resources", f"f_sc_{random_number_v_1}.jpg"))
    background_image_v1 = Image.open(background_path_random_number_v_1)
    background_photo_v1 = ImageTk.PhotoImage(background_image_v1)
    background_label_v1 = tk.Label(v_1, image=background_photo_v1)
    background_label_v1.image = background_photo_v1  # <--- línea clave
    background_label_v1.place(x=0, y=0, relwidth=1, relheight=1)

    if not a or not b:
        label_hello = Label(v_1, text="Please fill both fields!", bg="#195959", fg="white", font=("Arial", 10))
        label_hello.place(relx=0.5, rely=0.5, anchor="center")
        v_1.deiconify()
        return  # Puedes salir aquí para no intentar login con campos vacíos

    auth_aux = login_system.start_login(a, b)

    if auth_aux != False:
        message = 'Login Success!'
    else:
        message = 'Login Failed!'

    label_hello = Label(v_1, text=message, bg="#195959", fg="white", font=("Arial", 10))
    label_hello.place(relx=0.5, rely=0.5, anchor="center")
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

# === Background and Icon ===

# Get the base path of the current file
base_path = os.path.dirname(__file__)

# Construct the absolute path to the background image
random_number = random.randint(1, 10)
background_path = os.path.abspath(os.path.join(base_path, "..", "..", "graphics", "resources", f"f_sc_{random_number}.jpg"))

# Load the background image and convert it to a Tkinter-compatible format
background_image = Image.open(background_path)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to display the background image
background_label = tk.Label(v_main, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


icon_path = os.path.abspath(os.path.join(base_path, "..", "..", "graphics", "resources", "icon.png"))

# Load and set the window icon
icon = PhotoImage(file=icon_path)
v_main.iconphoto(False, icon)

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

entry2 = Entry(v_main, textvariable=inputText2, width=18, show="*")
entry2.grid(row=13, column=10, columnspan=3, rowspan=1, sticky="nsew")


# === Botones ===
b_main = Button(
    v_main, text="Ingresar", command=authentication,
    bg="#BFA980", fg="white", font=("Arial", 14)
)
b_main.grid(row=18, column=6, columnspan=3, rowspan=1, sticky="nsew")

b_main_1 = Button(
    v_main, text="Cerrar", command=hide_window,
    bg="#D9CFCC", fg="Black", font=("Arial", 14)
)
b_main_1.grid(row=18, column=11, columnspan=3, rowspan=1, sticky="nsew")

# === Ventana emergente ===
# === Loop principal ===
v_main.mainloop()
