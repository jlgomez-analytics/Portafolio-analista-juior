## Proyecto 1 — Análisis Exploratorio de Datos (EDA) y Visualización de Datos (BI)

En este proyecto se trabajará en poder entender el comportamiento de los datos, identificar tendencias, outliers y construir visualizaciones que permitan apoyar la toma de decisiones.

## Fuente de Datos

Retail Sales Dataset (obtenido desde Kaggle): https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset.
Los datos fueron utilizados exclusivamente con fines educativos y de análisis exploratorio.

##  Dataset
Dataset de ventas Retail que contiene información de:
- Transaction ID: Identificador único de cada transacción.
- Date: Fecha en la que se realizó la transacción.
- Customer ID: Identificador único de cada cliente.
- Gender: Género del cliente (Masculino/Femenino).
- Age: Edad del cliente.
- Product Category: Categoría del producto adquirido.
- Quantity: Cantidad de unidades del producto compradas en la transacción.
- Price per Unit: Precio de una unidad del producto.
- Total Amount: Monto total de la transacción, que representa el valor monetario de cada compra.

##  Tecnologías
- Python 
- R 
- Power BI (Power Query/ Medidas DAX)

## Interpretacion del Análisis

**Validación de calidad de datos (QA)**

Se realizó una validación lógica para verificar la consistencia del dataset, confirmando que el monto total de cada transacción corresponde al producto entre cantidad y precio unitario:

Total Amount = Quantity × Price per Unit

No se detectaron inconsistencias, lo que indica una buena calidad de los datos y confiabilidad para análisis posteriores.

**Detección de outliers**

Se identificaron transacciones con montos significativamente superiores al resto del conjunto de datos.
Estos outliers podrían corresponder a compras de alto volumen o a comportamientos atípicos de ciertos clientes.
