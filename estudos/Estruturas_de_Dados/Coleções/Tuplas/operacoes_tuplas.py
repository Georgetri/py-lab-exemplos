"""
==============================================================
            OPERADORES MATEMÁTICOS EM TUPLAS (PYTHON)
==============================================================

Este script contém:

1) Operações usando FOR:
   - Somar valor
   - Subtrair valor
   - Multiplicar por valor
   - Dividir por valor

2) Operações usando WHILE:
   - Somar valor
   - Subtrair valor
   - Multiplicar por valor
   - Dividir por valor

3) Operações ENTRE DUAS TUPLAS (FOR):
   - Soma elemento a elemento
   - Subtração
   - Multiplicação
   - Divisão

4) Operações ENTRE DUAS TUPLAS (WHILE)

Tuplas são IMUTÁVEIS, então cada operação retorna uma NOVA tupla.

Observe que em nenhuma função tentamos alterar valores diretamente.
Todas criam uma nova coleção e a convertem para tupla.
"""

# ======================================================================
#   FUNÇÕES AUXILIARES
# ======================================================================

def linha():
    print("-" * 60)

def pause():
    input("\nPressione ENTER para continuar...")

def titulo(txt):
    linha()
    print(txt)
    linha()


# ======================================================================
#   1) OPERAÇÕES COM FOR (TUPLA + VALOR)
# ======================================================================

def somar_for(tupla, valor):
    nova = []
    for elemento in tupla:
        nova.append(elemento + valor)
    return tuple(nova)

def subtrair_for(tupla, valor):
    nova = []
    for elemento in tupla:
        nova.append(elemento - valor)
    return tuple(nova)

def multiplicar_for(tupla, valor):
    nova = []
    for elemento in tupla:
        nova.append(elemento * valor)
    return tuple(nova)

def dividir_for(tupla, valor):
    nova = []
    for elemento in tupla:
        nova.append(elemento / valor)
    return tuple(nova)


# ======================================================================
#   2) OPERAÇÕES COM WHILE (TUPLA + VALOR)
# ======================================================================

def somar_while(tupla, valor):
    nova = []
    i = 0
    while i < len(tupla):
        nova.append(tupla[i] + valor)
        i += 1
    return tuple(nova)

def subtrair_while(tupla, valor):
    nova = []
    i = 0
    while i < len(tupla):
        nova.append(tupla[i] - valor)
        i += 1
    return tuple(nova)

def multiplicar_while(tupla, valor):
    nova = []
    i = 0
    while i < len(tupla):
        nova.append(tupla[i] * valor)
        i += 1
    return tuple(nova)

def dividir_while(tupla, valor):
    nova = []
    i = 0
    while i < len(tupla):
        nova.append(tupla[i] / valor)
        i += 1
    return tuple(nova)


# ======================================================================
#   3) OPERAÇÕES ENTRE DUAS TUPLAS (FOR)
# ======================================================================

def somar_tuplas_for(t1, t2):
    nova = []
    for a, b in zip(t1, t2):   # percorre ambas ao mesmo tempo
        nova.append(a + b)
    return tuple(nova)

def subtrair_tuplas_for(t1, t2):
    nova = []
    for a, b in zip(t1, t2):
        nova.append(a - b)
    return tuple(nova)

def multiplicar_tuplas_for(t1, t2):
    nova = []
    for a, b in zip(t1, t2):
        nova.append(a * b)
    return tuple(nova)

def dividir_tuplas_for(t1, t2):
    nova = []
    for a, b in zip(t1, t2):
        nova.append(a / b)
    return tuple(nova)


# ======================================================================
#   4) OPERAÇÕES ENTRE DUAS TUPLAS (WHILE)
# ======================================================================

def somar_tuplas_while(t1, t2):
    nova = []
    i = 0
    while i < len(t1):
        nova.append(t1[i] + t2[i])
        i += 1
    return tuple(nova)

def subtrair_tuplas_while(t1, t2):
    nova = []
    i = 0
    while i < len(t1):
        nova.append(t1[i] - t2[i])
        i += 1
    return tuple(nova)

def multiplicar_tuplas_while(t1, t2):
    nova = []
    i = 0
    while i < len(t1):
        nova.append(t1[i] * t2[i])
        i += 1
    return tuple(nova)

def dividir_tuplas_while(t1, t2):
    nova = []
    i = 0
    while i < len(t1):
        nova.append(t1[i] / t2[i])
        i += 1
    return tuple(nova)


# ======================================================================
#   SUBMENUS
# ======================================================================

def submenu_for():
    titulo("OPERAR TUPLA (FOR)")
    t = (10, 20, 30, 40)
    print("Tupla base:", t)
    valor = int(input("Digite o valor para operar: "))

    print("\nResultados:")
    print("Somar:      ", somar_for(t, valor))
    print("Subtrair:   ", subtrair_for(t, valor))
    print("Multiplicar:", multiplicar_for(t, valor))
    print("Dividir:    ", dividir_for(t, valor))

    pause()


def submenu_while():
    titulo("OPERAR TUPLA (WHILE)")
    t = (10, 20, 30, 40)
    print("Tupla base:", t)
    valor = int(input("Digite o valor para operar: "))

    print("\nResultados:")
    print("Somar:      ", somar_while(t, valor))
    print("Subtrair:   ", subtrair_while(t, valor))
    print("Multiplicar:", multiplicar_while(t, valor))
    print("Dividir:    ", dividir_while(t, valor))

    pause()


def submenu_duas_tuplas_for():
    titulo("OPERAR DUAS TUPLAS (FOR)")
    t1 = (10, 20, 30)
    t2 = (1, 2, 3)

    print("Tupla 1:", t1)
    print("Tupla 2:", t2)

    print("\nResultados:")
    print("Somar:      ", somar_tuplas_for(t1, t2))
    print("Subtrair:   ", subtrair_tuplas_for(t1, t2))
    print("Multiplicar:", multiplicar_tuplas_for(t1, t2))
    print("Dividir:    ", dividir_tuplas_for(t1, t2))

    pause()


def submenu_duas_tuplas_while():
    titulo("OPERAR DUAS TUPLAS (WHILE)")
    t1 = (10, 20, 30)
    t2 = (1, 2, 3)

    print("Tupla 1:", t1)
    print("Tupla 2:", t2)

    print("\nResultados:")
    print("Somar:      ", somar_tuplas_while(t1, t2))
    print("Subtrair:   ", subtrair_tuplas_while(t1, t2))
    print("Multiplicar:", multiplicar_tuplas_while(t1, t2))
    print("Dividir:    ", dividir_tuplas_while(t1, t2))

    pause()


# ======================================================================
#   MENU PRINCIPAL
# ======================================================================

def menu():
    while True:
        titulo("MENU PRINCIPAL - OPERAÇÕES COM TUPLAS")
        print("1 - Operações com FOR (tupla + valor)")
        print("2 - Operações com WHILE (tupla + valor)")
        print("3 - Operar DUAS TUPLAS (FOR)")
        print("4 - Operar DUAS TUPLAS (WHILE)")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1": submenu_for()
            case "2": submenu_while()
            case "3": submenu_duas_tuplas_for()
            case "4": submenu_duas_tuplas_while()
            case "0":
                print("\nEncerrando. Bons estudos sobre tuplas!")
                break
            case _:
                print("Opção inválida!")
                pause()


# ======================================================================
#   PROGRAMA PRINCIPAL
# ======================================================================

if __name__ == "__main__":
    menu()
