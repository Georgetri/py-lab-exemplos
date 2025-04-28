"""
Created on Sun Apr 27 19:51:11 2025
@author: jorge
"""
def mensagem():
    print("Hello World!")

def mensagemTexto(texto):
    print(texto)

def ler_mensagem(mensagem):
    return input(mensagem)

def ler_decimal(decimal):
    return float(input(decimal))

def soma(a, b):
    print(a + b)

def somar(a, b):
    return a + b

def calcular_energia_potencial_gravitacional(m, h, g=10):
    '''
    :param m: massa
    :param h: altura
    :param g: aceleração gravitacional
    :return: cálculo da energia
    '''
    energia = g * m * h
    return energia


def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Exibir mensagem 'Hello World!'")
    print("2. Exibir mensagem com parâmetro")
    print("3. Ler montadora e número")
    print("4. Somar dois números")
    print("5. Calcular Energia Potencial Gravitacional")
    print("6. Sair")


def menu():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            mensagem()
        elif opcao == '2':
            texto = ler_mensagem("Digite um texto para exibir: ")
            mensagemTexto(texto)
        elif opcao == '3':
            texto = ler_mensagem("Digite a montadora do seu carro: ")
            num = ler_decimal("Digite um número: ")
            print(f"Montadora: {texto}, Número: {num}")
        elif opcao == '4':
            x = ler_decimal("Digite o primeiro número: ")
            y = ler_decimal("Digite o segundo número: ")
            soma(x, y)
        elif opcao == '5':
            m = ler_decimal("Digite a massa (m): ")
            h = ler_decimal("Digite a altura (h): ")
            energia = calcular_energia_potencial_gravitacional(m, h)
            print(f"A Energia Potencial Gravitacional é: {energia} Joules")
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Chama o menu principal
menu()
