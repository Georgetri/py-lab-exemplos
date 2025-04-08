
# Imprimindo uma string
print("Olá, mundo!")  # Exibe a frase "Olá, mundo!" no console

# Concatenando strings
nome = "Maria"
sobrenome = "Silva"
print(nome + " " + sobrenome)  # Maria Silva

# Repetindo uma string
print("python " * 3)  # python python python

# Descobrindo o tamanho da string
print(len("Jorge"))  # 5

# Deixando todos os caracteres maiúsculos
print("python".upper())  # PYTHON

# Deixando todos os caracteres minúsculos
print("PYTHON".lower())  # python

# Capitalizando a primeira letra
print("python".capitalize())  # Python

# Trocando partes da string
print("banana".replace("a", "o"))  # bonono

# Verificando se um texto está contido na string
print("grama" in "programação")  # True
print("java" in "programação")  # False

# Verificando se a string começa ou termina com algo
print("banana".startswith("ba"))  # True
print("banana".endswith("na"))    # True

# Removendo espaços extras nas pontas
print("   texto com espaços   ".strip())  # "texto com espaços"

# Fatiando uma string (slicing)
texto = "programação"
print(texto[0:5])   # progr (do índice 0 ao 4)
print(texto[:4])    # prog (início até o 3)
print(texto[5:])    # amação (do índice 5 até o final)
print(texto[-1])    # ã (último caractere)
print(texto[-3:])   # ção (últimos 3 caracteres)

# Quebrando string por espaços (split)
frase = "Python é incrível"
print(frase.split())  # ['Python', 'é', 'incrível']

# Unindo listas de string com separador
palavras = ['Python', 'é', 'top']
print(" ".join(palavras))  # Python é top

# Formatação moderna com f-strings
nome = "João"
idade = 25
print(f"{nome} tem {idade} anos.")  # João tem 25 anos.

# Formatando com números
pi = 3.14159265
print(f"Valor de PI: {pi:.2f}")  # Valor de PI: 3.14

# Contando quantas vezes um caractere aparece
print("banana".count("a"))  # 3

# Encontrando a posição de uma substring
print("banana".find("na"))  # 2 (índice da primeira ocorrência)

# Verificando se a string é numérica
print("123".isdigit())  # True
print("abc123".isdigit())  # False

# Verificando se a string é alfabética
print("abc".isalpha())  # True
print("abc123".isalpha())  # False

# Verificando se a string é alfanumérica
print("abc123".isalnum())  # True

# Centralizando texto
print("Python".center(20, "-"))  # -------Python-------

# Alinhando texto à direita ou esquerda
print("Python".rjust(10))  # "    Python"
print("Python".ljust(10))  # "Python    "

# Convertendo string para lista de caracteres
print(list("python"))  # ['p', 'y', 't', 'h', 'o', 'n']

# Substituindo múltiplos espaços por hífens
mensagem = "texto com    vários   espaços"
print(" ".join(mensagem.split()))  # texto com vários espaços
print("-".join(mensagem.split()))  # texto-com-vários-espaços
