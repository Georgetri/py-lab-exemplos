"""
    EXEMPLOS DE COMO IMPRIMIR VETORES DE MÚLTIPLAS FORMAS
    Autor: Jorge Luis
    Descrição: Demonstra três formas diferentes de imprimir vetores em Python:
    1. Forma Pythonica (usando desempacotamento *)
    2. Usando laço FOR
    3. Usando laço WHILE
"""
# -------------------------------------------
# 🧮 Dados de exemplo
# -------------------------------------------
vetor_a = [1, 2, 3]
vetor_b = [4, 5, 6]
vetor_c = [5, 7, 9]
num = len(vetor_a)

# -------------------------------------------
# 1️⃣ Forma Pythonica (simples e elegante)
# -------------------------------------------
print("=== IMPRESSÃO PYTHONICA ===")
print("VETOR A:", *vetor_a)
print("VETOR B:", *vetor_b)
print("VETOR C:", *vetor_c)
print("-" * 40)

# -------------------------------------------
# 2️⃣ Forma com FOR
# -------------------------------------------
print("=== IMPRESSÃO COM FOR ===")

print("VETOR A:", end=" ")
for elemento in vetor_a:
    print(elemento, end=" ")
print()

print("VETOR B:", end=" ")
for elemento in vetor_b:
    print(elemento, end=" ")
print()

print("VETOR C:", end=" ")
for elemento in vetor_c:
    print(elemento, end=" ")
print()
print("-" * 40)

# -------------------------------------------
# 3️⃣ Forma com WHILE
# -------------------------------------------
print("=== IMPRESSÃO COM WHILE ===")
i = 0
print("VETOR A:", end=" ")
while i < num:
    print(vetor_a[i], end=" ")
    i += 1
print()

i = 0
print("VETOR B:", end=" ")
while i < num:
    print(vetor_b[i], end=" ")
    i += 1
print()

i = 0
print("VETOR C:", end=" ")
while i < num:
    print(vetor_c[i], end=" ")
    i += 1
print()

print("-" * 40)
print("🚗 Fim do programa — 3 formas de imprimir vetores demonstradas com sucesso!")
