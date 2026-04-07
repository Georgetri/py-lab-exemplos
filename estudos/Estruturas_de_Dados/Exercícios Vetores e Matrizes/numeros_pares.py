"""
Faça um programa que leia N números inteiros e armazene-os em um vetor. Em seguida, mostre na
tela todos os números pares, e também a quantidade de números pares.
"""
numeros = []
qtde = 0

num = int(input("Quantos números você vai digitar?"))

for i in range(num):
    valor = int(input(f"Digite o {i+1}º nº: "))
    numeros.append(valor)
    if valor %2 == 0:
        qtde += 1

print("Lista completa:",numeros)

print("Números Pares", end=" ")
for valores in numeros:
    if valores %2 == 0:
        print(valores,end=" ")

print("\nQtde de números pares na lista:",qtde)

# print(*numeros,sep=" ") O operador * desempacota a lista
# print(numeros)
# end=" " substitui o caractere de quebra de linha (\n) que o print coloca automaticamente no final.