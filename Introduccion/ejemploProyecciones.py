import numpy as np
import matplotlib.pyplot as plt

tiempo = np.arange(100)
ventas_aleatorias = np.random.rand(100)*1000

# Proyectar las ventas con una tendencia lineal
pendiente = 50
interseccion = 1000
ventas_proyectadas = pendiente*tiempo+interseccion+ventas_aleatorias

#graficar informacion
plt.plot(tiempo, ventas_proyectadas, label = "Ventas proyectadas")
plt.xlabel("Tiempo")
plt.ylabel("ventas Proyectadas")
plt.legend()
plt.show()