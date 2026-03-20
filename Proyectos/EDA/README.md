## Proyecto 1 — Análisis Exploratorio de Datos y Visualización de Datos 

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

**Validación de calidad de datos**

Se realizó una validación lógica para verificar la consistencia del dataset, confirmando que el monto total de cada transacción corresponde al producto entre cantidad y precio unitario:

Total Amount = Quantity × Price per Unit

No se detectaron inconsistencias, lo que indica una buena calidad de los datos y confiabilidad para análisis posteriores.

**Detección de outliers**

Se identificaron transacciones con montos significativamente superiores al resto del conjunto de datos.
Estos outliers podrían corresponder a compras de alto volumen o a comportamientos atípicos de ciertos clientes.

**Cantidad de productos**

La variable Quantity muestra que la mayoría de las transacciones corresponden a compras de pocas unidades, lo que indica un patrón de consumo principalmente minorista.

**Precio por unidad**

El Price per Unit presenta una dispersión moderada, reflejando la coexistencia de productos de bajo y alto valor dentro del catálogo. Esta variabilidad explica, en parte, las diferencias observadas en el monto total de las transacciones y permite identificar categorías de productos con distinto posicionamiento de precio.

**Monto total de la transacción**

El Total Amount exhibe una distribución asimétrica hacia la derecha, con la mayoría de las transacciones concentradas en montos bajos o medios y una cola hacia valores altos. Esto nos indica que:

- La media tiende a ser mayor que la mediana

- Los outliers influyen significativamente en el promedio

- La mediana resulta una medida más representativa del comportamiento típico de las transacciones

**Edad de los clientes**

La variable Age muestra una distribución relativamente amplia, lo que sugiere una base de clientes diversa en términos etarios. Esto permite segmentar el análisis y evaluar cómo varían los patrones de consumo entre distintos grupos de edad.


## Insights del Análisis Exploratorio

**Ventas por categoría de producto**

El análisis evidenció que las categorías de Electrónicos y Ropa concentran una mayor proporción del monto total de ventas, sin presentar diferencias significativas entre ellas.
Esto sugiere que ambas categorías actúan como los principales motores de ingresos del negocio.

Este resultado permite identificar estas categorías como estratégicas para priorizar decisiones de inventario y acciones comerciales.

**Segmentación por género**

Se observaron diferencias en el comportamiento de compra entre géneros, donde el género femenino presenta un mayor aporte al monto total de ventas en comparación con el masculino.
Este resultado sugiere la existencia de patrones de consumo diferenciados, lo que podría ser aprovechado para estrategias de marketing segmentadas o para la personalización de ofertas.

**Análisis por edad**

El análisis inicial mediante un gráfico de dispersión entre edad y monto de compra muestra una alta dispersión y ausencia de una relación clara entre ambas variables.
Esto sugiere que la edad, de forma individual, no es un factor determinante del monto de las transacciones, siendo necesario agrupar por rangos etarios para obtener conclusiones más interpretables.

**Evolución temporal de las ventas**

La exploración temporal permitió identificar variaciones en el nivel de ventas a lo largo del tiempo, lo que sugiere posibles efectos de estacionalidad o la influencia de eventos específicos.
En particular, se observa que el mes de mayo concentra el mayor nivel de ventas del año 2023.
Este comportamiento resalta la importancia de considerar el factor temporal en la planificación y proyección de ventas.

##  Conclusión

El análisis exploratorio permitió identificar patrones clave en el comportamiento de ventas retail, destacando una distribución asimétrica de los montos, la relevancia de las categorías de Electrónicos y Ropa, y diferencias en el comportamiento de compra por género.

No se observó una relación clara entre edad y monto de compra, mientras que el análisis temporal evidenció variaciones relevantes en las ventas, con una alza en las ventas en mayo de 2023. La validación de calidad de datos confirmó la consistencia del dataset, proporcionando una base confiable para análisis posteriores.
