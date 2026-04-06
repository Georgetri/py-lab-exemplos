print("🔹 Exemplo: preencher um vetor com 5 números usando WHILE")

vetor = []       # cria a lista vazia
i = 0            # contador começa em 0

while i < 5:     # enquanto i for menor que 5, repete
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor.append(valor)   # adiciona o valor no vetor
    i += 1                # incrementa o contador (passa para o próximo índice)

print("🧱 Vetor completo:", vetor, sep="  ")

print("="*50)   # ====================================================

print("🔹 Exemplo 2: Preencher vetor com tamanho informado pelo usuário (usando WHILE)")

vetor2 = []  # cria a lista vazia
i = 0       # contador inicial

num = int(input("Quantos elementos terá o vetor? "))

while i < num:
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor2.append(valor)
    i += 1  # incrementa o contador

print("🧱 Vetor completo:", vetor2)





