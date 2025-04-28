numero = -1
num = 1
soma = 0

while numero < 1 or numero > 10:
     numero = int(input("Digite um número de [1-10]:"))
print("----------")

while num < 6:
    print(num, end=" ")
    soma += num
    num += 1
print("\nSoma dos números:",soma)

numero = -1
while numero < 1 or numero > 10:
    numero = int(input("Digite um número de 1 a 10:"))