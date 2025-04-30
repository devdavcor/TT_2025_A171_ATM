import pandas as pd

# Ruta del archivo CSV
ruta_csv = r"C:\Users\devdavcor\Documents\tt\TT_2025_A171_SC\db\usuarios.csv"

# Leer el CSV
df = pd.read_csv(ruta_csv)

# Guardar como Parquet (usando pyarrow o fastparquet)
ruta_parquet = r"C:\Users\devdavcor\Documents\tt\TT_2025_A171_SC\db\usuarios.parquet"
df.to_parquet(ruta_parquet, engine="pyarrow")  # O engine="fastparquet"
