def divide(a, b):
    """
    Tenta dividir dois números. Trata erro de divisão por zero.

    Parâmetros:
    - a: numerador
    - b: denominador

    Exceções tratadas:
    - ZeroDivisionError: ocorre quando b é 0
    """
    try:
        result = a / b
        print(f"Resultado da divisão: {result}")
    except ZeroDivisionError as e:
        print(f"Erro: divisão por zero não é permitida! ({e})")


def access_list_element(my_list, index):
    """
    Tenta acessar um elemento de uma lista pelo índice.

    Parâmetros:
    - my_list: lista de elementos
    - index: posição a ser acessada

    Exceções tratadas:
    - IndexError: ocorre quando o índice não existe na lista
    """
    try:
        print(f"Elemento no índice {index}: {my_list[index]}")
    except IndexError as e:
        print(f"Erro: índice fora dos limites da lista! ({e})")


def use_undefined_variable():
    """
    Simula o uso de uma variável não definida.

    Exceções tratadas:
    - NameError: ocorre quando tentamos usar uma variável que não foi declarada
    """
    try:
        print(valor_que_nao_existe)  # Vai gerar NameError
    except NameError as e:
        print(f"Erro: variável não definida! ({e})")


def converter_para_inteiro(valor):
    try:
        numero = int(valor)
        print(f"Conversão bem-sucedida: {numero}")
        return numero
    except ValueError as e:
        print("Erro de valor:", e)
        return None


def add_numbers(a, b):
    """
    Tenta somar dois valores.

    Parâmetros:
    - a, b: valores a serem somados

    Exceções tratadas:
    - TypeError: ocorre quando os tipos são incompatíveis (ex: int + str)
    """
    try:
        result = a + b
        print(f"Soma: {result}")
    except TypeError as e:
        print(f"Erro: tipos incompatíveis para soma! ({e})")


def trigger_runtime_error():
    """
    Dispara manualmente um erro de tempo de execução.

    Exceções tratadas:
    - RuntimeError: erro genérico que pode ser usado para simular falhas
    """
    try:
        raise RuntimeError("Erro em tempo de execução simulado!")
    except RuntimeError as e:
        print(f"Erro de execução: {e}")


def simulate_syntax_error():
    """
    Simula um erro de sintaxe usando eval().

    Exceções tratadas:
    - SyntaxError: erro de sintaxe em tempo de avaliação dinâmica
    - Exception: usado como fallback para capturar erros gerais (inclui SyntaxError em eval)
    """
    try:
        eval("x === x")  # Erro de sintaxe proposital
    except SyntaxError as e:
        print(f"Erro de sintaxe! ({e})")
    except Exception as e:
        print(f"Erro geral ao avaliar código com erro de sintaxe: {e}")


def main():
    """
    Função principal que executa todas as funções de teste.
    """
    print("== Teste de divisão ==")
    divide(10, 0)

    print("\n== Teste de índice inválido ==")
    lista = [1, 2, 3]
    access_list_element(lista, 5)

    print("\n== Teste de variável indefinida ==")
    use_undefined_variable()

    print("\n== Teste de tipos incompatíveis ==")
    add_numbers(5, "dez")

    print("\n== Teste de erro em tempo de execução ==")
    trigger_runtime_error()

    print("\n== Teste de erro de sintaxe ==")
    simulate_syntax_error()

    print("\n== Teste converter String para Inteiro ==")
    converter_para_inteiro("abc")


# Início da execução do programa
if __name__ == "__main__":
    main()
