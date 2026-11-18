"""
    Faça um programa que leia um nº inteiro N (máximo = 10) que definirá o tamanho do vetor
    e depois N números inteiros e armazene-os em um vetor.
     Em seguida, mostrar na tela todos os números negativos lidos.
"""
vetor = []
negativos = 0

# se 1 < num e num for <= 10: números entre 1 e 10
# condição True, entra no while e ativa o break e sai do laço while e vai para a próxima linha de código
while True:
    num = int(input("Digite um número de 1 a 10: "))
    if 1 < num <= 10:
        break
    print("⚠️ Número fora do intervalo. Tente novamente.")


# Preencher o vetor(lista em python)
for i in range(num):
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor.append(valor)


print("Números negativos no vetor: ", end=" ")
for negativos in vetor:
    if negativos < 0:
        print(negativos, end="  ")

print("\nVetor completo:",vetor)


"""
negativos = []

for i in range(num):
    valor = int(input(f"Digite o {i+1}º número: "))
    vetor.append(valor)
    if valor < 0:
        negativos.append(valor)
"""