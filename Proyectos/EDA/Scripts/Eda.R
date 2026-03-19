# ============================================================
# Proyecto 1 - Análisis Exploratorio de Datos (EDA) y Visualización de Datos (BI)
# Autor: José Luis Gómez
# Descripción: Exploración inicial de un dataset de ventas Retail
# ============================================================

# 1. Librerías 
library(tidyverse)
library(lubridate)

# 2. Carga de datos 
Ventas <- read_csv(file.choose())

# 3. Inspección inicial 
head(Ventas)
glimpse(Ventas)
summary(Ventas)

# Dimensiones del dataset
cat("Filas:", nrow(Ventas), "\n")
cat("Columnas:", ncol(Ventas), "\n")

# 4. Calidad de datos
# Valores nulos por variable
na_summary <- colSums(is.na(Ventas))
print(na_summary)

# Porcentaje de nulos
na_pct <- round(colMeans(is.na(Ventas)) * 100, 2)
print(na_pct)

# 4.1. Validacion de datos

# Total Amount debería ser Quantity * Price per Unit

Ventas %>%
  mutate(check = Quantity * price_per_unit) %>%
  summarise(
    diferencias = sum(abs(check - total_amount) > 0.01, na.rm = TRUE)
  )

# 5. Outliers 
Q1 <- quantile(Ventas$total_amount, 0.25, na.rm = TRUE)
Q3 <- quantile(Ventas$total_amount, 0.75, na.rm = TRUE)
IQR <- Q3 - Q1

outliers <- Ventas %>%
  filter(total_amount < Q1 - 1.5 * IQR |
         total_amount > Q3 + 1.5 * IQR)

cat("Cantidad de outliers detectados:", nrow(outliers), "\n")

ggplot(Ventas, aes(y = total_amount)) +
  geom_boxplot(fill = "tomato") +
  labs(title = "Distribución del monto total y outliers")

# 6. Transformaciones básicas 

Ventas <- Ventas %>%
  rename(
    transaction_id = `Transaction ID`,
    customer_id = `Customer ID`,
    product_category = `Product Category`,
    price_per_unit = `Price per Unit`,
    total_amount = `Total Amount`
  ) %>%
  mutate(
    Date = as.Date(Date),
    Gender = as.factor(Gender),
    product_category = as.factor(product_category)
  )

# 7. Estadística descriptiva 

Ventas %>%
  summarise(
    monto_promedio = mean(total_amount, na.rm = TRUE),
    monto_mediano = median(total_amount, na.rm = TRUE),
    monto_max = max(total_amount, na.rm = TRUE),
    monto_min = min(total_amount, na.rm = TRUE),
    edad_promedio = mean(Age, na.rm = TRUE)
  )
hist(Ventas$total_amount)

# 8. Ventas por categoría 

ventas_categoria <- Ventas %>%
  group_by(product_category) %>%
  summarise(
    ventas_totales = sum(total_amount, na.rm = TRUE),
    ticket_promedio = mean(total_amount, na.rm = TRUE),
    transacciones = n()
  ) %>%
  arrange(desc(ventas_totales))

print(ventas_categoria)

ggplot(ventas_categoria,
       aes(x = reorder(product_category, ventas_totales),
           y = ventas_totales)) +
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(
    title = "Ventas totales por categoría de producto",
    x = "Categoría",
    y = "Ventas totales"
  )

# 9. Segmentación por género 

Ventas %>%
  group_by(Gender) %>%
  summarise(
    ventas_totales = sum(total_amount, na.rm = TRUE),
    ticket_promedio = mean(total_amount, na.rm = TRUE)
  ) %>%
  ggplot(aes(x = Gender, y = ventas_totales)) +
  geom_col(fill = "darkgreen") +
  labs(
    title = "Ventas totales por género",
    x = "Género",
    y = "Ventas"
  )

# 10. Análisis por edad 

Ventas %>%
  ggplot(aes(x = Age, y = total_amount)) +
  geom_point(alpha = 0.4) +
  labs(
    title = "Relación entre edad y monto de compra",
    x = "Edad",
    y = "Monto total"
  )


# 11. Evolución temporal 

ventas_tiempo <- Ventas %>%
  group_by(Date) %>%
  summarise(ventas_totales = sum(total_amount, na.rm = TRUE))

ggplot(ventas_tiempo, aes(x = Date, y = ventas_totales)) +
  geom_line(color = "black") +
  labs(
    title = "Evolución temporal de las ventas",
    x = "Fecha",
    y = "Ventas"
  )
