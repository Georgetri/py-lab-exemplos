total = 0
i = 0
media = 0
notas = 0
while i < 5:
    notas = float(input("Insira a nota:"))
    total += notas
    i += 1
media = total / i
print(media)