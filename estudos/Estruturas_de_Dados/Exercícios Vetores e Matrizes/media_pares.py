"""
    Fazer um programa para ler um vetor de N números inteiros. Em seguida, mostrar na tela a média
    aritmética somente dos números pares lidos, com uma casa decimal. Se nenhum número par for
    digitado, mostrar a mensagem "NENHUM NUMERO PAR"
"""
vetor = []
total_pares = 0
cont_pares = 0
while True:
    num = int(input("Digite um número entre [1-5]:"))
    if 1 < num <= 5:
        break
    print("⚠️ Número fora do intervalo. Tente novamente.")

for i in range(num):
    valor = float(input(f"Digite o {i+1}º número:"))
    vetor.append(valor)
    if vetor[i] %2 == 0:
        total_pares += vetor[i]
        cont_pares += 1

if cont_pares == 0:
    print("NENHUM NÚMERO PAR")
else:
    print(f"Média aritmética dos números pares:{total_pares/cont_pares}")