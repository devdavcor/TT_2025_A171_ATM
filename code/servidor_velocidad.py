import socket
import time

HOST = "0.0.0.0"  # Escucha desde cualquier IP
PORT = 5001       # Puedes cambiarlo si quieres

BUFFER_SIZE = 65536

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Esperando conexión en {HOST}:{PORT}...")
        conn, addr = s.accept()
        print(f"Conexión establecida desde {addr}")

        total_data = 0
        start_time = time.time()

        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            total_data += len(data)

        end_time = time.time()
        elapsed = end_time - start_time
        velocidad_MBps = (total_data / 1024 / 1024) / elapsed

        print(f"\n📦 Total recibido: {total_data / 1024 / 1024:.2f} MB")
        print(f"⏱️ Tiempo: {elapsed:.2f} segundos")
        print(f"⚡ Velocidad: {velocidad_MBps:.2f} MB/s")

if __name__ == "__main__":
    run_server()
