import socket
import threading
from pathlib import Path

HOST = '0.0.0.0'  # Acepta conexiones de cualquier IP
PORT = 5001
MAX_CLIENTES = 3
IMAGEN_PATH = Path(__file__).parent / "fsc_1.jpg"

def manejar_cliente(conn, addr):
    print(f"[+] Cliente conectado desde {addr}")
    try:
        while True:
            solicitud = conn.recv(1024).decode()
            print(f"[{addr}] solicitó: {solicitud}")
            if solicitud == "GET_IMAGEN":
                if IMAGEN_PATH.exists():
                    with open(IMAGEN_PATH, 'rb') as f:
                        datos = f.read()
                        conn.sendall(len(datos).to_bytes(8, 'big'))
                        conn.sendall(datos)
                        print(f"[{addr}] Imagen enviada ({len(datos)} bytes)")
                else:
                    conn.sendall(b"ERROR: Imagen no encontrada")
            break
    except Exception as e:
        print(f"[!] Error con {addr}: {e}")
    finally:
        conn.close()
        print(f"[-] Cliente {addr} desconectado")

def iniciar_servidor():
    print("[*] Iniciando servidor...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(MAX_CLIENTES)
    print(f"[*] Servidor escuchando en {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        threading.Thread(target=manejar_cliente, args=(conn, addr)).start()

if __name__ == "__main__":
    iniciar_servidor()
