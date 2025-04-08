import math
import random
from decimal import Decimal, getcontext
from fractions import Fraction

print("📘 1. Tipos numéricos em Python")
print("int = inteiro | float = decimal | complex = número complexo")
a = 10
b = 3.5
c = 2 + 3j  # Número complexo
print("int (a):", a, "| tipo:", type(a))
print("float (b):", b, "| tipo:", type(b))
print("complex (c):", c, "| tipo:", type(c))
print("-------------------------")

print("📘 2. Operações com float: cuidado com precisão")
print("0.1 + 0.2 não é exatamente 0.3 por causa da precisão binária:")
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3?", 0.1 + 0.2 == 0.3)
print("-------------------------")

print("📘 3. Usando Decimal para mais precisão")
getcontext().prec = 10  # Define precisão de casas decimais
x = Decimal("0.1")
y = Decimal("0.2")
z = x + y
print("Decimal('0.1') + Decimal('0.2') =", z)
print("Precisão controlada:", z == Decimal("0.3"))
print("-------------------------")

print("📘 4. Usando Fraction para frações exatas")
f1 = Fraction(1, 3)
f2 = Fraction(1, 6)
soma = f1 + f2
print("1/3 + 1/6 =", soma)  # 1/2
print("Como float:", float(soma))
print("-------------------------")

print("📘 5. Números complexos: parte real e imaginária")
z = 3 + 4j
print("Número complexo:", z)
print("Parte real:", z.real)
print("Parte imaginária:", z.imag)
print("Módulo (|z|):", abs(z))
print("-------------------------")

print("📘 6. Funções matemáticas com o módulo math")
print("math.sqrt(25):", math.sqrt(25))
print("math.pow(2, 3):", math.pow(2, 3))
print("math.factorial(5):", math.factorial(5))
print("math.log(100, 10):", math.log(100, 10))  # log base 10
print("math.gcd(36, 60):", math.gcd(36, 60))  # máximo divisor comum
print("-------------------------")

print("📘 7. Trigonometria com math")
graus = 90
radianos = math.radians(graus)
print("Seno de 90 graus:", math.sin(radianos))
print("Cosseno de 0 graus:", math.cos(math.radians(0)))
print("-------------------------")

print("📘 8. Geração de números aleatórios com random")
print("random.randint(1, 100):", random.randint(1, 100))
print("random.uniform(1.5, 3.5):", random.uniform(1.5, 3.5))
lista = [10, 20, 30, 40]
print("random.choice(lista):", random.choice(lista))
print("random.shuffle embaralha a lista:")
random.shuffle(lista)
print("Lista embaralhada:", lista)
print("-------------------------")

print("📘 9. Operadores binários (bitwise)")
a = 6  # binário: 110
b = 3  # binário: 011
print("a & b (E bit-a-bit):", a & b)  # 110 & 011 = 010 = 2
print("a | b (OU bit-a-bit):", a | b)  # 110 | 011 = 111 = 7
print("a ^ b (XOR):", a ^ b)  # 110 ^ 011 = 101 = 5
print("~a (NOT):", ~a)  # Inverte os bits
print("a << 1 (shift para a esquerda):", a << 1)  # 1100 = 12
print("a >> 1 (shift para a direita):", a >> 1)  # 011 = 3
print("-------------------------")

print("📘 10. Conversões entre tipos numéricos")
num = 7.89
print("float:", num)
print("Para inteiro (int(num)):", int(num))
print("Para string (str(num)):", str(num))
print("Para Decimal:", Decimal(str(num)))
print("Para fração:", Fraction(num).limit_denominator())
print("-------------------------")

print("📘 11. Expressões matemáticas com parênteses e ordem de precedência")
resultado = 10 + 2 * 5  # 10 + (2*5) = 20
print("Sem parênteses (10 + 2 * 5):", resultado)
resultado2 = (10 + 2) * 5  # (10+2)*5 = 60
print("Com parênteses ((10 + 2) * 5):", resultado2)
print("-------------------------")
