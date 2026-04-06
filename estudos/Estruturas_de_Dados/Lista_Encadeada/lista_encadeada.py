from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterator, Optional, TypeVar


T = TypeVar("T")

@dataclass
class No(Generic[T]):
    valor: T
    proximo: Optional["No[T]"] = None


class ListaEncadeada(Generic[T]):
    def __init__(self) -> None:
        self._cabeca: Optional[No[T]] = None
        self._cauda: Optional[No[T]] = None
        self._tamanho: int = 0

    def esta_vazia(self) -> bool:
        return self._cabeca is None

    def tamanho(self) -> int:
        return self._tamanho

    def inserir_no_inicio(self, valor: T) -> None:
        novo_no = No(valor=valor, proximo=self._cabeca)
        self._cabeca = novo_no

        if self._cauda is None:
            self._cauda = novo_no

        self._tamanho += 1

    def inserir_no_fim(self, valor: T) -> None:
        novo_no = No(valor=valor)

        if self._cauda is None:
            self._cabeca = novo_no
            self._cauda = novo_no
        else:
            self._cauda.proximo = novo_no
            self._cauda = novo_no

        self._tamanho += 1

    def inserir_em(self, indice: int, valor: T) -> None:
        if indice < 0 or indice > self._tamanho:
            raise IndexError("Índice fora do intervalo.")

        if indice == 0:
            self.inserir_no_inicio(valor)
            return

        if indice == self._tamanho:
            self.inserir_no_fim(valor)
            return

        anterior = self._cabeca
        for _ in range(indice - 1):
            if anterior is None:
                raise IndexError("Índice inválido.")
            anterior = anterior.proximo

        if anterior is None:
            raise IndexError("Índice inválido.")

        novo_no = No(valor=valor, proximo=anterior.proximo)
        anterior.proximo = novo_no
        self._tamanho += 1

    def remover_do_inicio(self) -> T:
        if self._cabeca is None:
            raise IndexError("Não é possível remover de uma lista encadeada vazia.")

        valor_removido = self._cabeca.valor
        self._cabeca = self._cabeca.proximo

        if self._cabeca is None:
            self._cauda = None

        self._tamanho -= 1
        return valor_removido

    def remover_do_fim(self) -> T:
        if self._cabeca is None:
            raise IndexError("Não é possível remover de uma lista encadeada vazia.")

        if self._cabeca == self._cauda:
            valor_removido = self._cabeca.valor
            self._cabeca = None
            self._cauda = None
            self._tamanho -= 1
            return valor_removido

        anterior = self._cabeca
        atual = self._cabeca.proximo

        while atual is not None and atual != self._cauda:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            raise RuntimeError("Estado inconsistente da lista encadeada.")

        valor_removido = atual.valor
        anterior.proximo = None
        self._cauda = anterior
        self._tamanho -= 1
        return valor_removido

    def remover_valor(self, valor: T) -> bool:
        if self._cabeca is None:
            return False

        if self._cabeca.valor == valor:
            self.remover_do_inicio()
            return True

        anterior = self._cabeca
        atual = self._cabeca.proximo

        while atual is not None:
            if atual.valor == valor:
                anterior.proximo = atual.proximo

                if atual == self._cauda:
                    self._cauda = anterior

                self._tamanho -= 1
                return True

            anterior = atual
            atual = atual.proximo

        return False

    def buscar(self, valor: T) -> bool:
        atual = self._cabeca

        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo

        return False

    def obter(self, indice: int) -> T:
        if indice < 0 or indice >= self._tamanho:
            raise IndexError("Índice fora do intervalo.")

        atual = self._cabeca
        for _ in range(indice):
            if atual is None:
                raise IndexError("Índice inválido.")
            atual = atual.proximo

        if atual is None:
            raise IndexError("Índice inválido.")

        return atual.valor

    def obter_primeiro(self) -> T:
        if self._cabeca is None:
            raise IndexError("A lista encadeada está vazia.")
        return self._cabeca.valor

    def obter_ultimo(self) -> T:
        if self._cauda is None:
            raise IndexError("A lista encadeada está vazia.")
        return self._cauda.valor

    def listar(self) -> list[T]:
        elementos: list[T] = []
        atual = self._cabeca

        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        return elementos

    def listar_debug(self) -> None:
        print("\n" + "=" * 55)
        print("DEBUG DA LISTA ENCADEADA")
        print("=" * 55)
        print(f"Tamanho atual : {self._tamanho}")
        print(f"Está vazia?   : {self.esta_vazia()}")
        print(f"Cabeça        : {self._cabeca.valor if self._cabeca else None}")
        print(f"Cauda         : {self._cauda.valor if self._cauda else None}")
        print("-" * 55)

        if self._cabeca is None:
            print("Lista sem elementos.")
            print("=" * 55)
            return

        atual = self._cabeca
        indice = 0

        while atual is not None:
            marcador = []
            if atual == self._cabeca:
                marcador.append("CABEÇA")
            if atual == self._cauda:
                marcador.append("CAUDA")

            sufixo = f" <- {' | '.join(marcador)}" if marcador else ""
            proximo_valor = atual.proximo.valor if atual.proximo else None

            print(
                f"[índice {indice}] valor={atual.valor} | "
                f"proximo={proximo_valor}{sufixo}"
            )

            atual = atual.proximo
            indice += 1

        print("-" * 55)
        print("Visualização lógica:")
        print(" -> ".join(str(valor) for valor in self.listar()) + " -> None")
        print("=" * 55)

    def limpar(self) -> None:
        self._cabeca = None
        self._cauda = None
        self._tamanho = 0

    def __iter__(self) -> Iterator[T]:
        atual = self._cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self) -> int:
        return self._tamanho

    def __repr__(self) -> str:
        return f"ListaEncadeada(elementos={self.listar()})"


if __name__ == "__main__":
    print("\n=== EXEMPLO 1: LISTA ENCADEADA DE STRINGS ===")
    lista_tarefas: ListaEncadeada[str] = ListaEncadeada()
    lista_tarefas.inserir_no_fim("preparar")
    lista_tarefas.inserir_no_fim("validar")
    lista_tarefas.inserir_no_inicio("iniciar")
    print(lista_tarefas)
    print("Buscar 'validar':", lista_tarefas.buscar("validar"))
    print("Primeiro:", lista_tarefas.obter_primeiro())
    print("Último:", lista_tarefas.obter_ultimo())
    print("Remover do início:", lista_tarefas.remover_do_inicio())
    print("Lista atual:", lista_tarefas.listar())
    lista_tarefas.listar_debug()

    print("\n=== EXEMPLO 2: LISTA ENCADEADA DE INTEIROS ===")
    lista_numeros: ListaEncadeada[int] = ListaEncadeada()
    lista_numeros.inserir_no_fim(10)
    lista_numeros.inserir_no_fim(20)
    lista_numeros.inserir_no_fim(30)
    lista_numeros.inserir_em(1, 15)
    print(lista_numeros)
    print("Elemento no índice 2:", lista_numeros.obter(2))
    print("Remover do fim:", lista_numeros.remover_do_fim())
    print("Lista atual:", lista_numeros.listar())
    lista_numeros.listar_debug()

    print("\n=== EXEMPLO 3: LISTA ENCADEADA DE OBJETOS ===")

    @dataclass
    class Cliente:
        id: int
        nome: str

    lista_clientes: ListaEncadeada[Cliente] = ListaEncadeada()
    lista_clientes.inserir_no_fim(Cliente(1, "Jorge"))
    lista_clientes.inserir_no_fim(Cliente(2, "Maria"))
    lista_clientes.inserir_no_inicio(Cliente(0, "Ana"))

    for cliente in lista_clientes:
        print(cliente)

    lista_clientes.listar_debug()