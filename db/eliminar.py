import tkinter as tk
from tkinter import messagebox
import pandas as pd


# Función para eliminar un usuario del archivo Parquet
def eliminar_usuario() :
    # Obtener el nombre de usuario ingresado
    username = entry.get ()

    # Leer el archivo Parquet
    df = pd.read_parquet ( 'users_prueba.parquet' )

    # Comprobar si el usuario existe en el DataFrame
    if username in df['user'].values :
        # Eliminar al usuario
        df = df[df['user'] != username]

        # Guardar los cambios de nuevo en el archivo Parquet
        df.to_parquet ( 'users_prueba.parquet', engine='pyarrow' )

        # Mostrar un mensaje de éxito
        messagebox.showinfo ( "Éxito", f"El usuario {username} ha sido eliminado." )
    else :
        # Mostrar mensaje si el usuario no existe
        messagebox.showerror ( "Error", f"El usuario {username} no existe en la base de datos." )


# Crear la ventana principal
root = tk.Tk ()
root.title ( "Eliminar Usuario" )
root.geometry ( "400x200" )  # Tamaño de la ventana
root.resizable ( False, False )  # No reescalable

# Etiqueta para el nombre de usuario
label = tk.Label ( root, text="Ingrese el nombre de usuario a eliminar:" )
label.pack ( pady=10 )

# Campo de entrada para el nombre de usuario
entry = tk.Entry ( root, width=30 )
entry.pack ( pady=10 )

# Botón para eliminar el usuario
eliminar_button = tk.Button ( root, text="Eliminar Usuario", command=eliminar_usuario )
eliminar_button.pack ( pady=20 )

# Iniciar el bucle de la interfaz gráfica
root.mainloop ()
