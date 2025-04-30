import tkinter as tk
from tkinter import ttk
import pandas as pd

def mostrar_datos_parquet(filepath):
    """Muestra los datos de un archivo Parquet en una ventana de Tkinter."""
    # Leer el archivo Parquet
    df = pd.read_parquet(filepath)

    # Ordenar los datos por la columna 'user' alfabéticamente
    df = df.sort_values(by="user", ascending=True)

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Datos de Usuarios")
    root.geometry("1000x600")  # Tamaño de la ventana
    root.resizable(False, False)  # No reescalable
    root.configure(bg="#f5f5f5")  # Fondo gris claro

    # Crear un frame para el Treeview
    frame = tk.Frame(root, bg="#f5f5f5")
    frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Crear Treeview para mostrar los datos
    tree = ttk.Treeview(frame, columns=df.columns.tolist(), show="headings", style="Custom.Treeview")

    # Definir las columnas
    for col in df.columns:
        tree.heading(col, text=col, anchor="center")  # Asignar el nombre de la columna
        tree.column(col, width=300, anchor="center")  # Ajustar el tamaño de las columnas

    # Insertar los datos del DataFrame al Treeview
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    # Colocar el Treeview en el frame
    tree.pack(fill=tk.BOTH, expand=True)

    # Crear un estilo personalizado para el Treeview
    style = ttk.Style()
    style.configure("Custom.Treeview",
                    background="#e3e3e3",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#f5f5f5")
    style.map("Custom.Treeview",
              background=[("selected", "#5c8a8a")],
              foreground=[("selected", "white")])

    # Iniciar el bucle de la interfaz gráfica
    root.mainloop()

# Llamar a la función para mostrar los datos (asegúrate de usar la ruta correcta)
mostrar_datos_parquet("users_prueba.parquet")
