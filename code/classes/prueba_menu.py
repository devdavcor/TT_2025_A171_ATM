from tkinter import Tk, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import random
import os


# ---------- Funciones Auxiliares ----------

def try_login():
    username = server_app.user.get()  # Accede a la entrada de usuario desde el objeto 'server_app'
    passwd = server_app.password.get()  # Accede a la entrada de contraseña desde el objeto 'server_app'
    result = login_instance.start_login(username, passwd)

    if result:
        messagebox.showinfo("Login", f"Bienvenido, {result}!")
        open_menu_window()  # Llama a la función para abrir el siguiente menú
        login_window.destroy()  # Cierra la ventana de login
    else:
        messagebox.showerror("Login", "Usuario o contraseña incorrectos.")


def open_menu_window():
    # Cierra la ventana de login y crea una nueva ventana para el menú
    root = Tk()  # Nueva instancia de Tk() para el menú
    root.title("Menu")  # Asigna un título a la ventana
    root.geometry("1000x600")  # Establece un tamaño para la ventana

    # Obtener la ruta base desde el archivo actual
    base_path = os.path.dirname(os.path.abspath(__file__))

    # Generar una imagen aleatoria de fondo
    random_number = random.randint(1, 10)
    image_path = os.path.join(base_path, "graphics", "resources", f"f_sc_{random_number}.jpg")  # Usamos el número aleatorio

    try:
        image = Image.open(image_path)
        background_img = ImageTk.PhotoImage(image)

        # Crear un label para el fondo y asegurarse que ocupe toda la ventana
        background_label = tk.Label(root, image=background_img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Necesitamos mantener una referencia de la imagen
        root.background_img = background_img

    except FileNotFoundError:
        print(f"Error: La imagen {image_path} no existe.")

    # Agrega controles a la ventana de menú
    menu_label = tk.Label(root, text="Hola.", bg="#195959", fg="white", font=("Arial", 16))
    menu_label.place(relx=0.5, rely=0.5, anchor="center")

    root.mainloop()  # Mantener la ventana abierta


# ---------- Función para crear la ventana de login ----------

def create_login_window():
    # Instrucciones
    server_app.create_label(
        text="Please, enter your credentials below.",
        row=6,
        column=6,
        columnspan=8,
        rowspan=1,
        bg="#195959",
        fg="white",
        font=("Arial", 16)
    )

    # Espacio para usuario
    server_app.create_label(
        text="User:",
        row=9,
        column=7,
        columnspan=3,
        rowspan=1,
        bg="#195959",
        fg="white",
        font=("Arial", 16),
        anchor="w"
    )

    server_app.user = server_app.create_entry(row=9, column=9, columnspan=4)

    # Espacio para el password
    server_app.create_label(
        text="Password:",
        row=12,
        column=7,
        columnspan=3,
        rowspan=1,
        bg="#195959",
        fg="white",
        font=("Arial", 16),
        anchor="w"
    )

    server_app.password = server_app.create_entry(row=12, column=9, columnspan=4, show_text=False)

    # Espacio para el botón
    server_app.create_button(
        text="Login",
        command=try_login,  # Llama a la función try_login
        row=15,
        column=8,
        columnspan=4,
        rowspan=1,
        bg="#D9CFCC",
        fg="#0D2626",
        font=("Arial", 14)
    )


# ---------- Configuración de la DB ----------

def get_parquet_path():
    base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, "db", "usuarios.parquet")


parquet_path = get_parquet_path()
login_instance = Login(parquet_path)

if __name__ == "__main__":
    login_window = Tk()
    server_app = Window(login_window)

    # Crear la ventana de login
    create_login_window()

    # Mantener el ciclo principal abierto
    login_window.mainloop()
