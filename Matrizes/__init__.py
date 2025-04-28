# Importando a biblioteca NumPy, que é usada para trabalhar com arrays e matrizes numéricas
import numpy as np

# Criando uma matriz (array 2D) com 2 linhas e 3 colunas
matriz = np.array([[2, 3, 1],
                   [4, 5, 7]])

# Exibindo a matriz completa
print("Matriz completa:")
print(matriz)

# Exibindo o formato da matriz: (linhas, colunas)
print("\nFormato da matriz (shape):")
print(matriz.shape)  # Resultado: (2, 3)

# Acessando e exibindo cada linha da matriz
print("\nLinha 0:")
print(matriz[0])  # Primeira linha

print("\nLinha 1:")
print(matriz[1])  # Segunda linha

# Acessando elementos individuais da matriz (matriz[linha][coluna])
print("\nElementos da matriz:")
print(f"matriz[0][0] = {matriz[0][0]}")  # 1ª linha, 1ª coluna
print(f"matriz[0][1] = {matriz[0][1]}")  # 1ª linha, 2ª coluna
print(f"matriz[0][2] = {matriz[0][2]}")  # 1ª linha, 3ª coluna
print(f"matriz[1][0] = {matriz[1][0]}")  # 2ª linha, 1ª coluna
print(f"matriz[1][1] = {matriz[1][1]}")  # 2ª linha, 2ª coluna
print(f"matriz[1][2] = {matriz[1][2]}")  # 2ª linha, 3ª coluna

# Tentar acessar matriz[2][0] ou qualquer linha além da 1 vai causar erro
# Portanto, comentamos ou removemos essas linhas:
# print(matriz[2][0])  # ERRO: linha 2 (índice 2) não existe
# print(matriz[2][1])  # ERRO: linha 2 não existe
# print(matriz[2][2])  # ERRO: linha 2 não existe

print("\nPercorrendo a matriz com FOR:")
for i in range(matriz.shape[0]):        # Percorre as linhas
    for j in range(matriz.shape[1]):    # Percorre as colunas
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")


print("\nPercorrendo a matriz com WHILE:")
i = 0
while i < matriz.shape[0]:              # Enquanto houver linhas
    j = 0
    while j < matriz.shape[1]:          # Enquanto houver colunas
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")
        j += 1
    i += 1
