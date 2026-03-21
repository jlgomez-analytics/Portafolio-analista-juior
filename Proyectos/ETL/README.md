# Proyecto 2 — Pipeline ETL Automatizado de Calidad de Datos

Este proyecto tiene como objetivo asegurar la calidad de los datos mediante la implementación de validaciones y el desarrollo de un pipeline ETL automatizado en Python, aplicado a un dataset transaccional de ventas retail. El pipeline permite:

- Procesar datos crudos

- Aplicar transformaciones estructurales

- Ejecutar validaciones de calidad de datos (QA)

- Generar un dataset limpio y listo para análisis

## Fuente de Datos

El dataset utilizado para realizar las validaciones y el pipeline ETL es Online Retail Dataset (obtenido desde Kaggle): [https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset). Los datos fueron utilizados exclusivamente con fines educativos

## Dataset

El dataset contiene la siguiente informacion:

- InvoiceNo: Número de factura.

- StockCode: Código de producto.
  
- Description: Nombre del producto.

- Quantity: Cantidad de cada producto por transacción. 

- InvoiceDate: Fecha y hora de la factura.

- UnitPrice: Precio unitario.

- CustomerID: Número de cliente.

- Country: Nombre del país.

## Tecnologías

- Python

## Flujo ETL

El pipeline sigue las tres etapas clásicas de ETL:

**Extract**

- Lectura del dataset desde archivo CSV

**Transform**

- Normalización de nombres de columnas

- Conversión de tipos de datos

- Creación de variable derivada:
  total_amount = quantity * unitprice
  
**Load**

- Exportación del dataset limpio a CSV

- Archivo listo para consumo analítico
  
## Data Quality (QA)

Se aplicaron reglas de calidad para asegurar consistencia:

- Eliminación de devoluciones 

- Eliminación de precios inválidos 

- Eliminación de registros sin cliente 

Estas validaciones permiten evitar errores en análisis posteriores.


## Principales hallazgos de calidad de datos

Durante el análisis se identificaron:

- 25% de registros sin customerid

- Registros con cantidades negativas que se interpretaron como devoluciones

- Precios nulos o iguales a cero

Estos problemas fueron tratados mediante reglas de limpieza en el pipeline.

## Conclusión

A partir del análisis, se identificaron diversas inconsistencias en los datos, por lo que fue necesario implementar validaciones de calidad orientadas a garantizar la confiabilidad de la información. Esto permitió obtener un dataset limpio y consistente, que pueda generar resultados más precisos y aportar valor a la toma de decisiones del negocio. 


