import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset ficticio
datos_estudiantes = {
    "peso": pd.Series([55, 68, 74, 60, 72], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "altura": pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "promedio": pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "edad": pd.Series([17, 18, 17, 19, 18], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
}

df = pd.DataFrame(datos_estudiantes)
print(df)

#crear una serie con los nombres y alturas de los estudiantes 

s = pd.Series(datos_estudiantes["altura"])
print(s)


print(datos_estudiantes["promedio"].loc["Carlos"])
print(datos_estudiantes["promedio"].iloc[1])
print(datos_estudiantes["promedio"].iloc[1:2])

s2 = (datos_estudiantes["promedio"]>=4.0)
print(s2)

#estadisticas descriptiva
estadisticas = df.describe()
print(estadisticas)

# if df["edad"]>=18:
#     df = df.assign(mayor=[True])
# else:
#     df = df.assign(mayor=[False])
df = df.assign(mayor=[False, True, False, True, True])
print(df)


df["AñoNacimiento"] = 2025 - df["edad"]
print(df)

#vizualiza los promedios de los estudiantes en un grafico

df["promedio"].plot(kind="bar",title="Promedio de Estudiantes")
plt.xlabel=("Estudiante")
plt.ylabel=("Promedio")
plt.show()

df = df.query("altura >= 165 and altura <=175")
print(df)

dfcopy = df.copy()
del dfcopy["peso"]
print(dfcopy)

datosNuevodf = {
    "nombre":pd.Series(["luisa","ana","david"]),
    "edad":pd.Series([18,20,26]),
    "nacimiento":pd.Series([2004,2003,2003])
}

dfNuevo = pd.DataFrame(datosNuevodf)
print(dfNuevo)
