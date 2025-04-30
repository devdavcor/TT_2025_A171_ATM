import socket
from pathlib import Path

HOST = '192.168.0.229'
PORT = 5001
ARCHIVO_SALIDA = Path(__file__).parent / "imagen_recibida.jpg"

def pedir_imagen():
    print("[*] Conectando al servidor...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("[+] Conectado")

        s.sendall(b"GET_IMAGEN")
        print("[>] Solicitud enviada")

        longitud = int.from_bytes(s.recv(8), 'big')
        print(f"[<] Recibiendo {longitud} bytes...")

        datos = b""
        while len(datos) < longitud:
            paquete = s.recv(4096)
            if not paquete:
                break
            datos += paquete

        with open(ARCHIVO_SALIDA, 'wb') as f:
            f.write(datos)
            print(f"[✔] Imagen guardada en {ARCHIVO_SALIDA.name}")

if __name__ == "__main__":
    pedir_imagen()
