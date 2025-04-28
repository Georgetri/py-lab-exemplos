import random

def menu():
    print("\n🎲 MENU - Biblioteca random")
    print("1 - Número aleatório entre 0.0 e 1.0")
    print("2 - Float entre dois valores (uniform)")
    print("3 - Inteiro entre dois valores (randint)")
    print("4 - Número com passo (randrange)")
    print("5 - Sortear item de uma lista (choice)")
    print("6 - Sortear múltiplos com repetição (choices)")
    print("7 - Sortear múltiplos sem repetição (sample)")
    print("8 - Embaralhar lista (shuffle)")
    print("9 - Usar seed (reproduzir sequência)")
    print("10 - Simular moeda")
    print("11 - Simular dado")
    print("12 - Números da Mega-Sena")
    print("13 - Gerar notas aleatórias")
    print("0 - Sair")

def executar_opcao(opcao):
    if opcao == "1":
        print("→ random():", random.random())

    elif opcao == "2":
        a = float(input("Valor mínimo: "))
        b = float(input("Valor máximo: "))
        print("→ uniform():", random.uniform(a, b))

    elif opcao == "3":
        a = int(input("Valor mínimo: "))
        b = int(input("Valor máximo: "))
        print("→ randint():", random.randint(a, b))

    elif opcao == "4":
        inicio = int(input("Início: "))
        fim = int(input("Fim: "))
        passo = int(input("Passo: "))
        print("→ randrange():", random.randrange(inicio, fim, passo))

    elif opcao == "5":
        lista = input("Digite itens separados por vírgula: ").split(",")
        print("→ choice():", random.choice(lista))

    elif opcao == "6":
        lista = input("Digite itens separados por vírgula: ").split(",")
        k = int(input("Quantos sortear? "))
        print("→ choices():", random.choices(lista, k=k))

    elif opcao == "7":
        lista = input("Digite itens separados por vírgula: ").split(",")
        k = int(input("Quantos sortear? (sem repetição) "))
        print("→ sample():", random.sample(lista, k))

    elif opcao == "8":
        lista = input("Digite itens separados por vírgula: ").split(",")
        random.shuffle(lista)
        print("→ shuffle():", lista)

    elif opcao == "9":
        semente = int(input("Digite a semente (número): "))
        random.seed(semente)
        print("→ random.randint(1, 100):", random.randint(1, 100))
        random.seed(semente)
        print("→ Repetindo com mesma seed:", random.randint(1, 100))

    elif opcao == "10":
        print("→ Moeda:", random.choice(["Cara", "Coroa"]))

    elif opcao == "11":
        print("→ Dado:", random.randint(1, 6))

    elif opcao == "12":
        print("→ Mega-Sena:", sorted(random.sample(range(1, 61), 6)))

    elif opcao == "13":
        n = int(input("Quantas notas gerar? "))
        notas = [round(random.uniform(0, 10), 1) for _ in range(n)]
        print("→ Notas:", notas)

    elif opcao == "0":
        print("Saindo...")
        return False
    else:
        print("❌ Opção inválida!")
    return True

# Loop principal
continuar = True
while continuar:
    menu()
    escolha = input("Escolha uma opção: ")
    continuar = executar_opcao(escolha)
