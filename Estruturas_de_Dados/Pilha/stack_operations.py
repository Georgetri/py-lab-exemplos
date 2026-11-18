import numpy as np

class Pilha:
    def __init__(self, capacidade: int):
        if capacidade <= 0:
            raise ValueError("A capacidade da pilha deve ser maior que zero.")

        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_cheia(self) -> bool:
        return self.__topo == self.__capacidade - 1

    def __pilha_vazia(self) -> bool:
        return self.__topo == -1

    def empilhar(self, valor: int) -> bool:
        if self.__pilha_cheia():
            print("A pilha está cheia.")
            return False

        self.__topo += 1
        self.__valores[self.__topo] = valor
        return True

    def desempilhar(self):
        if self.__pilha_vazia():
            print("A pilha está vazia.")
            return None

        valor = int(self.__valores[self.__topo])
        self.__topo -= 1
        return valor

    def ver_topo(self):
        if self.__pilha_vazia():
            print("A pilha está vazia.")
            return None

        return int(self.__valores[self.__topo])

    def tamanho(self) -> int:
        return self.__topo + 1

    def capacidade(self) -> int:
        return self.__capacidade

    def esta_vazia(self) -> bool:
        return self.__pilha_vazia()

    def esta_cheia(self) -> bool:
        return self.__pilha_cheia()

    def listar(self) -> None:
        print("\n" + "=" * 50)
        print("DEBUG DA PILHA")
        print("=" * 50)
        print(f"Capacidade total : {self.__capacidade}")
        print(f"Topo atual       : {self.__topo}")
        print(f"Tamanho atual    : {self.tamanho()}")
        print(f"Está vazia?      : {self.esta_vazia()}")
        print(f"Está cheia?      : {self.esta_cheia()}")
        print("-" * 50)

        if self.__pilha_vazia():
            print("Pilha sem elementos.")
            print("=" * 50)
            return

        print("Elementos válidos da pilha:")
        for indice in range(self.__topo + 1):
            marcador = " <- TOPO" if indice == self.__topo else ""
            valor = int(self.__valores[indice])
            print(f"[índice {indice}] = {valor}{marcador}")

        print("-" * 50)
        print("Visualização lógica (topo -> base):")

        elementos_topo_base = []
        for indice in range(self.__topo, -1, -1):
            elementos_topo_base.append(int(self.__valores[indice]))

        print(elementos_topo_base)
        print("=" * 50)


class InterfacePilha:
    def __init__(self):
        capacidade = self.ler_inteiro_positivo("Digite a capacidade da pilha: ")
        self.pilha = Pilha(capacidade)

    def ler_inteiro(self, mensagem: str) -> int:
        while True:
            try:
                return int(input(mensagem).strip())
            except ValueError:
                print("Digite um número inteiro válido.")

    def ler_inteiro_positivo(self, mensagem: str) -> int:
        while True:
            valor = self.ler_inteiro(mensagem)
            if valor > 0:
                return valor
            print("Digite um número inteiro maior que zero.")

    def mostrar_menu(self) -> None:
        print("\n" + "=" * 40)
        print("MENU DA PILHA")
        print("=" * 40)
        print("1 - Empilhar")
        print("2 - Desempilhar")
        print("3 - Ver topo")
        print("4 - Listar pilha (debug)")
        print("5 - Mostrar tamanho")
        print("6 - Verificar se está vazia")
        print("7 - Verificar se está cheia")
        print("8 - Mostrar capacidade")
        print("0 - Sair")

    def executar(self) -> None:
        while True:
            self.mostrar_menu()
            opcao = input("Escolha uma opção: ").strip()

            match opcao:
                case "1":
                    valor = self.ler_inteiro("Digite o valor para empilhar: ")
                    inserido = self.pilha.empilhar(valor)

                    if inserido:
                        print(f"Valor {valor} empilhado com sucesso.")

                case "2":
                    valor_removido = self.pilha.desempilhar()

                    if valor_removido is not None:
                        print(f"Valor removido: {valor_removido}")

                case "3":
                    topo = self.pilha.ver_topo()

                    if topo is not None:
                        print(f"Topo da pilha: {topo}")

                case "4":
                    self.pilha.listar()

                case "5":
                    print(f"Tamanho atual da pilha: {self.pilha.tamanho()}")

                case "6":
                    print(f"Pilha vazia? {self.pilha.esta_vazia()}")

                case "7":
                    print(f"Pilha cheia? {self.pilha.esta_cheia()}")

                case "8":
                    print(f"Capacidade da pilha: {self.pilha.capacidade()}")

                case "0":
                    print("Encerrando o programa.")
                    break

                case _:
                    print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    interface = InterfacePilha()
    interface.executar()