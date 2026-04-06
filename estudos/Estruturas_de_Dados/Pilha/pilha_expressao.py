import numpy as np

class Pilha:
    def __init__(self,capacidade): # dois traços __ define como privado
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype='<U1')

    def __pilha_cheia(self):
        if self.topo == self.capacidade -1:
            return True
        else:
            return False


    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False


    def empilhar(self,valor):
        if self.__pilha_cheia():
            print('A pílha está cheia')
        else:
            self.topo += 1
            self.valores[self.topo] = valor


    def desempilhar(self):
        if self.pilha_vazia():
            print('A pilha está vazia')
            return None
        valor = self.valores[self.topo]
        self.topo -= 1
        return valor


    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        else:
            return -1


expressao = str(input('Digite uma expressão:'))
pilha = Pilha(len(expressao))

for i in range(len(expressao)):
    ch = expressao[i]
    if ch == '{' or ch == '[' or ch == '(':
        pilha.empilhar(ch)
    elif ch == '}' or ch == ']' or ch == ')':
        if not pilha.pilha_vazia():
            chx = str(pilha.desempilhar())
            if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '('):
                print('Erro:',ch,' na posicao ', i)
                break
        else:
            print('Erro:', ch, ' na posicao ', i)
if not pilha.pilha_vazia():
    print('Erro !')


# =========================
#         TESTES
# =========================

# c[d] , a{b[c]d}e , a{b(c]d}e, a[b{c}d]e}, a{b(c)


"""
Então, pra que serve isso?

Este código utiliza uma pilha (estrutura de dados do tipo LIFO - Last In, First Out)
para verificar se uma expressão possui símbolos corretamente balanceados.

Ele analisa caracteres como:
    (), {}, []

A lógica é a seguinte:

1. Sempre que encontra um símbolo de abertura:
   - '(', '{', '['
   → ele empilha esse símbolo.

2. Sempre que encontra um símbolo de fechamento:
   - ')', '}', ']'
   → ele desempilha o último símbolo aberto e verifica se corresponde.

3. Se houver incompatibilidade (ex: fecha com ']' mas abriu com '('):
   → ocorre erro.

4. Ao final da leitura da expressão:
   - Se a pilha estiver vazia → expressão válida
   - Se ainda houver elementos → erro (algo não foi fechado)

Exemplo:

Entrada:
    a{b(c)d}

Processo:
    empilha '{'
    empilha '('
    desempilha '(' ao encontrar ')'
    desempilha '{' ao encontrar '}'

Resultado:
    Expressão válida

----------------------------------------

Caso de erro:

Entrada:
    a{b(c)

Processo:
    empilha '{'
    empilha '('
    desempilha '(' ao encontrar ')'
    sobra '{' na pilha

Resultado:
    Erro!

----------------------------------------

Aplicações reais desse algoritmo:

- Compiladores e interpretadores de linguagem
- Editores de código (VSCode, IntelliJ)
- Validação de JSON e estruturas de dados
- Análise de expressões matemáticas
- Parsers (análise sintática)

Resumo:

Este algoritmo responde à pergunta:
"Todos os símbolos abertos foram fechados corretamente?"

Se sim → estrutura válida
Se não → erro estrutural
"""