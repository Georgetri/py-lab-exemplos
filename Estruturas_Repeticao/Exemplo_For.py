for i in range(0,5): # processamento do [0-4]
    print(i, end=" ")
print("")
for num in range(4,-1,-1):
    print(num, end=" ")

print("")
soma = 0
for num in range(1,6): # Vai de 1 até 5
    soma += num
    print(num, end=" ")
print("\nsoma dos elementos do for:", soma)

palavra = 'sorvete'
for letra in palavra:
    print(letra, end=" ")
    if letra == 'e':
        print("\nAchou a letra E")


for i in range(0,5):
    print(i)
    print("---")
    for j in range(0,3):
        print(j)