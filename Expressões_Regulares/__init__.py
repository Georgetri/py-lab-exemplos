import re

def validar_email():
    texto = input("Digite um texto com e-mails: ")
    padrao = r'\b[\w\.-]+@[\w\.-]+\.\w{2,}\b'
    resultado = re.findall(padrao, texto)
    print("\nE-mails encontrados:", resultado)

def validar_cpf():
    cpf = input("Digite um CPF (formato 000.000.000-00): ")
    if re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        print("CPF válido!")
    else:
        print("CPF inválido.")

def validar_telefone():
    telefone = input("Digite um telefone (formato (99) 91234-5678): ")
    if re.fullmatch(r'\(\d{2}\)\s9\d{4}-\d{4}', telefone):
        print("Telefone válido!")
    else:
        print("Telefone inválido.")

def remover_espacos():
    frase = input("Digite uma frase com muitos espaços: ")
    nova = re.sub(r'\s+', ' ', frase)
    print("Frase limpa:", nova)

def encontrar_nomes():
    texto = input("Digite um texto com nomes próprios: ")
    nomes = re.findall(r'\b[A-Z][a-z]+', texto)
    print("Nomes encontrados:", nomes)

def validar_senha():
    senha = input("Digite uma senha com letras e números (mínimo 6 caracteres): ")
    padrao = r'(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{6,}'
    if re.fullmatch(padrao, senha):
        print("Senha válida!")
    else:
        print("Senha inválida.")

def extrair_urls():
    texto = input("Digite um texto com URLs: ")
    urls = re.findall(r'https?://[^\s]+|www\.[^\s]+', texto)
    print("URLs encontradas:", urls)

def extrair_datas():
    texto = input("Digite um texto com datas (formato dd/mm/aaaa): ")
    datas = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', texto)
    print("Datas encontradas:", datas)

def extrair_numeros():
    texto = input("Digite um texto com números: ")
    numeros = re.findall(r'\d+', texto)
    print("Números encontrados:", numeros)

def encontrar_palavras_maiusculas():
    texto = input("Digite um texto: ")
    palavras = re.findall(r'\b[A-Z]{2,}\b', texto)
    print("Palavras em maiúsculas:", palavras)

def validar_placa_carro():
    placa = input("Digite a placa do carro (formato ABC-1234): ")
    if re.fullmatch(r'[A-Z]{3}-\d{4}', placa):
        print("Placa válida!")
    else:
        print("Placa inválida.")

def substituir_digitos():
    texto = input("Digite um texto com números: ")
    novo = re.sub(r'\d', '*', texto)
    print("Texto com números ocultados:", novo)

def separar_palavras():
    texto = input("Digite um texto: ")
    palavras = re.findall(r'\w+', texto)
    print("Palavras encontradas:", palavras)

def verificar_codigo_postal():
    cep = input("Digite o CEP (formato 12345-678): ")
    if re.fullmatch(r'\d{5}-\d{3}', cep):
        print("CEP válido!")
    else:
        print("CEP inválido.")

def extrair_hashtags():
    texto = input("Digite um texto com hashtags: ")
    hashtags = re.findall(r'#\w+', texto)
    print("Hashtags encontradas:", hashtags)

def menu():
    opcoes = {
        "1": ("Validar e extrair e-mails", validar_email),
        "2": ("Validar CPF", validar_cpf),
        "3": ("Validar telefone celular", validar_telefone),
        "4": ("Remover múltiplos espaços", remover_espacos),
        "5": ("Encontrar nomes próprios", encontrar_nomes),
        "6": ("Validar senha forte simples", validar_senha),
        "7": ("Extrair URLs", extrair_urls),
        "8": ("Extrair datas (dd/mm/aaaa)", extrair_datas),
        "9": ("Extrair números", extrair_numeros),
        "10": ("Palavras em maiúsculas", encontrar_palavras_maiusculas),
        "11": ("Validar placa de carro", validar_placa_carro),
        "12": ("Substituir dígitos por *", substituir_digitos),
        "13": ("Separar palavras do texto", separar_palavras),
        "14": ("Validar CEP (código postal)", verificar_codigo_postal),
        "15": ("Extrair hashtags", extrair_hashtags),
        "0": ("Sair", None)
    }

    while True:
        print("\n=== MENU EXPRESSÕES REGULARES ===")
        for k, v in opcoes.items():
            print(f"{k}. {v[0]}")
        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("Saindo...")
            break
        elif escolha in opcoes:
            opcoes[escolha][1]()  # Chama a função associada
        else:
            print("Opção inválida.")

# Executa o menu
if __name__ == "__main__":
    menu()
