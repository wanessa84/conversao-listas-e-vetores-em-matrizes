import numpy as np

array = np.array ([0, 1, 2, 3, 4])
lista = [0, 1, 2, 3, 4]
matriz_1 = np.array([lista, lista, lista])
print(matriz_1)
print('----------------')
matriz_2 = np.array([array, array, array])
print(matriz_2)

#---------------------------------

matriz_2 += 3       #Soma com matrizes
print(matriz_2)

matriz_2 -= 1      #subtração com matrizes
print(matriz_2)

matriz_2 *= 3
print(matriz_2)

matriz_2 = matriz_2/2
print(matriz_2)
