class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.cabeca is None

    def inserir_no_inicio(self, valor):
        novo_no = No(valor)

        if self.esta_vazia():
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no

        self.tamanho += 1

    def inserir_no_fim(self, valor):
        novo_no = No(valor)

        if self.esta_vazia():
            self.cabeca = novo_no
            self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no
            self.cauda = novo_no

        self.tamanho += 1

    def remover_do_inicio(self):
        if self.esta_vazia():
            raise IndexError("A lista encadeada está vazia.")

        valor_removido = self.cabeca.valor
        self.cabeca = self.cabeca.proximo

        if self.cabeca is None:
            self.cauda = None

        self.tamanho -= 1
        return valor_removido

    def remover_do_fim(self):
        if self.esta_vazia():
            raise IndexError("A lista encadeada está vazia.")

        if self.cabeca == self.cauda:
            valor_removido = self.cabeca.valor
            self.cabeca = None
            self.cauda = None
            self.tamanho -= 1
            return valor_removido

        atual = self.cabeca
        while atual.proximo != self.cauda:
            atual = atual.proximo

        valor_removido = self.cauda.valor
        atual.proximo = None
        self.cauda = atual
        self.tamanho -= 1
        return valor_removido

    def buscar(self, valor):
        atual = self.cabeca

        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo

        return False

    def listar(self):
        elementos = []
        atual = self.cabeca

        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        return elementos

    def obter_tamanho(self):
        return self.tamanho


class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.topo is None

    def empilhar(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self.tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")

        valor_removido = self.topo.valor
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return valor_removido

    def espiar(self):
        if self.esta_vazia():
            raise IndexError("A pilha está vazia.")

        return self.topo.valor

    def listar(self):
        elementos = []
        atual = self.topo

        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        return elementos

    def obter_tamanho(self):
        return self.tamanho


class Fila:
    def __init__(self):
        self.frente = None
        self.tras = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.frente is None

    def enfileirar(self, valor):
        novo_no = No(valor)

        if self.esta_vazia():
            self.frente = novo_no
            self.tras = novo_no
        else:
            self.tras.proximo = novo_no
            self.tras = novo_no

        self.tamanho += 1

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia.")

        valor_removido = self.frente.valor
        self.frente = self.frente.proximo

        if self.frente is None:
            self.tras = None

        self.tamanho -= 1
        return valor_removido

    def primeiro(self):
        if self.esta_vazia():
            raise IndexError("A fila está vazia.")

        return self.frente.valor

    def listar(self):
        elementos = []
        atual = self.frente

        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        return elementos

    def obter_tamanho(self):
        return self.tamanho


class InterfaceEstruturas:
    def __init__(self):
        self.lista_encadeada = ListaEncadeada()
        self.pilha = Pilha()
        self.fila = Fila()

    def exibir_menu_principal(self):
        print("\n" + "=" * 50)
        print("        SISTEMA DE ESTRUTURAS DE DADOS")
        print("=" * 50)
        print("1 - Lista Encadeada")
        print("2 - Pilha")
        print("3 - Fila")
        print("0 - Sair")

    def exibir_menu_lista_encadeada(self):
        print("\n" + "-" * 50)
        print("MENU - LISTA ENCADEADA")
        print("-" * 50)
        print("1 - Inserir no início")
        print("2 - Inserir no fim")
        print("3 - Remover do início")
        print("4 - Remover do fim")
        print("5 - Buscar valor")
        print("6 - Listar elementos")
        print("7 - Mostrar tamanho")
        print("8 - Verificar se está vazia")
        print("0 - Voltar ao menu principal")

    def exibir_menu_pilha(self):
        print("\n" + "-" * 50)
        print("MENU - PILHA")
        print("-" * 50)
        print("1 - Empilhar")
        print("2 - Desempilhar")
        print("3 - Espiar topo")
        print("4 - Listar elementos")
        print("5 - Mostrar tamanho")
        print("6 - Verificar se está vazia")
        print("0 - Voltar ao menu principal")

    def exibir_menu_fila(self):
        print("\n" + "-" * 50)
        print("MENU - FILA")
        print("-" * 50)
        print("1 - Enfileirar")
        print("2 - Desenfileirar")
        print("3 - Consultar primeiro")
        print("4 - Listar elementos")
        print("5 - Mostrar tamanho")
        print("6 - Verificar se está vazia")
        print("0 - Voltar ao menu principal")

    def executar(self):
        while True:
            self.exibir_menu_principal()
            opcao = input("Escolha uma opção: ").strip()

            match opcao:
                case "1":
                    self.executar_lista_encadeada()
                case "2":
                    self.executar_pilha()
                case "3":
                    self.executar_fila()
                case "0":
                    print("Encerrando o sistema.")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")

    def executar_lista_encadeada(self):
        while True:
            self.exibir_menu_lista_encadeada()
            opcao = input("Escolha uma operação: ").strip()

            try:
                match opcao:
                    case "1":
                        valor = input("Digite o valor para inserir no início: ")
                        self.lista_encadeada.inserir_no_inicio(valor)
                        print("Valor inserido com sucesso.")

                    case "2":
                        valor = input("Digite o valor para inserir no fim: ")
                        self.lista_encadeada.inserir_no_fim(valor)
                        print("Valor inserido com sucesso.")

                    case "3":
                        removido = self.lista_encadeada.remover_do_inicio()
                        print(f"Valor removido do início: {removido}")

                    case "4":
                        removido = self.lista_encadeada.remover_do_fim()
                        print(f"Valor removido do fim: {removido}")

                    case "5":
                        valor = input("Digite o valor para buscar: ")
                        encontrado = self.lista_encadeada.buscar(valor)
                        if encontrado:
                            print("Valor encontrado na lista encadeada.")
                        else:
                            print("Valor não encontrado na lista encadeada.")

                    case "6":
                        elementos = self.lista_encadeada.listar()
                        print(f"Elementos da lista encadeada: {elementos}")

                    case "7":
                        print(f"Tamanho da lista encadeada: {self.lista_encadeada.obter_tamanho()}")

                    case "8":
                        print(f"Lista encadeada vazia? {self.lista_encadeada.esta_vazia()}")

                    case "0":
                        break

                    case _:
                        print("Opção inválida. Tente novamente.")

            except IndexError as erro:
                print(f"Erro: {erro}")
            except Exception as erro:
                print(f"Erro inesperado: {erro}")

    def executar_pilha(self):
        while True:
            self.exibir_menu_pilha()
            opcao = input("Escolha uma operação: ").strip()

            try:
                match opcao:
                    case "1":
                        valor = input("Digite o valor para empilhar: ")
                        self.pilha.empilhar(valor)
                        print("Valor empilhado com sucesso.")

                    case "2":
                        removido = self.pilha.desempilhar()
                        print(f"Valor desempilhado: {removido}")

                    case "3":
                        topo = self.pilha.espiar()
                        print(f"Topo da pilha: {topo}")

                    case "4":
                        elementos = self.pilha.listar()
                        print(f"Elementos da pilha: {elementos}")

                    case "5":
                        print(f"Tamanho da pilha: {self.pilha.obter_tamanho()}")

                    case "6":
                        print(f"Pilha vazia? {self.pilha.esta_vazia()}")

                    case "0":
                        break

                    case _:
                        print("Opção inválida. Tente novamente.")

            except IndexError as erro:
                print(f"Erro: {erro}")
            except Exception as erro:
                print(f"Erro inesperado: {erro}")

    def executar_fila(self):
        while True:
            self.exibir_menu_fila()
            opcao = input("Escolha uma operação: ").strip()

            try:
                match opcao:
                    case "1":
                        valor = input("Digite o valor para enfileirar: ")
                        self.fila.enfileirar(valor)
                        print("Valor enfileirado com sucesso.")

                    case "2":
                        removido = self.fila.desenfileirar()
                        print(f"Valor desenfileirado: {removido}")

                    case "3":
                        primeiro = self.fila.primeiro()
                        print(f"Primeiro da fila: {primeiro}")

                    case "4":
                        elementos = self.fila.listar()
                        print(f"Elementos da fila: {elementos}")

                    case "5":
                        print(f"Tamanho da fila: {self.fila.obter_tamanho()}")

                    case "6":
                        print(f"Fila vazia? {self.fila.esta_vazia()}")

                    case "0":
                        break

                    case _:
                        print("Opção inválida. Tente novamente.")

            except IndexError as erro:
                print(f"Erro: {erro}")
            except Exception as erro:
                print(f"Erro inesperado: {erro}")


if __name__ == "__main__":
    sistema = InterfaceEstruturas()
    sistema.executar()