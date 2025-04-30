import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
import string

# Función para generar contraseñas aleatorias (en caso de querer una predeterminada)
def generar_contraseña(longitud=10):
    """Genera una contraseña aleatoria de 10 caracteres."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for i in range(longitud))

# Función para dar de alta un usuario
def dar_de_alta_usuario():
    """Agrega un nuevo usuario y contraseña al archivo Parquet."""
    # Obtener los valores del formulario
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    # Validación: Verificar que los campos no estén vacíos
    if not usuario or not contrasena:
        messagebox.showerror("Error", "Por favor, ingresa un usuario y una contraseña.")
        return

    # Cargar el archivo Parquet existente
    try:
        df = pd.read_parquet("users_prueba.parquet")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["user", "password"])

    # Verificar si el usuario ya existe
    if usuario in df["user"].values:
        messagebox.showerror("Error", "El usuario ya existe.")
        return

    # Agregar el nuevo usuario al DataFrame usando pd.concat
    nuevo_usuario = pd.DataFrame({"user": [usuario], "password": [contrasena]})
    df = pd.concat([df, nuevo_usuario], ignore_index=True)

    # Guardar los cambios en el archivo Parquet
    df.to_parquet("users_prueba.parquet", index=False)

    # Mostrar mensaje de éxito
    messagebox.showinfo("Éxito", "Usuario creado exitosamente.")

# Crear la ventana principal
root = tk.Tk()
root.title("Dar de Alta un Usuario")
root.geometry("400x300")
root.resizable(False, False)

# Etiqueta y campo de entrada para el usuario
label_usuario = tk.Label(root, text="Usuario:")
label_usuario.pack(pady=10)
entry_usuario = tk.Entry(root, width=30)
entry_usuario.pack(pady=5)

# Etiqueta y campo de entrada para la contraseña
label_contrasena = tk.Label(root, text="Contraseña:")
label_contrasena.pack(pady=10)
entry_contrasena = tk.Entry(root, width=30, show="*")  # show="*" oculta la contraseña
entry_contrasena.pack(pady=5)

# Botón para dar de alta al usuario
boton_alta = tk.Button(root, text="Dar de Alta", command=dar_de_alta_usuario)
boton_alta.pack(pady=20)

# Ejecutar la ventana
root.mainloop()
