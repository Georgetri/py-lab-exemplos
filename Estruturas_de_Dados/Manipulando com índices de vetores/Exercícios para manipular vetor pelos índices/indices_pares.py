"""
Dado um vetor de inteiros, crie outro vetor com os índices dos elementos pares.
Exemplo: [4, 7, 2, 9, 10] → [0, 2, 4] Dica: use append(i) quando vetor[i] % 2 == 0.
"""
vetor = [4, 7, 2, 9, 10]
indices = []
for i in range(len(vetor)):
    if vetor[i] %2 == 0:
        indices.append(i)

print(indices)
