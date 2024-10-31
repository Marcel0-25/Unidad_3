import numpy as np

# Parámetros de la distribución
media = 10
desviacion_estandar = 2

# Generación de tiempos de espera para 50 clientes
tiempos_espera = np.random.lognormal(mean=np.log(media), sigma=desviacion_estandar, size=50)
print("Tiempos de espera en el mostrador:", tiempos_espera)