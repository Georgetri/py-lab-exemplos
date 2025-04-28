import numpy as np  # Importa a biblioteca NumPy, usada para manipular matrizes e arrays numéricos


# Função para criar uma matriz com entrada do usuário
def criar_matriz(nome):
    # Solicita o número de linhas da matriz
    linhas = int(input(f"\nDigite o número de linhas da matriz {nome}: "))

    # Solicita o número de colunas
    colunas = int(input(f"Digite o número de colunas da matriz {nome}: "))

    # Instruções para o usuário inserir os elementos da matriz
    print(f"Digite os elementos da matriz {nome} linha por linha (separados por espaço):")
    matriz = []  # Lista vazia que vai receber as linhas da matriz

    for i in range(linhas):
        # Solicita a entrada de cada linha separada por espaço
        linha = input(f"Linha {i + 1}: ").split()

        # Converte todos os elementos da linha de string para inteiro
        linha = [int(x) for x in linha]

        # Verifica se a quantidade de elementos na linha está correta
        if len(linha) != colunas:
            print("Número de elementos incorreto. Tente novamente.")
            return criar_matriz(nome)  # Reinicia a criação da matriz se algo estiver errado

        matriz.append(linha)  # Adiciona a linha validada à matriz

    return np.array(matriz)  # Converte a lista de listas para um array NumPy e retorna


# Loop principal do menu
while True:
    # Exibe as opções do menu
    print("\n=== MENU ===")
    print("1. Criar e somar duas matrizes")
    print("2. Criar e multiplicar duas matrizes")
    print("3. Sair")

    # Recebe a escolha do usuário
    escolha = input("Escolha uma opção: ")

    # Opção 1: Soma de matrizes
    if escolha == '1':
        A = criar_matriz("A")  # Cria a matriz A
        B = criar_matriz("B")  # Cria a matriz B

        # Verifica se as matrizes têm o mesmo formato (shape)
        if A.shape == B.shape:
            print("\nResultado da soma:")
            print(A + B)  # Soma as duas matrizes elemento a elemento
        else:
            print("\n❌ As matrizes têm formatos diferentes e não podem ser somadas.")

    # Opção 2: Multiplicação de matrizes
    elif escolha == '2':
        A = criar_matriz("A")
        B = criar_matriz("B")

        # Verifica se o número de colunas de A é igual ao número de linhas de B
        if A.shape[1] == B.shape[0]:
            print("\nResultado da multiplicação:")
            print(np.dot(A, B))  # Multiplicação de matrizes (produto matricial)
        else:
            print("\n❌ As matrizes não podem ser multiplicadas (colunas de A ≠ linhas de B).")

    # Opção 3: Sair do programa
    elif escolha == '3':
        print("Programa encerrado.")
        break  # Encerra o loop e o programa

    # Caso o usuário digite algo inválido
    else:
        print("Opção inválida. Tente novamente.")
