""" Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida:
- Imprimir todos os elementos do vetor
- Mostrar na tela a soma e a média dos elementos do vetor """
soma, numero = 0 , 0
lista = []

while True:
    num = int(input("Entre com um número no intervalo de [0-5]:"))
    if 1 < num <= 5:
        break
    print("⚠️ Número fora do intervalo. Tente novamente.")


for i in range(num):
   numero = float(input(f"Digite o {i+1}º número:"))
   soma += numero

media = soma / num

for valor in lista:
    print(f"Elementos do vetor:{valor}", end=" ")

print(f"Soma dos números do vetor:{soma}")
print(f"Média dos elementos do vetor: {media:.1f}")