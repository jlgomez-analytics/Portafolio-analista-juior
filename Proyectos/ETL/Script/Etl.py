###########################################
# Proyecto 2 — Pipeline ETL Automatizado de Calidad de Datos
# Autor: jlgomez-analytics
# Lenguaje: Python
###########################################

# Librerias
import pandas as pd

# 1) Extraccion

df = pd.read_csv("online_retail.csv")
print(df.head())
print(df.info())

# 2) Transformacion

print(df.columns) # Entender el esquema original
print(df.dtypes)

# 3) Normalizacion de columnas

df.columns = df.columns.str.strip().str.lower()
print(df.columns)

# 4) Conversion de fecha
df["invoicedate"] = pd.to_datetime(
    df["invoicedate"],
    errors="coerce"
)

print(df["invoicedate"].head())
print(df["invoicedate"].isnull().sum())

# 5) Conversion de cantidad

df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
)

print(df["quantity"].head())
print(df["quantity"].isnull().sum())

# 6) Conversion precio unitario

df["unitprice"] = pd.to_numeric(
    df["unitprice"],
    errors="coerce"
)

print(df["unitprice"].head())
print(df["unitprice"].isnull().sum())

# 7) Columna Calculada

df["total_amount"] = df["quantity"] * df["unitprice"]

print(df[["quantity", "unitprice", "total_amount"]].head())

# 8) QA exploratorio

print("Nulos por columna:")
print(df.isnull().sum())

print("Cantidad <= 0:")
print((df["quantity"] <= 0).sum())

print("Precio <= 0:")
print((df["unitprice"] <= 0).sum())

print("Cantidad <= 0:", (df["quantity"] <= 0).sum())
print("Precio <= 0:", (df["unitprice"] <= 0).sum())

# Nota: Cantidad y Precios negativos

df[df["quantity"] < 0].head()

# 9) Limpieza Manual

df_clean = df[
    (df["quantity"] > 0) &
    (df["unitprice"] > 0) &
    (df["customerid"].notna())
]
print(df_clean.shape)

# 10) Original vs Limpio
print(df_clean.shape)
print(df.shape)


# 11) Guardar Dataset Limpio

df_clean.to_csv("online_retail_clean.csv", index=False)
