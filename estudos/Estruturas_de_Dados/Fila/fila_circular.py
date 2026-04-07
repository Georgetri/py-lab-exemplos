import numpy as np

class FilaCircular:

    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1     # É uma forma simples e eficiente de indicar que a fila ainda não possui nenhum elemento, e que o próximo elemento será inserido na posição 0 (final + 1).
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self,valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return
        if self.final == self.capacidade -1: # Aqui a capacidade e final são ponteiros dos índices, que é sempre -1 ex: capacidade = 5, índices 0,1,2,3,4
            self.final = -1
        self.final += 1
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila já está vazia')
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:
            self.inicio = 0
        self.numero_elementos -= 1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]

    def mostrar(self):
        if self.__fila_vazia():
            print('Fila está vazia')
            return
        print('Elementos da fila:',end=' ')
        indice = self.inicio
        for i in range(self.numero_elementos):
            print(self.valores[indice], end=' ')
            indice = (indice + 1) % self.capacidade
        print()  # Para pular linha ao final


fila = FilaCircular(5)
# print(fila.primeiro())
fila.enfileirar(1)
print(fila.primeiro())

fila.enfileirar(2)
print(fila.primeiro())

fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
# fila.enfileirar(6)

fila.mostrar()

fila.desenfileirar()
fila.desenfileirar()
print(fila.primeiro())
fila.mostrar()

fila.enfileirar(6)
fila.enfileirar(7)
fila.primeiro()
fila.mostrar()
print(fila.valores)
print(fila.valores[fila.final])
print(fila.valores[fila.inicio])













