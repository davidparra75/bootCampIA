import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt

#creacion objeto series
s = pd.Series([2,4,6,8,10])
print(s)

#creacion de un objeto serie inicializando con un diccionario de python
altura = {"Santiago":180, "Marcelo":172, "Luis":174, "Alejandra":160}
s = pd.Series(altura)
print(s)
""""
Creacion de un objeto series inicializandolo con algunos
de los elementos de un diccionario 
"""
altura = {"Santiago":180, "Marcelo":172, "Luis":174, "Alejandra":160}
s = pd.Series(altura, index = ["Marcelo","Luis"])
print(s)

#creacion de un objeto series inicializandoo con un escalar
s = pd.Series(34,["test1","test2","test3"])
print(s)

#Acceso a los elementos de un objeto o series
# cada eleemnto del objeto series tiene un identificdor unico
s = pd.Series([2,4,6,8],index=["num1","num2","num3","num4"])
print(s)
#accediendo al tercer elemento del objeto
print(s.loc["num3"])
print(s.iloc[2])

print(s.iloc[2:4])

#operaciones aritmeticas con series
print("suma de el arreglo",np.sum(s))
print(f"suma{np.sum(s)}")

temperaturas = pd.Series([4.4,5.1,6.1,6.2,7.1,7.2,8.2,8.9])
s = pd.Series(temperaturas, name="Temperaturas")
print(s)
s.plot()
plt.show()

#creacion de un objeto dataframe
personas={
    "peso":pd.Series([90,80,70,60],["Santiago","Marcelo","Luis","Alejandra"]),
    "altura":pd.Series({"Santiago":180,"Marcelo":172, "Luis":174, "Alejandra":160}),
    "hijos":pd.Series([2,3],["Luis","Marcelo"])
}
df = pd.DataFrame(personas)
print(df)
df2 = pd.DataFrame(
    personas,
    columns=["altura","peso"],
    index=["Santiago","Luis","Marcelo"]
)
print(df2)

print(df["peso"])

df3 =(df["peso"]>=60) & (df["peso"]<80)
print(df3)

#consultas avanzadas
df = df.query("altura >= 170 and peso > 70")
print(df)
#copiar un dataframe
df_copy = df.copy()
df_mod = df_copy.assign(mascotas=[1,3,])
print(df_mod) 