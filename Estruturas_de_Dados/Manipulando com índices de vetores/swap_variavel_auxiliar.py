"""
    Exemplos de troca (swap) usando variável auxiliar.
"""
# Exemplo 1: troca simples de inteiros
print("Exemplo 1: troca simples de inteiros")
a = 10
b = 20
print(f"Antes: a = {a}, b = {b}")

aux = a
a = b
b = aux

print(f"Depois: a = {a}, b = {b}")
print("-" * 40)

# Exemplo 2: troca de valores de ponto flutuante
print("Exemplo 2: troca de floats")
taxa_juros_atual = 0.12
taxa_juros_nova = 0.10
print(f"Antes: atual = {taxa_juros_atual}, nova = {taxa_juros_nova}")

aux = taxa_juros_atual
taxa_juros_atual = taxa_juros_nova
taxa_juros_nova = aux

print(f"Depois: atual = {taxa_juros_atual}, nova = {taxa_juros_nova}")
print("-" * 40)

# Exemplo 3: troca de strings
print("Exemplo 3: troca de strings")
nome = "Jorge"
sobrenome = "Luis"
print(f"Antes: nome = {nome}, sobrenome = {sobrenome}")

aux = nome
nome = sobrenome
sobrenome = aux

print(f"Depois: nome = {nome}, sobrenome = {sobrenome}")
print("-" * 40)

# Exemplo 4: troca de booleanos
print("Exemplo 4: troca de booleanos")
ligado = True
desligado = False
print(f"Antes: ligado = {ligado}, desligado = {desligado}")

aux = ligado
ligado = desligado
desligado = aux

print(f"Depois: ligado = {ligado}, desligado = {desligado}")
print("-" * 40)

# Exemplo 5: troca de mínimo e máximo
print("Exemplo 5: troca de mínimo e máximo")
minimo = 5
maximo = 100
print(f"Antes: mínimo = {minimo}, máximo = {maximo}")

# garante que mínimo seja sempre o menor
if minimo > maximo:
    aux = minimo
    minimo = maximo
    maximo = aux

print(f"Depois (ajustado): mínimo = {minimo}, máximo = {maximo}")
print("-" * 40)
