import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
print(df)
df['species'] = df['species'].map(dict(zip(range(3),iris.target_names)))

print(df.head())

#tipos de datos de las columnas
print(df.info())

#estadisticas descriptivas
print(df.describe())

#contar cuantas flores hay de cada clase
especie_count = df['species'].value_counts()
print(especie_count)

#crear grafico de Barras

plt.bar(especie_count.index,especie_count.values, color="red")
plt.xlabel("Especie")
plt.ylabel("Cantidad")
plt.title("Distrubucion de las especies")
plt.show()

#crear matriz de correlacion

df["species"]=iris.target

correlacion_matriz = df.corr()
sns.heatmap(correlacion_matriz, annot=True, cmap="coolwarm")
plt.title("Correlacion entre variables")
plt.show()
