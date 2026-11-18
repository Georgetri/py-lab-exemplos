# Inverter uma lista em Python

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
fim = len(x) - 1
# print(len(x)//2)
for i in range(len(x)//2):
    aux = x[fim]
    x[fim] = x[i]
    x[i] = aux
    fim -= 1
print("\nInverter uma lista em Python da maneira mais correta:",x)

