import re


# ===== FUNÇÕES DOS EXEMPLOS - Análise e Extração de Texto =====

def extrair_hashtags():
    texto = "Confira as últimas postagens: #Python #Regex #IA"
    hashtags = re.findall(r'#\w+', texto)
    print("\nCódigo:")
    print(
        'texto = "Confira as últimas postagens: #Python #Regex #IA"\nhashtags = re.findall(r\'#\\w+\', texto)\nprint(hashtags)')
    print("\nResultado:")
    print(hashtags)


def extrair_mencao():
    texto = "Olha o comentário de @usuario1 e @usuario2 sobre o código!"
    mencoes = re.findall(r'@\w+', texto)
    print("\nCódigo:")
    print(
        'texto = "Olha o comentário de @usuario1 e @usuario2 sobre o código!"\nmencoes = re.findall(r\'@\\w+\', texto)\nprint(mencoes)')
    print("\nResultado:")
    print(mencoes)


def extrair_unidades():
    texto = "O comprimento é de 12 km, a área é de 40 m² e o peso 20 kg."
    unidades = re.findall(r'\d+\s?(km|m²|kg|cm|g)', texto)
    print("\nCódigo:")
    print(
        'texto = "O comprimento é de 12 km, a área é de 40 m² e o peso 20 kg."\nunidades = re.findall(r\'\\d+\\s?(km|m²|kg|cm|g)\', texto)\nprint(unidades)')
    print("\nResultado:")
    print(unidades)


def palavras_maiusculas():
    texto = "Aqui temos algumas PALAVRAS em maiúsculas e outras minúsculas."
    palavras = re.findall(r'\b[A-Z]+\b', texto)
    print("\nCódigo:")
    print(
        'texto = "Aqui temos algumas PALAVRAS em maiúsculas e outras minúsculas."\npalavras = re.findall(r\'\\b[A-Z]+\\b\', texto)\nprint(palavras)')
    print("\nResultado:")
    print(palavras)


def extrair_urls():
    texto = "Acesse nosso site https://www.exemplo.com ou http://site.org para mais informações."
    urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', texto)
    print("\nCódigo:")
    print(
        'texto = "Acesse nosso site https://www.exemplo.com ou http://site.org para mais informações."\nurls = re.findall(r\'https?://(?:[-\\w.]|(?:%[\\da-fA-F]{2}))+\', texto)\nprint(urls)')
    print("\nResultado:")
    print(urls)


def extrair_telefone_comercial():
    texto = "Ligue para (11)1234-5678 ou (21)9876-5432 para saber mais."
    telefones = re.findall(r'\(\d{2}\)\d{4,5}-\d{4}', texto)
    print("\nCódigo:")
    print(
        'texto = "Ligue para (11)1234-5678 ou (21)9876-5432 para saber mais."\ntelefones = re.findall(r\'\\(\\d{2}\\)\\d{4,5}-\\d{4}\', texto)\nprint(telefones)')
    print("\nResultado:")
    print(telefones)


def capturar_citacoes():
    texto = "Ela disse: 'Vamos estudar Regex!' e ele respondeu: 'Com certeza!'"
    citacoes = re.findall(r"'([^']+)'", texto)
    print("\nCódigo:")
    # Aqui, escapamos as barras invertidas e usamos a string de forma clara
    print('texto = "Ela disse: \'Vamos estudar Regex!\' e ele respondeu: \'Com certeza!\'"')
    print('citacoes = re.findall(r"\'([^\\\']+)\'", texto)')
    print("\nResultado:")
    print(citacoes)


def extrair_palavras_com_underscore():
    texto = "A variável minha_variavel tem o valor 10, e outra_variavel tem o valor 20."
    palavras = re.findall(r'\w+_\w+', texto)
    print("\nCódigo:")
    print(
        'texto = "A variável minha_variavel tem o valor 10, e outra_variavel tem o valor 20."\npalavras = re.findall(r\'\\w+_\\w+\', texto)\nprint(palavras)')
    print("\nResultado:")
    print(palavras)


def extrair_versao_software():
    texto = "A versão do software é 2.3.4, e a versão beta é 3.0.0-beta."
    versao = re.findall(r'\d+\.\d+\.\d+(-beta)?', texto)
    print("\nCódigo:")
    print(
        'texto = "A versão do software é 2.3.4, e a versão beta é 3.0.0-beta."\nversao = re.findall(r\'\\d+\\.\\d+\\.\\d+(-beta)?\', texto)\nprint(versao)')
    print("\nResultado:")
    print(versao)


def capturar_pares_chave_valor():
    texto = "A chave de acesso é ABC123 e a chave de autenticação é XYZ456."
    pares = re.findall(r'(\w+)\s*=\s*(\w+)', texto)
    print("\nCódigo:")
    print(
        'texto = "A chave de acesso é ABC123 e a chave de autenticação é XYZ456."\npares = re.findall(r\'(\\w+)\\s*=\\s*(\\w+)\', texto)\nprint(pares)')
    print("\nResultado:")
    print(pares)


# ===== MENU DE CATEGORIA - Análise e Extração de Texto =====

def menu_analise_texto():
    while True:
        print("\n==== MENU: Análise e Extração de Texto ====")
        print("1 - Extrair Hashtags")
        print("2 - Extrair Menções (@usuário)")
        print("3 - Extrair Unidades de Medida")
        print("4 - Encontrar Palavras em Maiúsculas")
        print("5 - Extrair URLs")
        print("6 - Extrair Telefones Comerciais")
        print("7 - Capturar Citações")
        print("8 - Extrair Palavras com Underscore")
        print("9 - Extrair Versões de Software")
        print("10 - Capturar Pares Chave:Valor")
        print("0 - Voltar ao menu principal")

        escolha = input("Escolha o número do exemplo: ")

        if escolha == "1":
            extrair_hashtags()
        elif escolha == "2":
            extrair_mencao()
        elif escolha == "3":
            extrair_unidades()
        elif escolha == "4":
            palavras_maiusculas()
        elif escolha == "5":
            extrair_urls()
        elif escolha == "6":
            extrair_telefone_comercial()
        elif escolha == "7":
            capturar_citacoes()
        elif escolha == "8":
            extrair_palavras_com_underscore()
        elif escolha == "9":
            extrair_versao_software()
        elif escolha == "10":
            capturar_pares_chave_valor()
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente!")

