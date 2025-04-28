# Crie um dicionário para armazenar o nome e nota de 3 alunos,
# fazendo a leitura dos valores por meio de uma estrutura de repetiçao
# Depois, crie uma nova estrutura de repetição para somar todas a notas
# e retornar a média

dados = {}
soma = 0.0
media = 0.0

for i in range(3):
    chave = input("Nome do aluno:")
    valor = float(input(f"Nota do aluno {chave}:"))
    dados[chave] = valor

print("Dicionário preenchido:")
for chave, valor in dados.items():
    print(f"{chave}:{valor}")

for valor in dados.values():
    soma += valor

print(f"Soma das notas:{soma}")

media = soma / len(dados)
print("Média das notas:",round(media,2))

# Calculando a média e arredondando para 2 casas decimais
# media = round(soma / 3, 2)

