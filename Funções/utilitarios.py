
"""
Created on Sun Apr 27 18:38:46 2025
@author: jorge
"""

# Função soma: Recebe três números e retorna a soma deles.
def soma(a, b, c):
    """
    Função que recebe três números e retorna a soma deles.
    """
    somatorio = a + b + c
    return somatorio


# Função multiplicacao: Recebe três números e retorna o produto deles.
def multiplicacao(a, b, c):
    """
    Função que recebe três números e retorna o produto deles.
    """
    produto = a * b * c
    return produto


# Função isPalindromo: Verifica se uma string é um palíndromo (lê-se igual de trás pra frente).
def isPalindromo(string):
    """
    Função que verifica se uma string é um palíndromo.
    Um palíndromo é uma palavra, frase, número ou outro tipo de sequência
    que tem a mesma leitura, de trás para frente.
    """
    # Remover espaços e colocar a string em minúsculas para comparação
    string = string.replace(" ", "").lower()

    # Verifica se a string é igual a ela mesma invertida
    if string == string[::-1]:  # sequencia[início:fim:passo]
        return True
    else:
        return False


# Exemplo de uso das funções
if __name__ == "__main__":
    # Exemplo de soma
    num1 = 5
    num2 = 3
    num3 = 2
    print(f"Soma de {num1} + {num2} + {num3}: {soma(num1, num2, num3)}")

    # Exemplo de multiplicação
    print(f"Multiplicação de {num1} , {num2} e {num3}: {multiplicacao(num1, num2, num3)}")

    # Exemplo de verificação de palíndromo
    palavra = "arara"
    print(f"A palavra '{palavra}' é palíndromo? {isPalindromo(palavra)}")

    palavra2 = "python"
    print(f"A palavra '{palavra2}' é palíndromo? {isPalindromo(palavra2)}")