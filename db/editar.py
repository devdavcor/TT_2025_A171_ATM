import tkinter as tk
from tkinter import messagebox
import pandas as pd


# Función para cambiar la contraseña
def cambiar_contrasena() :
    # Obtener los valores ingresados
    username = entry_user.get ()
    old_password = entry_old_password.get ()
    new_password = entry_new_password.get ()

    # Leer el archivo Parquet
    df = pd.read_parquet ( 'users_prueba.parquet' )

    # Comprobar si el usuario existe
    if username in df['user'].values :
        # Obtener la contraseña almacenada para el usuario
        stored_password = df.loc[df['user'] == username, 'password'].values[0]

        # Verificar si la contraseña antigua coincide
        if old_password == stored_password :
            # Cambiar la contraseña por la nueva
            df.loc[df['user'] == username, 'password'] = new_password

            # Guardar los cambios en el archivo Parquet
            df.to_parquet ( 'users_prueba.parquet', engine='pyarrow' )

            # Mostrar mensaje de éxito
            messagebox.showinfo ( "Éxito", f"La contraseña para el usuario {username} ha sido cambiada." )
        else :
            # Mostrar mensaje si la contraseña antigua no coincide
            messagebox.showerror ( "Error", "La contraseña antigua no coincide." )
    else :
        # Mostrar mensaje si el usuario no existe
        messagebox.showerror ( "Error", f"El usuario {username} no existe." )


# Crear la ventana principal
root = tk.Tk ()
root.title ( "Cambiar Contraseña" )
root.geometry ( "400x400" )  # Tamaño de la ventana
root.resizable ( False, False )  # No reescalable

# Etiqueta para el nombre de usuario
label_user = tk.Label ( root, text="Ingrese el nombre de usuario:" )
label_user.pack ( pady=10 )

# Campo de entrada para el nombre de usuario
entry_user = tk.Entry ( root, width=30 )
entry_user.pack ( pady=10 )

# Etiqueta para la contraseña antigua
label_old_password = tk.Label ( root, text="Ingrese la contraseña antigua:" )
label_old_password.pack ( pady=10 )

# Campo de entrada para la contraseña antigua
entry_old_password = tk.Entry ( root, width=30, show="*" )
entry_old_password.pack ( pady=10 )

# Etiqueta para la nueva contraseña
label_new_password = tk.Label ( root, text="Ingrese la nueva contraseña:" )
label_new_password.pack ( pady=10 )

# Campo de entrada para la nueva contraseña
entry_new_password = tk.Entry ( root, width=30, show="*" )
entry_new_password.pack ( pady=10 )

# Botón para cambiar la contraseña
change_password_button = tk.Button ( root, text="Cambiar Contraseña", command=cambiar_contrasena )
change_password_button.pack ( pady=20 )

# Iniciar el bucle de la interfaz gráfica
root.mainloop ()
