print("1. Operações básicas com números")
print("Vamos somar, subtrair, multiplicar e dividir dois números:")
a = 10
b = 3
print("a =", a)
print("b =", b)
print("Soma (a + b):", a + b)
print("Subtração (a - b):", a - b)
print("Multiplicação (a * b):", a * b)
print("Divisão (a / b):", a / b)
print("-------------------------")

print("2. Divisão inteira e módulo (resto)")
print("A divisão inteira descarta os decimais, e o módulo retorna o resto:")
print("Divisão inteira (a // b):", a // b)
print("Resto da divisão (a % b):", a % b)
print("-------------------------")

print("3. Potência (expoente)")
print("Potência com operador '**' eleva um número a outro:")
print("a elevado a b (a ** b):", a ** b)
print("-------------------------")

print("4. Arredondamento")
print("Usamos round(), int() e float() para manipular casas decimais:")
num = 7.56789
print("Número original:", num)
print("Arredondado com round(num, 2):", round(num, 2))
print("Transformar em inteiro com int(num):", int(num))
print("Transformar inteiro em float com float(5):", float(5))
print("-------------------------")

print("5. Operadores de comparação")
print("Comparam valores e retornam True ou False:")
x = 8
y = 10
print("x =", x, ", y =", y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
print("-------------------------")

print("6. Operações combinadas (+=, -=, etc)")
print("Operadores para atualizar o valor de uma variável com uma operação:")
contador = 0
print("Contador inicial:", contador)
contador += 5
print("contador += 5:", contador)
contador *= 2
print("contador *= 2:", contador)
contador -= 3
print("contador -= 3:", contador)
contador /= 2
print("contador /= 2:", contador)
print("-------------------------")

print("7. Trabalhando com números aleatórios")
import random
print("Gerando números aleatórios com a biblioteca random:")
print("Número aleatório entre 1 e 10:", random.randint(1, 10))
print("Número float aleatório entre 0 e 1:", random.random())
print("-------------------------")

print("8. Cálculo com módulo math (raízes, seno, PI, etc)")
import math
print("Usamos a biblioteca math para funções matemáticas avançadas:")
print("Raiz quadrada de 16:", math.sqrt(16))
print("Seno de 90 graus (convertido em radianos):", math.sin(math.radians(90)))
print("Valor de PI:", math.pi)
print("-------------------------")

print("9. Conversões de tipos")
print("Convertendo strings para números e vice-versa:")
numero_str = "123"
print("String:", numero_str)
numero_int = int(numero_str)
print("Convertido para inteiro:", numero_int)
numero_float = float(numero_str)
print("Convertido para float:", numero_float)
numero_convertido_para_string = str(numero_int)
print("Convertido de volta para string:", numero_convertido_para_string)
print("-------------------------")

print("10. Trabalhando com médias")
notas = [7.5, 8.0, 6.5, 9.0]
print("Lista de notas:", notas)
media = sum(notas) / len(notas)
print("Média das notas:", media)
print("-------------------------")
