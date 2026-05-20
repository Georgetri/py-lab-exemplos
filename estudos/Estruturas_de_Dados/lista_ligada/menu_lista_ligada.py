from lista_ligada import ListaLigada, ElementoUnicoDaLista

class Loja:
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco

    def __repr__(self):
        return "{}\n {}".format(self.__nome, self.__endereco)


def cadastrar_lojas_iniciais(lista):
    loja1 = Loja("Mercadinho do Zé", "Rua das frutas frescas, 1234")
    loja2 = Loja("Direto do colono", "Rua do colono, 10000")
    loja3 = Loja("Quitanda do Bairro", "Rua dos Cebolas, 9999")
    loja4 = Loja("Boa Fruta", "Rua Eureka, 13254")
    loja5 = Loja("Horti Agora", "Rua da Praia, 5464")
    loja6 = Loja("Fruti-Fruti", "Av. dos Verdes, 5")

    lista.inserirNoInicioLista(loja1)
    lista.inserirNoInicioLista(loja2)
    lista.inserirNoInicioLista(loja3)
    lista.inserir(1, loja4)
    lista.inserir(0, loja5)
    lista.inserir(lista.quantidade, loja6)


def criar_loja():
    nome = input("Digite o nome da loja: ")
    endereco = input("Digite o endereço da loja: ")

    return Loja(nome, endereco)


def mostrar_menu():
    print("\n===== MENU LISTA LIGADA =====")
    print("1 - Imprimir lista")
    print("2 - Inserir loja no início")
    print("3 - Inserir loja em uma posição")
    print("4 - Remover loja do início")
    print("5 - Remover loja por posição")
    print("6 - Buscar loja por posição")
    print("7 - Mostrar quantidade")
    print("0 - Sair")


def main():
    lista = ListaLigada()

    cadastrar_lojas_iniciais(lista)

    while True:
        mostrar_menu()

        opcao = int(input("Escolha uma opção: "))

        match opcao:

            case 1:
                print("\nLista de lojas:")
                lista.imprimir()

            case 2:
                loja = criar_loja()
                lista.inserirNoInicioLista(loja)
                print("Loja inserida no início da lista.")

            case 3:
                posicao = int(input("Digite a posição: "))
                loja = criar_loja()
                lista.inserir(posicao, loja)
                print("Loja inserida na posição informada.")

            case 4:
                removido = lista.removerDoInicio()
                print(f"Removido: {removido}")

            case 5:
                posicao = int(input("Digite a posição que deseja remover: "))
                removido = lista.remover(posicao)
                print(f"Elemento removido: {removido}")

            case 6:
                posicao = int(input("Digite a posição que deseja buscar: "))
                elemento = lista.buscaElemento(posicao)
                print(f"Elemento encontrado: {elemento}")

            case 7:
                print(f"Quantidade de elementos: {lista.quantidade}")

            case 0:
                print("Programa encerrado.")
                break

            case _:
                print("Opção inválida.")


main()

