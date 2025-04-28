# Dada um matriz, construa uma estrutura de repetição
# para percorrer e somar todos os elementos da matriz
import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 4]])
soma = 0
print("Percorrendo matriz  com For:")
for i in range(matriz.shape[0]):
    print()
    for j in range(matriz.shape[1]):
        print(matriz[i][j], end="  ")
        soma += matriz[i][j]

print("\n-------------------------------")
print("\nPercorrendo matriz com while")
i = 0
while i < matriz.shape[0]:
    j = 0
    print()
    while j < matriz.shape[1]:
        print(matriz[i][j], end="  ")
        # print(f"Matriz [{i}][{j}] : {matriz[i][j]}")
        j += 1
    i += 1

print()
print(f"Soma dos números da matriz: {soma}")