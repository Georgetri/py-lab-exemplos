# n1 = int(input("Entre com um numero: "))
# n2 = int(input('Entre com outro numero: '))
n1 = 10
n2 = 3
print('Soma: ', n1 + n2)
print('Subtração: ', n1 - n2)
print('Multiplicação: ', n1 * n2)
print('Divisão: ', n1 / n2)
print('Resto da divisão: ', n1 % n2)

print('Um automóvel faz 12km/l, calcular a quantidade de litros de combustível usada na viagem')
tempo = float(input('Tempo gasto na viagem: '))
velocidade = float(input('Velocidade média: '))
distancia = tempo * velocidade
print('Distância percorrida:',distancia, 'km')
combustivel_usado = distancia / 12.0
print('Combustível gasto na viagem:',round(combustivel_usado, 1),'litros')
