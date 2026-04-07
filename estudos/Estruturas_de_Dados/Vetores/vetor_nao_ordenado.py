import numpy as np

class vetorNaoOrdenado:

    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = - 1
        self.valores = np.empty(self.capacidade,dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i," - ",self.valores[i])
    # O(1)
    def insere(self,valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Capacidade máxima atingida")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    # O(n)
    def pesquisar(self,valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    # O(n)
    def excluir(self,valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao,self.ultima_posicao):
                self.valores[i] = self.valores[i+1]
            self.ultima_posicao -= 1


    def menu(self):
        print(" ===  MENU  ===")
        print("Opção 1 : Inserir elementos no vetor")
        print("Opção 2 : Imprimir o vetor")
        print("Opção 3 : pesquisar elementos no vetor")
        print("Opção 4 : Deletar elemento do vetor")
        print("Opção 0 : Sair... ")


vetor = vetorNaoOrdenado(5)
print("Vetor:",vetor)

while True:

    vetor.menu()
    opcao = int(input("Escolha a opção:"))

    match opcao:

        case 1:
            num = int(input("Digite o nº para inserir: "))
            vetor.insere(num)
        case 2:
            vetor.imprime()
            print("="*20)
        case 3:
            num = int(input("Digite o nº para pesquisar: "))
            posicao = vetor.pesquisar(num)

            if posicao == -1:
                print(f"O valor {num} NÃO foi encontrado no vetor.")
            else:
                print(f"O valor {num} foi encontrado na posição {posicao}.")
        case 4:
            num = int(input("Digite o nº para deletar: "))
            vetor.excluir(num)
        case 0:
            print("Saindo do programa...")
            break
        case _:
            print("Digite um número válido!")
