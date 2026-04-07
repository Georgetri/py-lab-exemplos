"""
Uma empresa de estatística analisou os 5 melhores jogadores de uma liga profissional de basquete e registrou os pontos,
assistências e rebotes de cada um. Para isso, crie uma lista de tuplas, onde cada tupla é da forma (nome do jogador, pontos,
assistência, rebotes). Ao final, o programa deve percorrer a lista e informar a tupla do jogador que tem as
melhores estatísticas ((pontos+assistências+rebotes)/3)
"""
jogadores = [('Michael Jordan',32292,6533,6672),('Jabbar',38387,5660,17440),('Oscar',49973,6734,12450),
             ('Hortência',12590,3480,4590),('Shaquille O Neal',28596,3026,13099)]

estatistica = []

for dados in jogadores:
    soma = 0
    for i in range(1,4): # inicia índice 1 para pegar apenas números
        soma += dados[i]
    media = round(soma/3)
    estatistica.append((dados[0],media))

melhor = estatistica[0]
for item in estatistica:
    if item[1] > melhor[1]:
        melhor = item

print(estatistica)
print(f"Melhor estatística é do jogador {melhor[0]} com média de {melhor[1]}")

