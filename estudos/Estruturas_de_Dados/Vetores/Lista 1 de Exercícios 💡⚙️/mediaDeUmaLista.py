"""  Calcular a média de uma lista e exibir os valores quem estão acima dela. """

lista = [4,5,8,7,6]
maiores = []
soma = 0

for i in range(len(lista)): # O i neste caso sempre será o índice
    print(f"\níndice: {i} , dado(int):{lista[i]}", end="")
    soma += lista[i]

media = soma / len(lista)

for valor in lista:
    if valor > media :
        maiores.append(valor)

print()
print("=" * 25)
print(f"Média:{media:.1f}")
print(f"Números maiores que a média {maiores}")
