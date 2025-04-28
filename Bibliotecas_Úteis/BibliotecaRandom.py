import random
print()
print("🧠 Tudo sobre random em um único código:\n")

# 1️⃣ random.random() -> Gera um número float aleatório entre 0.0 e 1.0
print("1️⃣ Número aleatório entre 0.0 e 1.0:", random.random())

# 2️⃣ random.uniform(a, b) -> Gera um número float entre a e b
print("2️⃣ Número float entre 10.5 e 20.5:", random.uniform(10.5, 20.5))

# 3️⃣ random.randint(a, b) -> Número inteiro entre a e b (INCLUSIVO)
print("3️⃣ Número inteiro entre 1 e 10:", random.randint(1, 10))

# 4️⃣ random.randrange(start, stop[, step]) -> Inteiro entre start e stop (stop EXCLUSIVO)
print("4️⃣ Número entre 0 e 100 com passo 5:", random.randrange(0, 100, 5))

# 5️⃣ random.choice(seq) -> Escolhe 1 elemento aleatório de uma sequência
nomes = ['Alice', 'Bruno', 'Carlos', 'Diana']
print("5️⃣ Nome sorteado:", random.choice(nomes))
dado = [1,2,3,4,5,6]
print("   Nº do Dado 🎲:", random.choice(dado))

# 6️⃣ random.choices(seq, k=n) -> Escolhe n elementos com reposição (pode repetir)
print("6️⃣ Lista com 3 nomes aleatórios (com repetição):", random.choices(nomes, k=3))

# 7️⃣ random.sample(seq, k=n) -> Sorteia n elementos SEM repetição
print("7️⃣ Lista com 3 nomes aleatórios (sem repetição):", random.sample(nomes, 3))

# 8️⃣ random.shuffle(seq) -> Embaralha a lista original (modifica a lista)
cartas = ['A♠', 'K♠', 'Q♠', 'J♠']
random.shuffle(cartas)
print("8️⃣ Cartas embaralhadas:", cartas)

# 9️⃣ random.seed(n) -> Define uma semente para resultados reproduzíveis
print("\n9️⃣ Usando seed para repetir os mesmos números:")
random.seed(42)
print("Repetível 1:", random.randint(1, 100))
random.seed(42)
print("Repetível 2 (igual ao anterior):", random.randint(1, 100))

# 1️⃣0️⃣ Simulando uma moeda
def jogar_moeda():
    return random.choice(["Cara", "Coroa"])

print("🔁 Jogando uma moeda:", jogar_moeda())

# 1️⃣1️⃣ Simulando um dado de 6 lados
def rolar_dado():
    return random.randint(1, 6)

print("🎲 Resultado do dado:", rolar_dado())

# 1️⃣2️⃣ Sorteio de números únicos da Mega-Sena
def mega_sena():
    return sorted(random.sample(range(1, 61), 6))

print("🎰 Números da Mega-Sena:", mega_sena())

# 1️⃣3️⃣ Simulando notas de alunos (de 0 a 10)
def gerar_notas(n):
    return [round(random.uniform(0, 10), 1) for _ in range(n)]

print("📊 Notas simuladas para 5 alunos:", gerar_notas(5))
