import tkinter as tk
from PIL import Image, ImageTk
import random

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Corona Banking Central Server")
        self.root.configure(bg="white")
        self.center_window(self.root, 1000, 600)
        self.root.resizable(False, False)

        # Change icon
        self.icon = tk.PhotoImage(file="resources/icon.png")
        self.root.iconphoto(False, self.icon)

        # Add background
        self.add_background()

        # Configure grid cells
        self.configure_grid(rows=24, columns=20)

        # Create popup window
        self.create_popup_window()

    def center_window(self, window, width, height):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def add_background(self):
        # Generar un número aleatorio entre 1 y 10 (inclusive)
        random_number = random.randint(1, 10)
        image_path = f"resources/f_sc_{random_number}.jpg"  # Usamos el número aleatorio
        image = Image.open(image_path)
        self.background_img = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.root, image=self.background_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def configure_grid(self, rows, columns):
        for r in range(rows):
            self.root.grid_rowconfigure(r, weight=1)
        for c in range(columns):
            self.root.grid_columnconfigure(c, weight=1)

    def create_popup_window(self):
        self.popup_window = tk.Toplevel(self.root)
        self.popup_window.withdraw()

    def show_window(self):
        self.popup_window.deiconify()

    def hide_window(self):
        self.popup_window.withdraw()

    def create_button(self, text, command, row, column, columnspan=1, rowspan=1, bg="gray", fg="black"):
        button = tk.Button(self.root, text=text, command=command, bg=bg, fg=fg)
        button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky="nsew", padx=2, pady=2)

    def create_entry(self, row, column, columnspan=1, rowspan=1, show_text=True):
        entry = tk.Entry(self.root, bg="white", fg="black", font=("Arial", 12))
        if not show_text:
            entry.config(show="*")  # Asterisks for passwords
        entry.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky="nsew", padx=2, pady=2)

    def create_label(self, text, row, column, columnspan=1, rowspan=1, bg="white", fg="black", font=("Arial", 12)):
        label = tk.Label(self.root, text=text, bg=bg, fg=fg, font=font)
        label.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky="nsew", padx=2, pady=2)

# Función fuera de la clase para decir "Hola Mundo"
def say_hello():
    print("¡Hola Mundo!")

# Crear la instancia de la clase y usar el método
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)  # Creamos el objeto de la clase

    # Crear un botón fuera de la clase que llama a say_hello
    app.create_button(
        text="Say Hello", command=say_hello, row=5, column=5, bg="blue", fg="white"
    )

    root.mainloop()  # Correcta indentación
