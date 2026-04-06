# tuplas são imutáveis
tupla = ('homo sapiens','canis familiaris', 'felis catus')
print(tupla)
print("índice", tupla.index('homo sapiens'),":",tupla[0])
print("índice", tupla.index('canis familiaris'),":", tupla[1])
print("índice", tupla.index('felis catus'),":", tupla[2])
print()
for elemento in tupla:
    print("Elemento:",elemento)