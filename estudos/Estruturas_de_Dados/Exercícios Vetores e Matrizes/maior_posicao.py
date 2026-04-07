"""
    Faça um programa que leia N números reais e armazene-os em um vetor.
    Em seguida, mostrar na tela o maior número do vetor (supor não haver empates).
    Mostrar também a posição do maior elemento, considerando a primeira posição como 0 (zero).
"""
vetor = []
maior = indice = 0

while True:
    num = int(input("Entre com um número inteiro entre [1-5]: "))
    if 1 < num <= 5:           # só para o loop do while quando as condição do if forem verdadeiras
        break
    print("⚠️ Número fora do intervalo. Tente novamente.")

for i in range(num):
    valor = float(input(f"Entre com o {i+1}º número: "))
    vetor.append(valor)
    if valor > maior:
        maior = valor
        indice = i

print("Vetor completo:", end=" ")
for array in vetor:
    print(array, end="  ")

print(f"\nO maior elemento do vetor é o nº {maior} e seu índice é o [{indice}]")
