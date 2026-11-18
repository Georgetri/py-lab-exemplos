"""
    Fazer um programa para ler um número inteiro N e depois um vetor de N números reais. Em seguida,
    mostrar na tela a média aritmética de todos elementos com três casas decimais. Depois mostrar todos
    os elementos do vetor que estejam abaixo da média, com uma casa decimal cada.
"""
vetor = []
soma, media, cont = 0,0,0

while True:
    num = int(input("Insira um nº entre 1 e 5 :"))
    if 1 < num <= 5:
        break
    print("⚠️ Número fora do intervalo. Tente novamente.")

for i in range(num):
    valor = float(input(f"Digite o {i+1}º número: "))
    vetor.append(valor)
    soma += valor

print(f"VETOR COMPLETO:{vetor}")
media = soma / num
print(f"Média aritmética:{media:.3f}")

print("Elemento do vetor abaixo da média:", end=" ")
while cont < num:
    if vetor[cont] < media:
        print(f"{vetor[cont]:.1f}", sep=" ")
    cont += 1



