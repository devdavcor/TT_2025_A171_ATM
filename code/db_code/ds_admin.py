import pandas as pd
from pathlib import Path
import random
import string

# Ruta del script actual
RUTA_SCRIPT = Path(__file__).resolve()

# Carpeta /code/db_code/
CARPETA_ACTUAL = RUTA_SCRIPT.parent

# Carpeta raíz del proyecto (/TT_2025_A171_SC/)
RAIZ_PROYECTO = CARPETA_ACTUAL.parent.parent

# Carpeta /db/ dentro del proyecto
CARPETA_DB = RAIZ_PROYECTO / "db"
CARPETA_DB.mkdir(exist_ok=True)

# Ruta completa al archivo CSV
ARCHIVO_USUARIOS = CARPETA_DB / "usuarios.csv"

# Crear o cargar el archivo
if not ARCHIVO_USUARIOS.exists():
    df = pd.DataFrame(columns=["usuario", "password"])
    df.loc[0] = ["admin", "admin"]
    print("Archivo creado con usuario admin.")
else:
    df = pd.read_csv(ARCHIVO_USUARIOS)
    print("Archivo cargado.")

# Verificar si ya existe el usuario admin
if "admin" not in df["usuario"].values:
    df.loc[len(df)] = ["admin", "admin"]

# Generador de usuarios aleatorios
def generar_usuario():
    usuario = ''.join(random.choices(string.ascii_lowercase, k=6))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return usuario, password

# Añadir 5 usuarios aleatorios si no existen ya
for _ in range(5):
    nuevo_usuario, nueva_password = generar_usuario()
    while nuevo_usuario in df["usuario"].values:
        nuevo_usuario, nueva_password = generar_usuario()
    df.loc[len(df)] = [nuevo_usuario, nueva_password]

# Guardar cambios
df.to_csv(ARCHIVO_USUARIOS, index=False)
print("Usuarios actualizados:")
print(df)

print('Probando')
primera_fila = df.iloc[0]
print(primera_fila)

usuario = df.iloc[0]["usuario"]
password = df.iloc[0]["password"]

print(usuario, password)
