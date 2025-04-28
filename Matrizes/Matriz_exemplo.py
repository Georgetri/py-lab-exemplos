import numpy as np

# Soma entre duas matrizes
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

C = A + B
print(C)
print("------------------------------------")
# Criando um array 1D (como um array em Java)
array = np.array([1, 2, 3, 4, 5])
print(array)

# Soma de todos os elementos
print(np.sum(array))  # Saída: 15

# Multiplicação por um escalar
print(array * 2)  # Saída: [2, 4, 6, 8, 10]
print("-------------------------------------")

# Criando uma matriz 2x3
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

# Acessando um elemento específico
print(matriz[0][1])  # Saída: 2 (primeira linha, segunda coluna)

# Alterando um elemento
matriz[1][2] = 99  # Agora a matriz é [[1, 2, 3], [4, 5, 99]]
print(matriz)

print("\n Este for acessa os elementos da matriz, um por um: ")
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        print(f"Matriz [{i}][{j}]:",matriz[i][j])

print("\nEste for acessa somente as linhas:")
for i in range(matriz.shape[0]):
    print(matriz[i])

print("\n-------------------------------------")
# Criando uma matriz 2x3 com listas de listas
matriz = [
    [1, 2, 3],  # Primeira linha
    [4, 5, 6]   # Segunda linha
]

print("\n Acessando elementos da matriz (coleção)")
print(matriz[0][1])  # Acessa o elemento da primeira linha e segunda coluna (valor 2)
print(matriz[1][2])  # Acessa o elemento da segunda linha e terceira coluna (valor 6)

print("\n Imprimindo a matriz com for")
print("Matriz 2x3:")
for linha in matriz:
    print(linha)
