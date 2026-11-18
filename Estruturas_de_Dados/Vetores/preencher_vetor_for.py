
print("🔹 Exemplo 1: Preencher vetor com tamanho informado pelo usuário (usando FOR)")

vetor = []  # cria a lista vazia

num = int(input("Quantos elementos terá o vetor? "))

for i in range(num):  # repete conforme o número informado
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor.append(valor)  # adiciona o número na lista

print("🧱 Vetor completo:", vetor, sep="  ")

print("=" * 40)   # ============================================

print("🔹 Exemplo 2: preencher um vetor com 5 números usando FOR")

vetor2 = []  # cria a lista vazia

for i in range(5):  # repete 5 vezes (índices: 0, 1, 2, 3, 4)
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor2.append(valor)  # adiciona o valor na lista

print("🧱 Vetor completo:", vetor2, end="  ")



