# Dicionário inicial com espécies e quantidades
coleta = {
    'mosquito': 32,
    'aranha': 7,
    'morcego': 2
}

# Função para exibir o menu
def mostrar_menu():
    print("\n===== MENU DE COLETA =====")
    print("1. Consultar espécie")
    print("2. Adicionar/Atualizar espécie")
    print("3. Remover espécie")
    print("4. Listar todas as espécies")
    print("5. Sair")

# Loop principal do programa
while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        especie = input("Digite o nome da espécie: ")
        if especie in coleta:
            print(f"{especie}: {coleta[especie]} espécimes")
        else:
            print(f"Espécie '{especie}' não encontrada.")

    elif escolha == '2':
        especie = input("Digite o nome da espécie: ")
        quantidade = int(input("Digite a quantidade: "))
        coleta[especie] = quantidade
        print(f"Espécie '{especie}' registrada com {quantidade} espécimes.")

    elif escolha == '3':
        especie = input("Digite o nome da espécie para remover: ")
        if especie in coleta:
            del coleta[especie]
            print(f"Espécie '{especie}' removida.")
        else:
            print(f"Espécie '{especie}' não encontrada.")

    elif escolha == '4':
        if coleta:
            print("\nEspécies coletadas:")
            for especie, quantidade in coleta.items():
                print(f"- {especie}: {quantidade} espécimes")
        else:
            print("Nenhuma espécie registrada.")

    elif escolha == '5':
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
