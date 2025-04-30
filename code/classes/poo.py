import tkinter as tk
from PIL import Image, ImageTk
from login_class import *
import os
import random

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Corona Banking Central Server")
        self.root.configure(bg="black")
        self.centrar_ventana(self.root, 1000, 600)
        self.root.resizable(False, False)

        # Cambiar ícono
        self.icono = tk.PhotoImage(file=self.obtener_ruta_recurso("icon.png"))
        self.root.iconphoto(False, self.icono)

        # Agregar fondo
        self.agregar_fondo()

        # Configurar celdas
        self.configurar_celdas(filas=24, columnas=20)

        # Crear etiquetas
        self.crear_label(
            texto="Corona Banking Central Server",
            row=3, column=6, columnspan=8, rowspan=1,
            bg="#195959", fg="white", font=("Arial", 18, "bold")
        )
        self.crear_label(
            texto="Please, enter your credentials below",
            row=7, column=8, columnspan=4, rowspan=1,
            bg="#195959", fg="white", font=("Arial", 16)
        )
        self.crear_label(
            texto="User:",
            row=10, column=7, columnspan=3, rowspan=1,
            bg="#195959", fg="white", font=("Arial", 14)
        )
        self.crear_label(
            texto="Password:",
            row=13, column=7, columnspan=3, rowspan=1,
            bg="#195959", fg="white", font=("Arial", 14)
        )

        # Entradas de texto
        self.inputText1 = tk.StringVar()
        self.inputText2 = tk.StringVar()
        self.crear_entry(row=10, column=10, columnspan=3, rowspan=1, variable=self.inputText1)
        self.crear_entry(row=13, column=10, columnspan=3, rowspan=1, variable=self.inputText2, mostrar_texto=False)

        # Botones
        self.crear_boton(
            texto="Ingresar", comando=self.authentication,
            row=18, column=6, columnspan=3, rowspan=1,
            bg="#BFA980", fg="white"
        )
        self.crear_boton(
            texto="Cerrar", comando=self.hide_window,
            row=18, column=11, columnspan=3, rowspan=1,
            bg="#D9CFCC", fg="black"
        )

    def obtener_ruta_recurso(self, nombre_recurso):
        base_path = os.path.dirname(__file__)
        return os.path.abspath(os.path.join(base_path, "..", "..", "graphics", "resources", nombre_recurso))

    def centrar_ventana(self, ventana, ancho, alto):
        ventana.update_idletasks()
        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def agregar_fondo(self):
        random_number = random.randint(1, 10)
        fondo_path = self.obtener_ruta_recurso(f"f_sc_{random_number}.jpg")
        fondo_imagen = Image.open(fondo_path)
        fondo_photo = ImageTk.PhotoImage(fondo_imagen)
        fondo_label = tk.Label(self.root, image=fondo_photo)
        fondo_label.image = fondo_photo
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_celdas(self, filas, columnas):
        for r in range(filas):
            self.root.grid_rowconfigure(r, weight=1)
        for c in range(columnas):
            self.root.grid_columnconfigure(c, weight=1)

    def crear_boton(self, texto, comando, row, column, columnspan=1, rowspan=1, bg="gray", fg="black"):
        boton = tk.Button(self.root, text=texto, command=comando, bg=bg, fg=fg)
        boton.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky="nsew", padx=2, pady=2)

    def crear_entry(self, row, column, columnspan=1, rowspan=1, variable=None, mostrar_texto=True):
        entry = tk.Entry(self.root, textvariable=variable, bg="white", fg="black", font=("Arial", 12))
        if not mostrar_texto:
            entry.config(show="*")  # Asteriscos para contraseñas
        entry.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky="nsew", padx=2, pady=2)

    def crear_label(self, texto, row, column, columnspan=1, rowspan=1, bg="white", fg="black", font=("Arial", 12)):
        label = tk.Label(self.root, text=texto, bg=bg, fg=fg, font=font)
        label.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky="nsew", padx=2, pady=2)

    def authentication(self):
        base_path = os.path.dirname(__file__)
        parquet_path = os.path.abspath(os.path.join(base_path, "..", "..", "db", "usuarios.parquet"))
        login_system = Login(parquet_path)
        a = self.inputText1.get()
        b = self.inputText2.get()

        # Cerrar cualquier ventana previa con el mismo título
        for widget in tk._default_root.winfo_children():
            if isinstance(widget, tk.Toplevel) and widget.title() == "Login message":
                widget.destroy()

        # Crear ventana emergente
        v_1 = tk.Toplevel(self.root)
        v_1.withdraw()
        v_1.title("Login message")
        v_1.geometry("250x150")
        self.centrar_ventana(v_1, 250, 150)
        v_1.resizable(False, False)

        random_number_v_1 = random.randint(1, 10)
        fondo_path = self.obtener_ruta_recurso(f"f_sc_{random_number_v_1}.jpg")
        fondo_imagen_v1 = Image.open(fondo_path)
        fondo_photo_v1 = ImageTk.PhotoImage(fondo_imagen_v1)
        fondo_label_v1 = tk.Label(v_1, image=fondo_photo_v1)
        fondo_label_v1.image = fondo_photo_v1
        fondo_label_v1.place(x=0, y=0, relwidth=1, relheight=1)

        if not a or not b:
            label_hello = tk.Label(v_1, text="Please fill both fields!", bg="#195959", fg="white", font=("Arial", 10))
            label_hello.place(relx=0.5, rely=0.5, anchor="center")
            v_1.deiconify()
            return

        auth_aux = login_system.start_login(a, b)

        if auth_aux != False:
            message = 'Login Success!'
        else:
            message = 'Login Failed!'

        label_hello = tk.Label(v_1, text=message, bg="#195959", fg="white", font=("Arial", 10))
        label_hello.place(relx=0.5, rely=0.5, anchor="center")
        v_1.deiconify()

    def hide_window(self):
        v_1.deiconify()
        v_1.withdraw()

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
