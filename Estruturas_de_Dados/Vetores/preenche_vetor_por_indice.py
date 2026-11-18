num = int(input("Tamanho do vetor: "))
vetor = [1] * num       # Ex.: Se digitar 3 aqui, o vetor imprime logo abaixo [0,0,0]
print(vetor)
negativos = []

for i in range(num):
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor[i] = valor          # preenche por índice

print(vetor)
