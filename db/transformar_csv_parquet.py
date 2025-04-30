import pandas as pd

# Cargar el CSV
df = pd.read_csv("sucursales.csv")

# Guardar como Parquet
df.to_parquet("sucursales.parquet", index=False)
