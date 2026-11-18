''' SOMA DOS ELEMENTOS DE UM VETOR
    Faça um programa que leia um vetor de N números inteiros e mostre a soma dos elementos do vetor. '''

n = int(input("Digite a quantidade de elementos do vetor: "))
vetor = []
soma = 0
for i in range(n):
    elemento = int(input(f"Digite o elemento {i + 1}º: "))
    vetor.append(elemento)
    soma += elemento    

print(f"A soma dos elementos do vetor é: {soma}")
print("*" * 40 )

# =======================================================================================

# Função para somar os elementos de um vetor

def soma_vetor(vetor):
    soma = 0
    for elemento in vetor:
        soma += elemento
    return soma

# Exemplo de uso da função soma_vetor
vetor_exemplo = [1, 2, 3, 4, 5]
resultado = soma_vetor(vetor_exemplo)  
print(f"A soma dos elementos do vetor exemplo é: {resultado}")     
print("*" * 40 )

# ======================================================================================

def somar_vetor(vetor: list[int]) -> int: #Aqui dá pra colocar quantos nºs inteiros quiser
    soma = 0
    for x in vetor:
        soma += x
    return soma

vetor_teste = [10, 20, 30, 40, 50]
print(f"A soma dos elementos do vetor de teste é: {somar_vetor(vetor_teste)}")
