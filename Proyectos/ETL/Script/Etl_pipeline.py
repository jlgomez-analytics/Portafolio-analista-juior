###########################################
# Proyecto 2 — Pipeline ETL Automatizado de Calidad de Datos
# Autor: José Luis Gómez
# Descripción: Diseño de Pipeline ETL Automatizado
###########################################

# Librerias

import pandas as pd

# 1) Extraccion

def extract():
    df = pd.read_csv("online_retail.csv")
    return df

# 2) Transformacion

def transform(df):
    
    # 2.1) Normalizar columnas
    df.columns = df.columns.str.strip().str.lower()

    # 2.2) Convertir tipos
    df["invoicedate"] = pd.to_datetime(df["invoicedate"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unitprice"] = pd.to_numeric(df["unitprice"], errors="coerce")

    # 2.3) Crear columna derivada
    df["total_amount"] = df["quantity"] * df["unitprice"]

    # 2.4) Reglas de calidad de datos
    df_clean = df[
        (df["quantity"] > 0) &
        (df["unitprice"] > 0) &
        (df["customerid"].notna())
    ]

    return df_clean

# 3) Cargado

def load(df):
    df.to_csv("online_retail_clean.csv", index=False)

    print("Dataset limpio guardado correctamente")

# 3.1) Creacion de Pipeline

def run_pipeline():
    print("Iniciando pipeline ETL")

    df = extract()

    df_clean = transform(df)

    load(df_clean)

    print("Pipeline finalizado correctamente")

run_pipeline()
