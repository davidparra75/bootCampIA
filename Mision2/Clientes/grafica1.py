import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

#1 carga de datos
df = pd.read_csv('clientes_supermercado.csv')
print(df)

#redondear antes de convertir a int
df['Edad']=df['Edad'].round().astype(int)
df['VisitasPorMes']=df['VisitasPorMes'].round().astype(int)
print(df)
x= df[['Edad','GastoMensual', 'VisitasPorMes']]

 #4 entrenar kmeans con k=4
KMeans=KMeans(n_clusters=4,random_state=42)
KMeans.fit(x)
df['Cluster']=KMeans.labels_

#graficar  en 3d con anotaciones 
fig=plt.figure(figsize=(10,7))
ax=fig.add_subplot(111,projection='3d')
#colocar colores 
sc=ax.scatter(df['Edad'],df['GastoMensual'],df['VisitasPorMes'],
              c=df['Cluster'],cmap='viridis',s=50
              )

#etiquetas de ejes 
ax.set_xlabel('Edad')
ax.set_ylabel('Gastos Mensuales')
ax.set_zlabel('Visitas Por mes ')
plt.title('Segmentacion de clietes Means k=4')

#Anotaciones interpretativas

ax.text(22,80,2,'Jovenes gasto bajo \n pocas visitas',color='black')
ax.text(38,480,9,'familias gasto alto \n frecuentes visitas ',color='black')
ax.text(63,410,5,'Mayores gasto medio \n visitas regulares ',color='black')
ax.text(33,920, 11,'clientes VIP \n gastos muy alto',color='black')
plt.show()