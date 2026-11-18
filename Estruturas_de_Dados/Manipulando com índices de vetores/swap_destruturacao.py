"""
    Exemplos de troca (swap) usando destruturação em Python.
"""

# Exemplo 1: troca simples de inteiros
print("Exemplo 1: troca simples de inteiros (a, b = b, a)")
a = 10
b = 20
print(f"Antes: a = {a}, b = {b}")

a, b = b, a

print(f"Depois: a = {a}, b = {b}")
print("-" * 40)

# Exemplo 2: troca de ordem para garantir (menor, maior)
print("Exemplo 2: garantindo que valor1 <= valor2")
valor1 = 50
valor2 = 10
print(f"Antes: valor1 = {valor1}, valor2 = {valor2}")

if valor1 > valor2:
    valor1, valor2 = valor2, valor1

print(f"Depois: valor1 = {valor1}, valor2 = {valor2}")
print("-" * 40)

# Exemplo 3: troca de coordenadas (x, y)
print("Exemplo 3: troca de coordenadas (x, y)")
x = 3
y = 7
print(f"Antes: x = {x}, y = {y}")

x, y = y, x

print(f"Depois: x = {x}, y = {y}")
print("-" * 40)

# Exemplo 4: troca de dia e mês (simulação de erro do usuário)
print("Exemplo 4: troca de dia e mês")
dia = 12
mes = 5   # usuário digitou invertido
print(f"Antes: dia = {dia}, mês = {mes}")

dia, mes = mes, dia

print(f"Depois (corrigido): dia = {dia}, mês = {mes}")
print("-" * 40)

# Exemplo 5: troca de variáveis dentro de uma função
print("Exemplo 5: função que garante (menor, maior) com swap")


def ordenar_par(a: int, b: int) -> tuple[int, int]:
    """Retorna (menor, maior) usando swap com destruturação."""
    if a > b:
        a, b = b, a
    return a, b


n1, n2 = 30, 5
print(f"Antes: n1 = {n1}, n2 = {n2}")
menor, maior = ordenar_par(n1, n2)
print(f"Depois (função): menor = {menor}, maior = {maior}")
print("-" * 40)
