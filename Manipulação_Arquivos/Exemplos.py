# Função para ler arquivo linha por linha
def ler_arquivo_linha_a_linha(caminho):
    print(f"\n📄 Lendo {caminho} linha por linha:")
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                print(linha.strip())
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")

# Função para ler arquivo com readlines
def ler_arquivo_com_readlines(caminho):
    print(f"\n📚 Lendo todas as linhas de {caminho} com readlines():")
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            print(linhas)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")

# Função para criar um arquivo de texto simples
def criar_texto(caminho, conteudo):
    print(f"\n📝 Criando o arquivo {caminho}")
    with open(caminho, 'w', encoding='utf-8') as texto:
        texto.write(conteudo)
    print("Arquivo criado com sucesso.")

# Função para ler o conteúdo de um arquivo de texto simples
def ler_texto(caminho):
    print(f"\n📖 Lendo o conteúdo de {caminho}:")
    try:
        with open(caminho, 'r', encoding='utf-8') as texto:
            for linha in texto:
                print(linha.strip())
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho}")

# Função para salvar uma lista em arquivo
def salvar_lista_em_arquivo(caminho, lista):
    print(f"\n💾 Salvando lista em {caminho}")
    with open(caminho, 'w', encoding='utf-8') as f:
        for item in lista:
            f.write(f"{item}\n")

# Função para salvar um dicionário em arquivo (chave: valor)
def salvar_dicionario_em_arquivo(caminho, dicionario):
    print(f"\n💾 Salvando dicionário em {caminho}")
    with open(caminho, 'w', encoding='utf-8') as f:
        for chave, valor in dicionario.items():
            f.write(f"{chave}: {valor}\n")

# Função para salvar uma tupla em arquivo
def salvar_tupla_em_arquivo(caminho, tupla):
    print(f"\n💾 Salvando tupla em {caminho}")
    with open(caminho, 'w', encoding='utf-8') as f:
        for item in tupla:
            f.write(f"{item}\n")

# Função principal
def main():
    # Caminhos (ajuste se necessário)
    caminho_salmo = 'C:/Users/jorge/PycharmProjects/PythonProject/Manipulação_Arquivos/Salmo_23'
    texto_simples = 'texto.txt'
    arquivo_lista = 'lista.txt'
    arquivo_dict = 'dicionario.txt'
    arquivo_tupla = 'tupla.txt'

    # Funções com arquivos de texto simples
    ler_arquivo_linha_a_linha(caminho_salmo)
    ler_arquivo_com_readlines(caminho_salmo)

    # Criar e ler um arquivo simples
    criar_texto(texto_simples, "Olá a todos")
    ler_texto(texto_simples)

    # Exemplos com estruturas de dados
    minha_lista = ["maçã", "banana", "laranja"]
    meu_dicionario = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
    minha_tupla = ("Python", "Java", "C++")

    salvar_lista_em_arquivo(arquivo_lista, minha_lista)
    salvar_dicionario_em_arquivo(arquivo_dict, meu_dicionario)
    salvar_tupla_em_arquivo(arquivo_tupla, minha_tupla)

    # Ler o conteúdo que foi salvo (opcional)
    ler_texto(arquivo_lista)
    ler_texto(arquivo_dict)
    ler_texto(arquivo_tupla)

# Execução do programa
if __name__ == "__main__":
    main()
