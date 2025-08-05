import pandas as pd
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
print(s["num3"])