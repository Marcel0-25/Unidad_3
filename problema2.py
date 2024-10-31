import numpy as np

# Parámetro de la distribución
tasa_llegadas = 1 / 15  # 1 llegada cada 15 minutos

# Generación de tiempos entre llegadas para 12 horas (720 minutos)
tiempos_entre_llegadas = np.random.exponential(1 / tasa_llegadas, int(720 / 15))
print("Tiempos entre llegadas de vehículos:", tiempos_entre_llegadas)