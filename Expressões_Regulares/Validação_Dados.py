import re


# ===== FUNÇÕES DOS EXEMPLOS - Validação de Dados =====

def validar_numeros_inteiros():
    texto = "Temos os números 45, -12 e 7890 aqui."
    numeros = re.findall(r'-?\d+', texto)
    print("\nCódigo:")
    print('texto = "Temos os números 45, -12 e 7890 aqui."\nnumeros = re.findall(r\'-?\\d+\', texto)\nprint(numeros)')
    print("\nResultado:")
    print(numeros)


def validar_numeros_decimais():
    texto = "Os preços são 4.50, 10.99 e 0.75 reais."
    numeros = re.findall(r'\d+\.\d+', texto)
    print("\nCódigo:")
    print(
        'texto = "Os preços são 4.50, 10.99 e 0.75 reais."\nnumeros = re.findall(r\'\\d+\\.\\d+\', texto)\nprint(numeros)')
    print("\nResultado:")
    print(numeros)


def validar_emails():
    texto = "Contate suporte@test.com ou vendas@example.org"
    emails = re.findall(r'\b[\w.-]+?@\w+?\.\w{2,4}\b', texto)
    print("\nCódigo:")
    print(
        'texto = "Contate suporte@test.com ou vendas@example.org"\nemails = re.findall(r\'\\b[\\w.-]+?@\\w+?\\.\\w{2,4}\\b\', texto)\nprint(emails)')
    print("\nResultado:")
    print(emails)


def validar_datas():
    texto = "Datas importantes: 12/05/2024, 01/01/2025."
    datas = re.findall(r'\d{2}/\d{2}/\d{4}', texto)
    print("\nCódigo:")
    print(
        'texto = "Datas importantes: 12/05/2024, 01/01/2025."\ndatas = re.findall(r\'\\d{2}/\\d{2}/\\d{4}\', texto)\nprint(datas)')
    print("\nResultado:")
    print(datas)


def validar_telefone():
    texto = "Ligue para (11)91234-5678 ou (21)99876-5432."
    telefones = re.findall(r'\(\d{2}\)\d{4,5}-\d{4}', texto)
    print("\nCódigo:")
    print(
        'texto = "Ligue para (11)91234-5678 ou (21)99876-5432."\ntelefones = re.findall(r\'\\(\\d{2}\\)\\d{4,5}-\\d{4}\', texto)\nprint(telefones)')
    print("\nResultado:")
    print(telefones)


def validar_cep():
    texto = "Endereço: Rua A, 12345-678 São Paulo."
    ceps = re.findall(r'\d{5}-\d{3}', texto)
    print("\nCódigo:")
    print('texto = "Endereço: Rua A, 12345-678 São Paulo."\nceps = re.findall(r\'\\d{5}-\\d{3}\', texto)\nprint(ceps)')
    print("\nResultado:")
    print(ceps)


def validar_senha_segura():
    senha = "Senha123!"
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    resultado = bool(re.match(padrao, senha))
    print("\nCódigo:")
    print(
        'senha = "Senha123!"\npadrao = r\'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&]).{8,}$\'\nresultado = bool(re.match(padrao, senha))\nprint(resultado)')
    print("\nResultado:")
    print(resultado)


def validar_ip():
    texto = "Servidor 192.168.0.1 online."
    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', texto)
    print("\nCódigo:")
    print(
        'texto = "Servidor 192.168.0.1 online."\nips = re.findall(r\'\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b\', texto)\nprint(ips)')
    print("\nResultado:")
    print(ips)


def validar_url():
    texto = "Acesse https://www.exemplo.com ou http://site.org"
    urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', texto)
    print("\nCódigo:")
    print(
        'texto = "Acesse https://www.exemplo.com ou http://site.org"\nurls = re.findall(r\'https?://(?:[-\\w.]|(?:%[\\da-fA-F]{2}))+\', texto)\nprint(urls)')
    print("\nResultado:")
    print(urls)


def validar_cpf():
    texto = "Meu CPF é 123.456.789-00."
    cpf = re.findall(r'\d{3}\.\d{3}\.\d{3}-\d{2}', texto)
    print("\nCódigo:")
    print(
        'texto = "Meu CPF é 123.456.789-00."\ncpf = re.findall(r\'\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}\', texto)\nprint(cpf)')
    print("\nResultado:")
    print(cpf)


# ===== MENU DE CATEGORIA - Validação de Dados =====

def menu_validacao_dados():
    while True:
        print("\n==== MENU: Validação de Dados ====")
        print("1 - Validar números inteiros")
        print("2 - Validar números decimais")
        print("3 - Validar emails")
        print("4 - Validar datas formato dd/mm/yyyy")
        print("5 - Validar telefones brasileiros")
        print("6 - Validar CEPs")
        print("7 - Validar senha segura")
        print("8 - Validar IPs")
        print("9 - Validar URLs")
        print("10 - Validar CPF")
        print("0 - Voltar ao menu principal")

        escolha = input("Escolha o número do exemplo: ")

        if escolha == "1":
            validar_numeros_inteiros()
        elif escolha == "2":
            validar_numeros_decimais()
        elif escolha == "3":
            validar_emails()
        elif escolha == "4":
            validar_datas()
        elif escolha == "5":
            validar_telefone()
        elif escolha == "6":
            validar_cep()
        elif escolha == "7":
            validar_senha_segura()
        elif escolha == "8":
            validar_ip()
        elif escolha == "9":
            validar_url()
        elif escolha == "10":
            validar_cpf()
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente!")


# ===== MENU PRINCIPAL =====

def menu_principal():
    while True:
        print("\n====== MENU DE CATEGORIAS ======")
        print("1 - Validação de Dados")
        print("2 - Análise e Extração de Texto (em construção)")
        print("3 - Limpeza de Texto para IA (em construção)")
        print("4 - Extração de Informações Complexas (em construção)")
        print("5 - Detecção de Emojis e Símbolos (em construção)")
        print("0 - Sair")

        escolha = input("Digite o número da categoria desejada: ")

        if escolha == "1":
            menu_validacao_dados()
        elif escolha == "0":
            print("Programa encerrado.")
            break
        else:
            print("Categoria ainda não disponível ou inválida.")


# ===== EXECUÇÃO =====

if __name__ == "__main__":
    menu_principal()
