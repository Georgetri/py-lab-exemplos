"""
    Tem-se um conjunto de dados contendo a altura e o gênero (M, F) de N pessoas.
    Fazer um programa que calcule e escreva a maior e a menor altura do grupo,
    a média de altura das mulheres, e o número de homens.
"""

pessoas = [
    {"altura": 1.70, "genero": "F"},
    {"altura": 1.83, "genero": "M"},
    {"altura": 1.54, "genero": "M"},
    {"altura": 1.61, "genero": "F"},
    {"altura": 1.75, "genero": "F"}
]

for i, pessoa in enumerate(pessoas, start=1):
    print(f"{i}ª pessoa → Altura: {pessoa['altura']:.2f}m "
          f" Gênero: {pessoa['genero']}")


maior = menor = pessoas[0]

for pessoa in pessoas:
    if pessoa['altura'] > maior['altura']:
        maior = pessoa
    elif pessoa['altura'] < menor['altura']:
        menor = pessoa


print("="*40)
print(f"A maior altura é {maior['altura']}m")
print(f"A menor altura é {menor['altura']}m")
