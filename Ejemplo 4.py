import numpy as np
import matplotlib.pyplot as plt
import math


lambda_poisson = 5  


num_simulaciones = 100  
U = np.random.uniform(0, 1, num_simulaciones)


def poisson_pmf(lambda_poisson, k):
    return (lambda_poisson ** k) * math.exp(-lambda_poisson) / math.factorial(k)


def poisson_inverse_transform(lambda_poisson, U):
    F_k = 0  
    k = 0
    while True:
        F_k += poisson_pmf(lambda_poisson, k)  
        if U <= F_k:
            return k  
        k += 1


llegadas_simuladas = [poisson_inverse_transform(lambda_poisson, u) for u in U]


print("Número de clientes que llegaron en cada simulación (hora):")
print(llegadas_simuladas)


plt.hist(llegadas_simuladas, bins=np.arange(min(llegadas_simuladas), max(llegadas_simuladas) + 1) - 0.5, edgecolor='black')
plt.title("Simulación de llegadas de clientes (Distribución Poisson)")
plt.xlabel("Número de clientes por hora")
plt.ylabel("Frecuencia")
plt.show()