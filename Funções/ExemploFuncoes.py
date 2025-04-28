"""
Created on Sun Apr 27 19:18:43 2025
@author: jorge
"""
# Desafio 1: Função para verificar se um número é primo
def is_prime(n):
    """Verifica se um número é primo."""
    if n <= 1:
        return False  # Números menores que ou iguais a 1 não são primos
    for i in range(2, int(n ** 0.5) + 1):  # Verifica até a raiz quadrada de n
        if n % i == 0:
            return False  # Se for divisível por qualquer número, não é primo
    return True  # Se não encontrou divisores, é primo

# Desafio 2: Função para contar as vogais em uma string
def count_vowels(string):
    """Conta as vogais em uma string."""
    vowels = "aeiouAEIOU"  # Definimos as vogais (minúsculas e maiúsculas)
    count = 0
    for char in string:
        if char in vowels:  # Verifica se o caractere é uma vogal
            count += 1  # Se for, incrementa o contador
    return count

# Desafio 3: Função que retorna a sequência de Fibonacci até o n-ésimo termo
def fibonacci(n):
    """Retorna a sequência de Fibonacci até o n-ésimo termo."""
    fib_sequence = [0, 1]  # Inicia com os dois primeiros termos
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])  # Soma os dois anteriores
    return fib_sequence

# Desafio 4: Função para calcular o fatorial de um número
def factorial(n):
    """Calcula o fatorial de um número n (n!)."""
    if n == 0 or n == 1:  # Caso base: fatorial de 0 ou 1 é 1
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiplica os números de 1 até n
    return result

# Desafio 5: Função para verificar se uma palavra é um palíndromo
def is_palindrome(word):
    """Verifica se uma palavra é um palíndromo."""
    word = word.replace(" ", "").lower()  # Remove espaços e coloca tudo em minúsculo
    return word == word[::-1]  # Compara a palavra com a versão invertida dela

# Desafio 6: Função para encontrar o maior número em uma lista
def find_max(lst):
    """Encontra o maior número em uma lista."""
    max_num = lst[0]  # Assume que o primeiro número é o maior
    for num in lst:
        if num > max_num:  # Se encontrar um número maior, atualiza max_num
            max_num = num
    return max_num

# Desafio 7: Função para ordenar uma lista em ordem crescente
def sort_list(lst):
    """Ordena uma lista de números em ordem crescente."""
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:  # Se o elemento i for maior que j, troca
                lst[i], lst[j] = lst[j], lst[i]
    return lst

# Desafio 8: Função para verificar se um número é perfeito
def is_perfect_number(n):
    """Verifica se um número é perfeito."""
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])  # Soma os divisores de n
    return divisors_sum == n  # Um número perfeito é igual à soma de seus divisores

# Desafio 9: Função para gerar uma matriz transposta
def transpose_matrix(matrix):
    """Gera a transposta de uma matriz."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # A transposta troca as linhas com as colunas da matriz original.

# Desafio 10: Função para verificar se uma string é um anagrama de outra
def is_anagram(str1, str2):
    """Verifica se duas strings são anagramas uma da outra."""
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())
    # Remove espaços, coloca em minúsculas e compara as versões ordenadas das duas strings.

# Desafio 11: Função para encontrar o segundo maior número em uma lista
def second_largest(lst):
    """Encontra o segundo maior número em uma lista."""
    unique_lst = list(set(lst))  # Remove elementos duplicados
    unique_lst.sort()  # Ordena a lista
    if len(unique_lst) > 1:
        return unique_lst[-2]  # Retorna o segundo maior
    return None  # Retorna None se não houver um segundo maior número

# Desafio 12: Função para contar as ocorrências de cada elemento em uma lista
def count_occurrences(lst):
    """Conta as ocorrências de cada elemento em uma lista."""
    occurrences = {}
    for item in lst:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences

# Função principal para testar as funções
def main():
    print("Desafio 1 - Número Primo:")
    print(is_prime(7))  # Testando se 7 é primo

    print("\nDesafio 2 - Contar Vogais:")
    print(count_vowels("Hello World"))  # Contando as vogais em "Hello World"

    print("\nDesafio 3 - Sequência de Fibonacci:")
    print(fibonacci(10))  # Gerando os primeiros 10 termos da sequência de Fibonacci

    print("\nDesafio 4 - Fatorial:")
    print(factorial(5))  # Calculando o fatorial de 5

    print("\nDesafio 5 - Palíndromo:")
    print(is_palindrome("A man a plan a canal Panama"))  # Verificando se a frase é um palíndromo

    print("\nDesafio 6 - Maior Número em uma Lista:")
    print(find_max([3, 5, 7, 2, 8, 6]))  # Encontrando o maior número na lista

    print("\nDesafio 7 - Ordenação de Lista:")
    print(sort_list([3, 1, 4, 1, 5, 9]))  # Ordenando a lista de números

    print("\nDesafio 8 - Número Perfeito:")
    print(is_perfect_number(6))  # Verificando se 6 é um número perfeito

    print("\nDesafio 9 - Matriz Transposta:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose_matrix(matrix))  # Transposta de uma matriz 3x3

    print("\nDesafio 10 - Anagramas:")
    print(is_anagram("listen", "silent"))  # Verificando se "listen" e "silent" são anagramas

    print("\nDesafio 11 - Segundo Maior Número:")
    print(second_largest([3, 5, 7, 2, 8, 6]))  # Encontrando o segundo maior número na lista

    print("\nDesafio 12 - Contagem de Ocorrências:")
    print(count_occurrences([1, 2, 2, 3, 3, 3, 4, 4]))  # Contando as ocorrências de cada número

# Chamando a função principal
if __name__ == "__main__":
    main()
