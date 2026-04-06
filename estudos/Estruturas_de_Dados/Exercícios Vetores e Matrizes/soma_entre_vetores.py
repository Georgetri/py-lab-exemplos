"""
    Faça um programa para ler dois vetores A e B, contendo N elementos cada. Em seguida, gere um
    terceiro vetor C onde cada elemento de C é a soma dos elementos correspondentes de A e B. Imprima
    o vetor C gerado.
"""
# vetor_a = vetor_b = vetor_c = []  ⚠️ Errado: cria apenas UMA lista compartilhada
# ✅ Certo: cria três listas independentes -> vetor_a, vetor_b, vetor_c = [], [], []
vetor_a = []
vetor_b = []
vetor_c = []

while True:
    num = int(input("Escolha o tamanho dos vetores dentro deste intervalo [1-5]: "))  # 0
    if 1 < num <= 5:            # Se as 2 condições forem verdadeiras o programa entra no if e break: Sai do loop
        break
    print("⚠️ Número fora do intervalo. Tente novamente.")


print("Preenchendo o vetor A :")
for i in range(num):
    valor_a = int(input(f"Insira o {i+1} elemento: "))
    vetor_a.append(valor_a)

print("-" * 40)

i = 0
print("Preenchendo o vetor B:")
while i < num:
    valor_b = int(input(f"Insira o {i+1} elemento:"))
    vetor_b.append(valor_b)
    i += 1

print("-" * 40)

# SOMA DOS VETORES A e B, JUNTO COM A INSERÇÃO DO RESULTADO NO VETOR C
for i in range(0,num,1):
    valor_c = vetor_a[i] + vetor_b[i]
    vetor_c.append(valor_c)

# 💡 Em Python, variáveis criadas dentro de laços (for ou while) pertencem ao escopo global do programa,
# não a um escopo local. Ou seja, continuam acessíveis após o término do laço.

# IMPRIME TODOS OS VETORES
# -------------------------------------------
#  Forma Pythonica (simples e elegante)
# -------------------------------------------
print("1️⃣ IMPRESSÃO PYTHONICA ")
print("VETOR A:", *vetor_a)
print("VETOR B:", *vetor_b)
print("VETOR C:", *vetor_c)
print("-" * 40)

# -------------------------------------------
#  Forma com FOR
# -------------------------------------------
print("2️⃣ IMPRESSÃO COM FOR ")
print("VETOR A:", end=" ")
for elemento in vetor_a:
    print(elemento, end=" ")
print()  # quebra de linha

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
#  Forma com WHILE
# -------------------------------------------
print("3️⃣ IMPRESSÃO COM WHILE ")
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


