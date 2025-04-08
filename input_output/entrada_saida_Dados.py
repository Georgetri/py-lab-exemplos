# entrada_saida_avancado.py

import sys
from datetime import datetime

print("📘 EXEMPLOS AVANÇADOS DE ENTRADA E SAÍDA EM PYTHON")
print("--------------------------------------------------")

# Entrada básica com input()
print("\n▶️ Entrada de texto com input()")
nome = input("Digite seu nome: ")
print("Olá,", nome)

print("--------------------------------------------------")

# Entrada numérica com casting
print("\n▶️ Entrada de número inteiro com int()")
idade = int(input("Digite sua idade: "))
print("Idade digitada:", idade)

print("--------------------------------------------------")

# Entrada de número float
print("\n▶️ Entrada de número float com float()")
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))
print(f"Peso: {peso} kg, Altura: {altura} m")

print("--------------------------------------------------")

# Entrada múltipla em uma linha
print("\n▶️ Entrada de múltiplos dados usando split()")
print("Digite dois números separados por espaço:")
x, y = map(int, input().split())
print("Você digitou x =", x, "e y =", y)

print("--------------------------------------------------")

# Entrada de lista de números
print("\n▶️ Entrada de lista de números (split + list comprehension)")
print("Digite vários números separados por espaço:")
numeros = [int(n) for n in input().split()]
print("Lista de números:", numeros)

print("--------------------------------------------------")

# Saída com formatação básica
print("\n▶️ Saída com f-strings")
pi = 3.1415926535
print(f"Valor de pi com 2 casas decimais: {pi:.2f}")

print("--------------------------------------------------")

# Saída com alinhamento
print("\n▶️ Impressão com alinhamento e largura fixa")
print(f"{'Produto':<10}{'Preço':>10}")
print(f"{'Maçã':<10}{2.5:>10.2f}")
print(f"{'Banana':<10}{1.89:>10.2f}")

print("--------------------------------------------------")

# Formatação de datas
print("\n▶️ Exibindo data e hora formatada")
agora = datetime.now()
print("Data e hora atuais:", agora)
print(f"Data formatada: {agora.strftime('%d/%m/%Y')}")
print(f"Hora formatada: {agora.strftime('%H:%M:%S')}")

print("--------------------------------------------------")

# Leitura de arquivo externo (simulando leitura de dados)
print("\n▶️ Leitura de dados de um arquivo (modo seguro)")
try:
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        print("Conteúdo do arquivo 'dados.txt':")
        for linha in arquivo:
            print(linha.strip())
except FileNotFoundError:
    print("Arquivo 'dados.txt' não encontrado.")

print("--------------------------------------------------")

# Escrita de dados em arquivo
print("\n▶️ Escrita de dados em arquivo")
with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha 1: Olá mundo!\n")
    arquivo.write("Linha 2: Escrevendo em arquivos com Python.\n")
print("Arquivo 'saida.txt' criado com sucesso.")

print("--------------------------------------------------")

# Redirecionando a saída padrão
print("\n▶️ Redirecionando saída para um arquivo usando sys.stdout")
original_stdout = sys.stdout  # Salva a referência original

with open("log_saida.txt", "w", encoding="utf-8") as f:
    sys.stdout = f  # Redireciona para o arquivo
    print("Esta linha vai para o arquivo log_saida.txt")
    print("Outro exemplo de log")
sys.stdout = original_stdout  # Restaura saída original
print("Saída foi redirecionada e restaurada com sucesso.")

print("--------------------------------------------------")

# Exemplo interativo: formulário simples
print("\n▶️ Mini formulário de cadastro")
nome = input("Nome: ")
email = input("Email: ")
idade = input("Idade: ")
print("\n🔎 Resumo do cadastro:")
print(f"Nome: {nome}\nEmail: {email}\nIdade: {idade}")

print("--------------------------------------------------")

# Entrada validada com loop
print("\n▶️ Entrada com validação e tratamento de erros")
while True:
    try:
        numero = int(input("Digite um número inteiro válido: "))
        print("Número válido:", numero)
        break
    except ValueError:
        print("❌ Isso não é um número inteiro. Tente novamente.")

print("✅ Fim da demonstração.")
