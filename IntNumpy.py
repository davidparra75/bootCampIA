# import numpy as np
# import matplotlib.pyplot as plt

# a = np.zeros((2,4))
# print(a)

# b = np.ones((2,4))
# print(b)

# c = np.random.rand(2,3,4)
# print(c)
# g=np.random.rand(10000)

# plt.hist(g,bins=200)
# plt.show()


def matriz(f,c):
    mat = []
    for i in range(f):
        fila = []
        for x in range(c):
            valor=0
            fila.append(valor)
        mat.append(fila)
    return mat

print("la matriz queda: ",matriz(2,2))