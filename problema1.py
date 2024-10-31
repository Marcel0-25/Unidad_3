import numpy as np

# Parámetros
pedidos_totales = 20
probabilidad_exito = 0.7

# Generación de variables aleatorias binomiales para 7 días
pedidos_satisfechos = np.random.binomial(pedidos_totales, probabilidad_exito, 7)
print("Pedidos satisfechos durante la semana:", pedidos_satisfechos)