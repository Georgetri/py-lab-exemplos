from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterator, Optional, TypeVar


T = TypeVar("T")


@dataclass
class No(Generic[T]):
    valor: T
    proximo: Optional["No[T]"] = None


class Fila(Generic[T]):
    def __init__(self) -> None:
        self._frente: Optional[No[T]] = None
        self._tras: Optional[No[T]] = None
        self._tamanho: int = 0

    def esta_vazia(self) -> bool:
        return self._frente is None

    def tamanho(self) -> int:
        return self._tamanho

    def enfileirar(self, valor: T) -> None:
        novo_no = No(valor=valor)

        if self._tras is None:
            self._frente = novo_no
            self._tras = novo_no
        else:
            self._tras.proximo = novo_no
            self._tras = novo_no

        self._tamanho += 1

    def desenfileirar(self) -> T:
        if self._frente is None:
            raise IndexError("Não é possível desenfileirar uma fila vazia.")

        valor_removido = self._frente.valor
        self._frente = self._frente.proximo

        if self._frente is None:
            self._tras = None

        self._tamanho -= 1
        return valor_removido

    def primeiro(self) -> T:
        if self._frente is None:
            raise IndexError("Não é possível consultar uma fila vazia.")

        return self._frente.valor

    def listar(self) -> list[T]:
        return list(self)

    def limpar(self) -> None:
        self._frente = None
        self._tras = None
        self._tamanho = 0

    def __iter__(self) -> Iterator[T]:
        atual = self._frente
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self) -> int:
        return self._tamanho

    def __repr__(self) -> str:
        return f"Fila({self.listar()})"


if __name__ == "__main__":
    print("\n=== EXEMPLO 1: FILA DE STRINGS ===")
    fila_atendimento: Fila[str] = Fila()
    fila_atendimento.enfileirar("cliente 1")
    fila_atendimento.enfileirar("cliente 2")
    fila_atendimento.enfileirar("cliente 3")
    print(fila_atendimento)
    print("Primeiro:", fila_atendimento.primeiro())
    print("Desenfileirar:", fila_atendimento.desenfileirar())
    print("Fila atual:", fila_atendimento.listar())

    print("\n=== EXEMPLO 2: FILA DE INTEIROS ===")
    fila_senhas: Fila[int] = Fila()
    fila_senhas.enfileirar(101)
    fila_senhas.enfileirar(102)
    fila_senhas.enfileirar(103)
    print(fila_senhas)

    print("\n=== EXEMPLO 3: FILA DE OBJETOS ===")

    @dataclass
    class Pedido:
        numero: int
        produto: str

    fila_pedidos: Fila[Pedido] = Fila()
    fila_pedidos.enfileirar(Pedido(1, "Notebook"))
    fila_pedidos.enfileirar(Pedido(2, "Mouse"))

    for pedido in fila_pedidos:
        print(pedido)