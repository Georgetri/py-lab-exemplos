"""  USAR LISTA COM DICIONÁRIO
    Fazer um programa para ler um conjunto de nomes de pessoas e suas respectivas idades.
    As informações de cada pessoa (nome e idade) devem ser armazenadas em dicionários dentro de uma lista.
    Depois, mostrar na tela o nome da pessoa mais velha.
"""
pessoas = []

while True:
    num = int(input("Quantas pessoas deseja adicionar?, escolha entre [1-3]:  "))
    if 1 < num <= 5:
        break
    print("⚠️ Número fora do intervalo. Tente novamente.")

for i in range(num):
    nome = input(f"Digite o nome da {i+1} pessoa:")
    idade = int(input("Digite a idade da pessoa: "))
    pessoas.append({'nome':nome,'idade':idade})

mais_velha = pessoas[0]
for pessoa in pessoas:
    if pessoa['idade'] > mais_velha['idade']:
        mais_velha = pessoa

print(f"A pessoa mais velha é:{mais_velha['nome']} com {mais_velha['idade']} anos de idade")
