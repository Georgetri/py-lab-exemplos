'''
============================================================
📘 CADERNO DE RESPOSTAS – Lógica de Programação em Python
Autor: Jorge Luis
Objetivo: Treinar raciocínio lógico, estruturas de repetição,
condicionais, listas e funções em Python.
============================================================
'''

# ============================================================
# 🧩 EXERCÍCIO 1 – Maior e menor número
# ============================================================
numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
print("Maior:", max(numeros))
print("Menor:", min(numeros))


# ============================================================
# 🧮 EXERCÍCIO 2 – Média e quem está acima dela
# ============================================================
notas = [float(input(f"Nota {i+1}: ")) for i in range(5)]
media = sum(notas) / len(notas)
acima = [n for n in notas if n > media]
print(f"Média: {media:.2f}")
print("Acima da média:", acima)


# ============================================================
# 🔢 EXERCÍCIO 3 – Pares e ímpares
# ============================================================
numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print("Pares:", pares)
print("Ímpares:", impares)


# ============================================================
# 🧮 EXERCÍCIO 4 – Tabuada
# ============================================================
n = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# ============================================================
# 🪞 EXERCÍCIO 5 – Palíndromo
# ============================================================
texto = input("Digite uma palavra: ").lower().replace(" ", "")
if texto == texto[::-1]:
    print("É palíndromo!")
else:
    print("Não é palíndromo.")


# ============================================================
# 🧠 EXERCÍCIO 6 – Contar vogais
# ============================================================
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
contagem = sum(1 for letra in frase if letra in vogais)
print("Número de vogais:", contagem)


# ============================================================
# ➕ EXERCÍCIO 7 – Somar positivos
# ============================================================
valores = [float(input(f"Valor {i+1}: ")) for i in range(5)]
positivos = [v for v in valores if v > 0]
print("Soma dos positivos:", sum(positivos))


# ============================================================
# 🔁 EXERCÍCIO 8 – Reverter lista
# ============================================================
lista = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
print("Lista invertida:", lista[::-1])


# ============================================================
# ➖ EXERCÍCIO 9 – Contar negativos
# ============================================================
numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(5)]
negativos = [n for n in numeros if n < 0]
print("Negativos:", negativos)
print("Quantidade:", len(negativos))


# ============================================================
# 🧮 EXERCÍCIO 10 – Fatorial
# ============================================================
num = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print(f"{num}! = {fatorial}")
# Complexidade O(n)
