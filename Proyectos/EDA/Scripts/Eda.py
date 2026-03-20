# ============================================================
# Proyecto 1 - Análisis Exploratorio de Datos y Visualización de Datos
# Autor: José Luis Gómez
# Descripción: Exploración inicial de un dataset de ventas Retail
# ============================================================

# Librerias
import pandas as pd
import matplotlib.pyplot as plt

# 1) Cargar dataset público
Ventas = pd.read_csv("retail_sales.csv")

# 2) Inspección inicial 
Ventas.head()
Ventas.info()

# 3) Limpieza simple
Ventas.isnull().sum()

# 4) Estadística descriptiva
Ventas.describe()

# 5) Validacion Logica

Ventas["monto_calculado"] = Ventas["Quantity"] * Ventas["Price per Unit"]

Ventas["diferencia"] = Ventas["monto_calculado"] - Ventas["Total Amount"]

Ventas[abs(Ventas["diferencia"]) > 0.01].shape[0]

# 6) Boxplot para detectar outliers

plt.figure()
plt.boxplot(Ventas["Total Amount"])
plt.title("Boxplot del Monto Total por Transacción")
plt.ylabel("Monto Total")
plt.show()

# 7) Ventas por categoria

ventas_categoria = (
    Ventas.groupby("Product Category")["Total Amount"]
      .sum()
      .reset_index()
      .sort_values("Total Amount", ascending=False)
)
ventas_categoria

plt.figure()
plt.bar(ventas_categoria["Product Category"], ventas_categoria["Total Amount"])
plt.title("Ventas Totales por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Monto Total")
plt.xticks(rotation=45)
plt.show()

# 8) Segmentacion por genero

ventas_genero = (
    Ventas.groupby("Gender")["Total Amount"]
      .sum()
      .reset_index()
)

ventas_genero

# 9) Evolucion temporal de ventas

Ventas["Date"] = pd.to_datetime(Ventas["Date"])

ventas_tiempo = (
    Ventas.groupby(Ventas["Date"].dt.to_period("M"))["Total Amount"]
      .sum()
      .reset_index()
)
