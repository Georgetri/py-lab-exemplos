# números_avancado.py

import math
import random
from decimal import Decimal, getcontext
from fractions import Fraction

# Configura a precisão do Decimal
getcontext().prec = 10

print("📘 EXEMPLOS AVANÇADOS DE NÚMEROS EM PYTHON")
print("--------------------------------------------------")

# Inteiros e floats
print("\n▶️ Trabalhando com inteiros e floats")
print("a = 10, b = 3")
a = 10
b = 3
print("Divisão comum (a / b):", a / b)
print("Divisão inteira (a // b):", a // b)
print("Resto da divisão (a % b):", a % b)
print("Potência (a ** b):", a ** b)

print("--------------------------------------------------")

# Cuidado com floats
print("\n▶️ Precisão de floats (problema comum)")
print("print(0.1 + 0.2) → resultado impreciso por causa do sistema binário:")
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3?", 0.1 + 0.2 == 0.3)

print("--------------------------------------------------")

# Usando Decimal
print("\n▶️ Usando Decimal para cálculos precisos")
x = Decimal("0.1")
y = Decimal("0.2")
z = x + y
print("Decimal('0.1') + Decimal('0.2') =", z)
print("z == Decimal('0.3'):", z == Decimal("0.3"))

print("--------------------------------------------------")

# Frações exatas
print("\n▶️ Trabalhando com frações exatas")
f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
soma = f1 + f2
print("Fraction(1, 3) + Fraction(1, 6) =", soma)
print("float(Fraction) =", float(soma))

print("--------------------------------------------------")

# Números complexos
print("\n▶️ Números complexos")
z = 4 + 5j
print("Número complexo z =", z)
print("Parte real:", z.real)
print("Parte imaginária:", z.imag)
print("Módulo (magnitude) de z:", abs(z))

print("--------------------------------------------------")

# Operadores compostos
print("\n▶️ Operadores compostos (+=, -=, etc)")
n = 5
print("n =", n)
n += 3
print("n += 3 →", n)
n *= 2
print("n *= 2 →", n)

print("--------------------------------------------------")

# Math avançado
print("\n▶️ Funções matemáticas com math")
print("Raiz quadrada de 49:", math.sqrt(49))
print("Potência: 2^5 =", math.pow(2, 5))
print("Fatorial de 6:", math.factorial(6))
print("Log base 10 de 1000:", math.log10(1000))
print("MDC entre 48 e 180:", math.gcd(48, 180))

print("--------------------------------------------------")

# Trigonometria
print("\n▶️ Trigonometria")
graus = 90
radianos = math.radians(graus)
print("Seno de 90 graus:", math.sin(radianos))
print("Cosseno de 0 graus:", math.cos(math.radians(0)))

print("--------------------------------------------------")

# Aleatoriedade com random
print("\n▶️ Geração de números aleatórios")
print("random.randint(1, 100):", random.randint(1, 100))
print("random.uniform(1.5, 5.5):", random.uniform(1.5, 5.5))
lista = ['Python', 'Java', 'C++']
print("Sorteio com random.choice(lista):", random.choice(lista))
print("random.shuffle(lista): embaralha a lista")
random.shuffle(lista)
print("Lista embaralhada:", lista)

print("--------------------------------------------------")

# Bitwise
print("\n▶️ Operadores Bit a Bit")
a = 6  # binário: 110
b = 3  # binário: 011
print("a =", a, "em binário:", bin(a))
print("b =", b, "em binário:", bin(b))
print("a & b (AND):", a & b, "| bin:", bin(a & b))
print("a | b (OR):", a | b, "| bin:", bin(a | b))
print("a ^ b (XOR):", a ^ b, "| bin:", bin(a ^ b))
print("~a (NOT):", ~a)
print("a << 1 (Shift à esquerda):", a << 1)
print("a >> 1 (Shift à direita):", a >> 1)

print("--------------------------------------------------")

# Conversão entre tipos
print("\n▶️ Conversão entre tipos numéricos")
n = 7.89
print("float:", n)
print("int(n):", int(n))
print("str(n):", str(n))
print("Decimal(str(n)):", Decimal(str(n)))
print("Fraction(n).limit_denominator():", Fraction(n).limit_denominator())

print("--------------------------------------------------")

print("✅ Fim da demonstração!")
