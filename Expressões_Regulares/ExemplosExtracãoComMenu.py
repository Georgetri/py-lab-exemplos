import re

def extrair_emails():
    texto = 'Contate-nos em suporte@example.com ou vendas@empresa.org.'
    resultado = re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', texto)
    print(resultado)

def extrair_numeros_inteiros():
    texto = 'Hoje temos 23 alunos e 7 professores.'
    resultado = re.findall(r'\b\d+\b', texto)
    print(resultado)

def extrair_numeros_decimais():
    texto = 'O preço é 12.50 reais e a taxa é 0.99.'
    resultado = re.findall(r'\b\d+\.\d+\b', texto)
    print(resultado)

def extrair_ceps_com_hifen():
    texto = 'Meu CEP é 12345-678 e o da empresa é 98765-432.'
    resultado = re.findall(r'\b\d{5}-\d{3}\b', texto)
    print(resultado)

def extrair_ceps_sem_hifen():
    texto = 'Informe seu CEP: 12345678 ou 87654321.'
    resultado = re.findall(r'\b\d{8}\b', texto)
    print(resultado)

def extrair_urls_http_https():
    texto = 'Acesse http://example.com ou https://secure.site.org para mais informações.'
    resultado = re.findall(r'https?://[^\s]+', texto)
    print(resultado)

def extrair_urls_com_www():
    texto = 'Visite www.exemplo.com e também https://site.com.br.'
    resultado = re.findall(r'(https?://|www\.)[^\s]+', texto)
    print(resultado)

def extrair_telefones():
    texto = 'Me ligue em (11) 91234-5678 ou (21) 99876-5432.'
    resultado = re.findall(r'\(\d{2}\)\s\d{5}-\d{4}', texto)
    print(resultado)

def extrair_placas_veiculo():
    texto = 'As placas são ABC-1234 e XYZ-9876.'
    resultado = re.findall(r'\b[A-Z]{3}-\d{4}\b', texto)
    print(resultado)

def extrair_cpf():
    texto = 'CPF válido: 123.456.789-00 e outro: 987.654.321-99.'
    resultado = re.findall(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b', texto)
    print(resultado)

def extrair_cnpj():
    texto = 'Empresa registrada com CNPJ: 12.345.678/0001-95.'
    resultado = re.findall(r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b', texto)
    print(resultado)

def extrair_hashtags():
    texto = 'Tópicos: #Python #Regex #Programação'
    resultado = re.findall(r'#\w+', texto)
    print(resultado)

def extrair_mencoes():
    texto = 'Mensagem para @joao e @maria no Instagram.'
    resultado = re.findall(r'@\w+', texto)
    print(resultado)

def extrair_datas():
    texto = 'As datas são 28/04/2025 e 01/01/2026.'
    resultado = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', texto)
    print(resultado)

def extrair_horarios():
    texto = 'A reunião será às 14:30 ou às 09:45.'
    resultado = re.findall(r'\b\d{2}:\d{2}\b', texto)
    print(resultado)

def extrair_zipcode_americano():
    texto = 'Endereços: 90210 e 12345-6789.'
    resultado = re.findall(r'\b\d{5}(?:-\d{4})?\b', texto)
    print(resultado)

def extrair_palavras_maiusculas():
    texto = 'Olá Mundo Bom Dia Programador'
    resultado = re.findall(r'\b[A-Z][a-z]*\b', texto)
    print(resultado)

def extrair_arquivos_imagem():
    texto = 'Fotos: imagem1.jpg banner.png logo.gif'
    resultado = re.findall(r'\b\w+\.(jpg|png|gif)\b', texto)
    print(resultado)

def extrair_palavras_terminadas_em_acao():
    texto = 'A programação é uma paixão que leva à inovação.'
    resultado = re.findall(r'\b\w+ção\b', texto)
    print(resultado)

def extrair_texto_entre_aspas():
    texto = 'Ele disse: "Vamos aprender Regex" e ela respondeu: "Claro!"'
    resultado = re.findall(r'"([^"]+)"', texto)
    print(resultado)

def menu():
    while True:
        print("\n--- Menu Regex ---")
        print("1 - Extrair e-mails")
        print("2 - Extrair números inteiros")
        print("3 - Extrair números decimais")
        print("4 - Extrair CEPs com hífen")
        print("5 - Extrair CEPs sem hífen")
        print("6 - Extrair URLs (http/https)")
        print("7 - Extrair URLs (com www)")
        print("8 - Extrair telefones")
        print("9 - Extrair placas de veículos")
        print("10 - Extrair CPF")
        print("11 - Extrair CNPJ")
        print("12 - Extrair hashtags")
        print("13 - Extrair menções (@usuario)")
        print("14 - Extrair datas (DD/MM/AAAA)")
        print("15 - Extrair horários (HH:MM)")
        print("16 - Extrair código postal americano")
        print("17 - Extrair palavras com inicial maiúscula")
        print("18 - Extrair arquivos de imagem (jpg, png, gif)")
        print("19 - Extrair palavras terminadas com 'ção'")
        print("20 - Extrair textos entre aspas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            extrair_emails()
        elif opcao == '2':
            extrair_numeros_inteiros()
        elif opcao == '3':
            extrair_numeros_decimais()
        elif opcao == '4':
            extrair_ceps_com_hifen()
        elif opcao == '5':
            extrair_ceps_sem_hifen()
        elif opcao == '6':
            extrair_urls_http_https()
        elif opcao == '7':
            extrair_urls_com_www()
        elif opcao == '8':
            extrair_telefones()
        elif opcao == '9':
            extrair_placas_veiculo()
        elif opcao == '10':
            extrair_cpf()
        elif opcao == '11':
            extrair_cnpj()
        elif opcao == '12':
            extrair_hashtags()
        elif opcao == '13':
            extrair_mencoes()
        elif opcao == '14':
            extrair_datas()
        elif opcao == '15':
            extrair_horarios()
        elif opcao == '16':
            extrair_zipcode_americano()
        elif opcao == '17':
            extrair_palavras_maiusculas()
        elif opcao == '18':
            extrair_arquivos_imagem()
        elif opcao == '19':
            extrair_palavras_terminadas_em_acao()
        elif opcao == '20':
            extrair_texto_entre_aspas()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
