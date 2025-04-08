import math

print("--------------------------------------------------")

# Entrada de número real (float)
print("\n▶️ Entrada de número real (float)")
print("Digite um número com casas decimais, ex: 3.14")
numero_real = float(input("Digite um número real: "))
print(f"Você digitou o número {numero_real:.2f}, que é do tipo {type(numero_real)}")

print("--------------------------------------------------")

# Cálculo da área da circunferência
print("\n▶️ Cálculo da área da circunferência")
print("Usando a fórmula A = π . r² com raio r = 6")
r = 6
A = math.pi * math.pow(r, 2)
print(f"Área da circunferência com raio {r}m: {A:.2f} m²")

# Cálculo do perímetro da circunferência
print("\n▶️ Cálculo do perímetro da circunferência")
print("Usando a fórmula P = 2πr com raio r = 10")
r = 10
P = 2 * math.pi * r
print(f"Perímetro da circunferência com raio {r}m: {P:.2f} m")

print("--------------------------------------------------")

# Entrada de múltiplos floats com validação
print("\n▶️ Entrada de múltiplos números reais com validação")
print("Digite dois números reais separados por espaço (ex: 2.5 3.14)")
while True:
    try:
        a, b = map(float, input("Digite dois números reais: ").split())
        print(f"Você digitou a = {a:.2f} e b = {b:.2f}")
        print(f"Soma = {a + b:.2f} | Média = {(a + b) / 2:.2f}")
        break
    except ValueError:
        print("❌ Entrada inválida. Use ponto para casas decimais e separe com espaço.")

print("--------------------------------------------------")

# Raiz quadrada e potência com float
print("\n▶️ Operações com float: raiz quadrada e potência")
numero = float(input("Digite um número real para calcular sua raiz quadrada e potência ao cubo: "))
print(f"Raiz quadrada de {numero:.2f} = {math.sqrt(numero):.2f}")
print(f"{numero:.2f} elevado ao cubo = {math.pow(numero, 3):.2f}")

print("--------------------------------------------------")

# Exemplo prático: cálculo do IMC
print("\n▶️ Cálculo do IMC (Índice de Massa Corporal)")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / math.pow(altura, 2)
print(f"Seu IMC é: {imc:.2f}")

# Classificação básica do IMC
print("Classificação do IMC:")
if imc < 18.5:
    print("→ Abaixo do peso")
elif imc < 25:
    print("→ Peso normal")
elif imc < 30:
    print("→ Sobrepeso")
else:
    print("→ Obesidade")

print("--------------------------------------------------")

# Conversão de temperatura
print("\n▶️ Conversão de temperatura (Celsius ↔ Fahrenheit)")
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F")

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit:.2f}°F equivalem a {celsius:.2f}°C")

print("✅ Fim dos exemplos avançados com números float")
