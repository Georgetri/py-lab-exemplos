
negativos = int(input("Quantos números você quer? "))
inteiros = []
i=0

print( i < negativos , " i é menor que negativos") # Se for True entra no while
print( i > negativos, " i é maior que negativos") # Se for False não entra no while e termina o programa

while i < negativos:
    inteiros.append(int(input("Digite um número: ")))
    i+= 1

for num in inteiros:
  if num < 0:
   print("Nº negativo:",num)
