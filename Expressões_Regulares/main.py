from Analise_Extração_Texto import menu_analise_texto


def menu_principal():
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1 - Análise e Extração de Texto")
        print("0 - Sair")

        escolha = input("Escolha o número da categoria: ")

        if escolha == "1":
            menu_analise_texto()  # Chama o menu da Análise e Extração de Texto
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente!")


if __name__ == "__main__":
    menu_principal()  # Inicia o menu principal
