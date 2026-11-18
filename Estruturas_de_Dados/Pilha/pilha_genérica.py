from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterator, Optional, TypeVar

# Uma pilha genérica é usada em ambientes profissionais para implementar comportamentos LIFO em diversos contextos,
# como undo/redo, parsing, backtracking e controle de execução, garantindo reutilização e segurança de tipos.

T = TypeVar("T")

@dataclass
class No(Generic[T]):
    valor: T
    proximo: Optional["No[T]"] = None


class Pilha(Generic[T]):
    def __init__(self) -> None:
        self._topo: Optional[No[T]] = None
        self._tamanho: int = 0

    def esta_vazia(self) -> bool:
        return self._topo is None

    def tamanho(self) -> int:
        return self._tamanho

    def empilhar(self, valor: T) -> None:
        novo_no = No(valor=valor, proximo=self._topo)
        self._topo = novo_no
        self._tamanho += 1

    def desempilhar(self) -> T:
        if self._topo is None:
            raise IndexError("Não é possível desempilhar uma pilha vazia.")

        valor_removido = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return valor_removido

    def espiar(self) -> T:
        if self._topo is None:
            raise IndexError("Não é possível espiar uma pilha vazia.")

        return self._topo.valor

    def limpar(self) -> None:
        self._topo = None
        self._tamanho = 0

    def listar(self) -> list[T]:
        """
        Retorna os elementos da pilha do topo para a base.
        Exemplo:
        topo -> [30, 20, 10] <- base
        """
        elementos: list[T] = []
        atual = self._topo

        while atual is not None:
            elementos.append(atual.valor)
            atual = atual.proximo

        return elementos

    def listar_base_para_topo(self) -> list[T]:
        """
        Retorna os elementos da base para o topo.
        Exemplo:
        base -> [10, 20, 30] <- topo
        """
        return list(reversed(self.listar()))

    def __iter__(self) -> Iterator[T]:
        atual = self._topo
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self) -> int:
        return self._tamanho

    def __repr__(self) -> str:
        return f"Pilha(topo_para_base={self.listar()})"