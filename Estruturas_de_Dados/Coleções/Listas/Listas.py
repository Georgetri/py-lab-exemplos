lista1 = ['homo sapiens','canis familiaris', 'felis catus']
print(lista1)

lista2 = ['xenopus laevis', 'Ailuropoda melanoleuca']
print(lista2)

l2_2 = lista2 * 2
print(l2_2)

lista3 = lista1 + lista2
print(lista3)

print(lista1[0], lista1[1])
print(lista1[0:2])
lista1.append('Gorila gorila')
print(lista1)

lista1.remove('felis catus')
print(lista1)

for item in l2_2:
    print(item)


