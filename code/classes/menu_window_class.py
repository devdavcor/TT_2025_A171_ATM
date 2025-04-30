import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
import random

def show_menu_window(root, server):
    def centrar_ventana(ventana, ancho, alto):
        ventana.update_idletasks()
        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def start_server():
        server.start_server()

    def stop_server():
        server.stop_server()

    def open_new_window(title) :
        new_window = Toplevel ( root )
        new_window.title ( title )
        new_window.configure ( bg="black" )

        # Tamaño 50% de root
        width = 500
        height = 300
        centrar_ventana ( new_window, width, height )
        new_window.resizable ( False, False )

        # Fondo aleatorio
        base_path = os.path.dirname ( __file__ )
        random_number = random.randint ( 1, 10 )
        background_path = os.path.abspath (
            os.path.join ( base_path, "..", "..", "graphics", "resources", f"f_sc_{random_number}.jpg" ) )
        background_image = Image.open ( background_path )
        background_photo = ImageTk.PhotoImage ( background_image )

        background_label = tk.Label ( new_window, image=background_photo )
        background_label.image = background_photo  # MUY IMPORTANTE
        background_label.place ( x=0, y=0, relwidth=1, relheight=1 )

        # Configuración de filas y columnas para la ventana secundaria
        filas = 24  # Puedes ajustar el número de filas
        columnas = 10  # Puedes ajustar el número de columnas
        for r in range ( filas ) :
            new_window.grid_rowconfigure ( r, weight=1 )
        for c in range ( columnas ) :
            new_window.grid_columnconfigure ( c, weight=1 )

        # Agregar botones o elementos independientes en cada ventana secundaria
        if title == "Settings" :
            settings_button = Button ( new_window, text="Save Settings", command=lambda : print ( "Settings Saved" ),
                                       bg="#D9CFCC", fg="black", font=("Arial", 12) )
            settings_button.grid(row=10, column=8, columnspan=4, rowspan=1, sticky="nsew")

        elif title == "Branches" :
            branch_button = Button ( new_window, text="New Branch", command=lambda : print ( "New Branch Created" ),
                                     bg="#D9CFCC", fg="black", font=("Arial", 12) )
            branch_button.grid ( row=0, column=0, padx=20, pady=20 )

        elif title == "Clients" :
            client_button = Button ( new_window, text="Add Client", command=lambda : print ( "Client Added" ),
                                     bg="#D9CFCC", fg="black", font=("Arial", 12) )
            client_button.grid ( row=0, column=0, padx=20, pady=20 )

        elif title == "Logs" :
            log_button = Button ( new_window, text="View Logs", command=lambda : print ( "Viewing Logs" ), bg="#D9CFCC",
                                  fg="black", font=("Arial", 12) )
            log_button.grid ( row=0, column=0, padx=20, pady=20 )

    def settings():
        open_new_window("Settings")

    def branches():
        open_new_window("Branches")

    def clients():
        open_new_window("Clients")

    def logs():
        open_new_window("Logs")

    def hide_window():
        root.withdraw()

    # === Ventana principal ===
    root.title("Corona Banking Central Server")
    root.configure(bg="black")
    centrar_ventana(root, 1000, 600)
    root.resizable(False, False)

    # === Imagen de fondo e icono ===
    base_path = os.path.dirname(__file__)
    random_number = random.randint(1, 10)
    background_path = os.path.abspath(os.path.join(base_path, "..", "..", "graphics", "resources", f"f_sc_{random_number}.jpg"))
    background_image = Image.open(background_path)
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    icon_path = os.path.abspath(os.path.join(base_path, "..", "..", "graphics", "resources", "icon.png"))
    icon = PhotoImage(file=icon_path)
    root.iconphoto(False, icon)

    # === Grid ===
    filas = 24
    columnas = 20
    for r in range(filas):
        root.grid_rowconfigure(r, weight=1)
    for c in range(columnas):
        root.grid_columnconfigure(c, weight=1)

    # === Labels ===
    label_main = Label(root, text="Corona Banking Central Server",
                       bg="#195959", fg="white", font=("Arial", 18, "bold"))
    label_main.grid(row=3, column=6, columnspan=8, rowspan=1, sticky="nsew")

    label_a = Label(root, text="Menu",
                    bg="#195959", fg="white", font=("Arial", 16))
    label_a.grid(row=6, column=8, columnspan=4, rowspan=1, sticky="nsew")

    # === Botones ===
    b_start = Button(root, text="Start Server", command=start_server,
                     bg="#D9CFCC", fg="black", font=("Arial", 14))
    b_start.grid(row=10, column=3, columnspan=4, rowspan=1, sticky="nsew")

    b_stop = Button(root, text="Stop Server", command=stop_server,
                    bg="#D9CFCC", fg="black", font=("Arial", 14))
    b_stop.grid(row=10, column=8, columnspan=4, rowspan=1, sticky="nsew")

    b_settings = Button(root, text="Settings", command=settings,
                        bg="#D9CFCC", fg="black", font=("Arial", 14))
    b_settings.grid(row=10, column=13, columnspan=4, rowspan=1, sticky="nsew")

    b_branch = Button(root, text="Branches", command=branches,
                      bg="#D9CFCC", fg="black", font=("Arial", 14))
    b_branch.grid(row=15, column=3, columnspan=4, rowspan=1, sticky="nsew")

    b_client = Button(root, text="Clients", command=clients,
                      bg="#D9CFCC", fg="black", font=("Arial", 14))
    b_client.grid(row=15, column=8, columnspan=4, rowspan=1, sticky="nsew")

    b_log = Button(root, text="Logs", command=logs,
                   bg="#D9CFCC", fg="black", font=("Arial", 14))
    b_log.grid(row=15, column=13, columnspan=4, rowspan=1, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    server = None  # Aquí puedes pasar la instancia del servidor si la tienes
    show_menu_window(root, server)
    root.mainloop()
