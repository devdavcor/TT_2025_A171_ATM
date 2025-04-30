import pandas as pd
import random
import string

# Función para generar cadenas aleatorias de 10 caracteres
def generar_cadena(longitud=10):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Generar los datos sintéticos
usuarios = [generar_cadena() for _ in range(100)]
contrasenas = [generar_cadena() for _ in range(100)]

# Crear un DataFrame con los datos generados
df = pd.DataFrame({
    'user': usuarios,
    'password': contrasenas
})

# Guardar el DataFrame como un archivo Parquet
df.to_parquet('users_prueba.parquet', engine='pyarrow')

print("Archivo Parquet 'users_prueba.parquet' generado con éxito.")
