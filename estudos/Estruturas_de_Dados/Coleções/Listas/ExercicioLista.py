# Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros
# e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição
# para somar os valores digitados

lista = []
soma = 0

for i in range(0,5):
    num = int(input(f"Digite o  {i+1}º numero:"))
    lista.append(num)

i = 0
while i < 5:
    soma += lista[i]
    i += 1

print("Números da lista: ")
for num in lista:
    print(num, end=" ")

print("\nSoma dos números da lista: ", soma)


# i = 0
# while i < 5:
#     num = int(input(f"Digite o {i+1}º número: "))
#     lista.append(num)
#     i += 1
#
# print("\nNúmeros digitados:")
# i = 0
# while i < len(lista):
#     print(lista[i], end=" ")
#     i += 1