import numpy as np

class Pilha:
    def __init__(self,capacidade): # dois traços __ define como privado
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade,dtype=int)


    def __pilha_cheia(self):
        if self.__topo == self.__capacidade -1:
            return True
        else:
            return False


    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False


    def empilhar(self,valor):
        if self.__pilha_cheia():
            print('A pílha está cheia')
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor


    def desempilhar(self):
        if self.__pilha_vazia():
            print('A pilha está vazia')
            return None
        valor = self.__valores[self.__topo]
        self.__topo -= 1
        return valor


    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1

'''

# =========================
#         TESTES 
# =========================

pilha = Pilha(5)
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)
pilha.empilhar(6)  # Pilha está cheia
print('Topo da pilha:', pilha.ver_topo())  # Deve mostrar 5
print('Valor removido:', pilha.desempilhar())
print('Topo da pilha:', pilha.ver_topo())  # Deve mostrar 4
print('Valor removido:', pilha.desempilhar())
print('Valor removido:', pilha.desempilhar())
print('Valor removido:', pilha.desempilhar())
print('Topo da pilha:', pilha.ver_topo())  # Deve mostrar 1
print('Valor removido:', pilha.desempilhar())
print('Topo da pilha:', pilha.ver_topo())  # Pilha vazia → -1
print('Valor removido:', pilha.desempilhar())

'''






