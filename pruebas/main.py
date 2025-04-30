import subprocess
import time
from pathlib import Path

BASE = Path(__file__).parent
RUTA_SERVIDOR = BASE / "servidor" / "servidor.py"
RUTA_CLIENTE = BASE / "cliente" / "cliente.py"

def main():
    print("[*] RUTA_SERVIDOR:", RUTA_SERVIDOR)
    print("[*] RUTA_CLIENTE:", RUTA_CLIENTE)

    print("[*] Iniciando servidor...")
    servidor = subprocess.Popen(["python", str(RUTA_SERVIDOR)])

    time.sleep(2)  # Esperamos a que el servidor arranque bien

    print("[*] Iniciando cliente...")
    cliente = subprocess.Popen(["python", str(RUTA_CLIENTE)])
    cliente.wait()

    print("[*] Cliente terminó.")
    servidor.terminate()
    print("[*] Servidor detenido.")

if __name__ == "__main__":
    main()
