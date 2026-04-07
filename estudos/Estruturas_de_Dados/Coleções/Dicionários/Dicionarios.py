# Informando sobre o uso de dicionários
print("\nDicionários trabalham com chave e valor")

# Criando um dicionário com espécies e suas quantidades
coleta = {'mosquito': 32, 'aranha': 7, 'morcego': 2}

# Acessando valores individuais por suas chaves
print(coleta['aranha'])   # Mostra a quantidade de aranhas
print(coleta['morcego'])  # Mostra a quantidade de morcegos

# Adicionando uma nova espécie ao dicionário
coleta['lagarto'] = 11
print(coleta)             # Mostra o dicionário atualizado

# Removendo uma espécie (chave) do dicionário
del coleta['mosquito']
print(coleta)             # Mostra o dicionário após remoção

# Exibindo os itens, chaves e valores do dicionário
print(coleta.items())     # Retorna todos os pares chave:valor
print(coleta.keys())      # Retorna apenas as chaves
print(coleta.values())    # Retorna apenas os valores

# Criando outro dicionário com mais espécies
coleta2 = {'cobra': 5, 'gambá': 3, 'sapo': 8}

# Atualizando o primeiro dicionário com o segundo
coleta.update(coleta2)
print(coleta)             # Mostra o dicionário após a atualização

# Iterando sobre os itens do dicionário para exibir os dados de forma formatada
for especie, quantidade in coleta.items():
    print(f'Espécie: {especie}, número desta espécime: {quantidade}')

# Criando uma tupla com biomoléculas (com repetições)
biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidrato',
                'lipídeo', 'proteína', 'ácidos nucleicos', 'carboidrato')
print(biomoleculas)  # Mostra todas as biomoléculas, incluindo repetidas

# Utilizando função set para eliminar duplicatas
print('Set traz os elementos sem os repetir')
print(set(biomoleculas))  # Mostra apenas elementos únicos

# Criando o primeiro conjunto com elementos únicos
conj1 = {1, 2, 3, 4, 5}

# Criando o segundo conjunto
conj2 = {3, 4, 5, 6, 7}

# A operação 'intersection' retorna os elementos que estão em *ambos* os conjuntos
conj3 = conj1.intersection(conj2)
print(conj3)  # Resultado: {3, 4, 5}

# A operação 'difference' retorna os elementos que estão em conj1 mas *não* em conj2
print(conj1.difference(conj2))  # Resultado: {1, 2}

# A operação 'difference' agora no sentido inverso: elementos em conj2 que não estão em conj1
print(conj2.difference(conj1))  # Resultado: {6, 7}



print("\n---------------------------------------------------------\n")

carro = {"marca": "Ford", "ano": 2020}
print(carro["marca"])  # Resultado: Ford

carro["cor"] = "preto" # Adiciona uma nova chave
print(carro)           # {'marca': 'Ford', 'ano': 2020, 'cor': 'preto'}
