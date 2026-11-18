# Inverter uma lista em Python

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
fim = len(x) - 1

print("\nInverter uma lista em Python da maneira mais correta:")

for i in range(len(x)//2):
    aux = x[fim]
    x[fim] = x[i]
    x[i] = aux
    fim -= 1
print(*x)
print("\n-------------------------------------------------------")

y = []

for i in range(len(x)-1, -1, -1):
    y.append(x[i])

print('')
print(y)
# Output: [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def inverter_lista(lista):
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

print(inverter_lista(x))
# Output: [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def inverter_lista_com_slicing(lista):
    return lista[::-1]

print(inverter_lista_com_slicing(x))
# Output: [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

