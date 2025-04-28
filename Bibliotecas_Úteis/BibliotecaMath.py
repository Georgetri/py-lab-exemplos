import math

# Função para mostrar constantes matemáticas
def mostrar_constantes():
    print("📌 Constantes:")
    print("PI:", math.pi)
    print("Euler (e):", math.e)
    print("Tau (2π):", math.tau)
    print("Infinito:", math.inf)
    print("Not a Number:", math.nan)
    print()

# Função para operações básicas
def operacoes_basicas(x, y):
    print("➕ Operações básicas:")
    print(f"sqrt({x}):", math.sqrt(x))       # Raiz quadrada
    print(f"pow({x}, {y}):", math.pow(x, y)) # Potência
    print(f"fabs(-{x}):", math.fabs(-x))     # Valor absoluto
    print(f"fmod({x}, {y}):", math.fmod(x, y)) # Resto da divisão
    print()

# Função para arredondamentos e divisões
def arredondamentos_e_divisao(a, b):
    print("🔁 Arredondamentos e divisão:")
    print(f"floor({a}):", math.floor(a))     # Arredonda para baixo
    print(f"ceil({a}):", math.ceil(a))       # Arredonda para cima
    print(f"trunc({a}):", math.trunc(a))     # Trunca o número (remove decimais)
    print(f"gcd({int(a)}, {int(b)}):", math.gcd(int(a), int(b)))  # Máximo divisor comum
    print()

# Função para funções trigonométricas
def funcoes_trigonometria(angulo_graus):
    angulo_rad = math.radians(angulo_graus)  # Converte para radianos
    print("🧭 Trigonometria:")
    print(f"Graus: {angulo_graus}° | Radianos: {angulo_rad}")
    print(f"sin({angulo_graus}°):", math.sin(angulo_rad)) #Seno
    print(f"cos({angulo_graus}°):", math.cos(angulo_rad)) #Cosseno
    print(f"tan({angulo_graus}°):", math.tan(angulo_rad)) #Tangente
    print()

# Função para logaritmos e exponenciais
def logaritmos_e_exp(n):
    print("📈 Logaritmos e exponenciais:")
    print(f"exp({n}):", math.exp(n))         # e^n
    print(f"log({n}):", math.log(n))         # log natural (base e)
    print(f"log10({n}):", math.log10(n))     # log na base 10
    print(f"log2({n}):", math.log2(n))       # log na base 2
    print()

# Função para fatorial e combinações
def fatorial_e_combinatoria(n, k):
    print("📊 Fatorial e combinatória:")
    print(f"factorial({n}):", math.factorial(n))
    print(f"comb({n}, {k}):", math.comb(n, k))     # Combinações: C(n, k)
    print(f"perm({n}, {k}):", math.perm(n, k))     # Permutações: P(n, k)
    print()

# Chamada das funções com valores de exemplo
mostrar_constantes()
operacoes_basicas(9, 2)
arredondamentos_e_divisao(5.75, 3.25)
funcoes_trigonometria(45)
logaritmos_e_exp(10)
fatorial_e_combinatoria(5, 3)
