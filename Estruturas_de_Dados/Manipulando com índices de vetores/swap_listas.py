"""
Arquivo: swap_listas.py
Exemplos de troca (swap) entre posições de listas (vetores).
"""

# Exemplo 1: trocar o primeiro e o último elemento
print("Exemplo 1: trocar primeiro e último elemento")
vetor = [10, 20, 30, 40, 50]
print("Antes:", vetor)

vetor[0], vetor[-1] = vetor[-1], vetor[0]

print("Depois:", vetor)
print("-" * 40)

# Exemplo 2: trocar pares de elementos (0↔1, 2↔3, ...)
print("Exemplo 2: trocar pares de elementos (0↔1, 2↔3, ...)")
vetor = [1, 2, 3, 4, 5, 6]
print("Antes:", vetor)

for i in range(0, len(vetor) - 1, 2):
    vetor[i], vetor[i+1] = vetor[i+1], vetor[i]

print("Depois:", vetor)
print("-" * 40)

# Exemplo 3: inversão manual de lista usando swap (início ↔ fim)
print("Exemplo 3: inversão manual de lista")
vetor = [1, 2, 3, 4, 5]
print("Antes:", vetor)

inicio = 0
fim = len(vetor) - 1

while inicio < fim:
    vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]
    inicio += 1
    fim -= 1

print("Depois:", vetor)
print("-" * 40)

# Exemplo 4: garantir que o primeiro seja o menor entre os dois primeiros
print("Exemplo 4: garantir que vetor[0] seja o menor dos dois primeiros")
vetor = [50, 10, 30, 40]
print("Antes:", vetor)

if vetor[0] > vetor[1]:
    vetor[0], vetor[1] = vetor[1], vetor[0]

print("Depois:", vetor)
print("-" * 40)

# Exemplo 5: troca em matriz (lista de listas)
print("Exemplo 5: troca em matriz (lista de listas)")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Antes:")
for linha in matriz:
    print(linha)

# trocar elemento [0][0] com [2][2] (cantos opostos)
matriz[0][0], matriz[2][2] = matriz[2][2], matriz[0][0]

print("Depois da troca [0][0] ↔ [2][2]:")
for linha in matriz:
    print(linha)

print("-" * 40)
