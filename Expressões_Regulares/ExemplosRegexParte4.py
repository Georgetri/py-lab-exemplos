import re

# === EXEMPLO 1: Usando re.search para encontrar a primeira correspondência ===
def busca_primeiro_email():
    # O método re.search encontra o primeiro email válido no texto
    texto = "Meu email é exemplo@dominio.com e outro email é outro@dominio.com."
    resultado = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', texto)
    print("\nCódigo:")
    print('resultado = re.search(r\'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b\', texto)')
    if resultado:
        print("Resultado:", resultado.group())
    else:
        print("Nenhum email encontrado.")

# === EXEMPLO 2: Usando re.match para verificar se o texto começa com um padrão ===
def verifica_inicio_palavra():
    # O método re.match verifica se o padrão ocorre no início do texto
    texto = "Olá, como você está?"
    resultado = re.match(r'Olá', texto)
    print("\nCódigo:")
    print('resultado = re.match(r\'Olá\', texto)')
    if resultado:
        print("Resultado:", resultado.group())
    else:
        print("O texto não começa com 'Olá'.")

# === EXEMPLO 3: Usando re.sub para substituições no texto ===
def substitui_emails():
    # O método re.sub substitui todos os emails encontrados por '[email protegido]'
    texto = "Entre em contato com contato@exemplo.com ou suporte@exemplo.com."
    novo_texto = re.sub(r'[\w\.-]+@[\w\.-]+', '[email protegido]', texto)
    print("\nCódigo:")
    print('novo_texto = re.sub(r\'[\\w\\.-]+@[\\w\\.-]+\', \'[email protegido]\', texto)')
    print("Texto substituído:", novo_texto)

# === EXEMPLO 4: Usando re.split para dividir uma string com base em um padrão ===
def divide_texto():
    # O método re.split divide a string em partes usando o padrão de separação
    texto = "Python, Java, C, C++"
    partes = re.split(r',\s*', texto)  # Divide pelo delimitador de vírgula com espaço opcional
    print("\nCódigo:")
    print('partes = re.split(r\',\\s*\', texto)')
    print("Resultado:", partes)

# === EXEMPLO 5: Usando re.sub para remover espaços extras ===
def remove_espacos_extras():
    # O método re.sub remove os espaços extras, substituindo múltiplos espaços por um único
    texto = "   Este   texto   tem  espaços   extras.  "
    texto_limpo = re.sub(r'\s+', ' ', texto).strip()
    print("\nCódigo:")
    print('texto_limpo = re.sub(r\'\\s+\', \' \', texto).strip()')
    print("Texto sem espaços extras:", texto_limpo)

# === EXEMPLO 6: Usando re.search para validar um CPF (com a máscara) ===
def valida_cpf():
    # O método re.search verifica se o CPF está no formato correto
    texto = "Meu CPF é 123.456.789-10"
    resultado = re.search(r'\d{3}\.\d{3}\.\d{3}-\d{2}', texto)
    print("\nCódigo:")
    print('resultado = re.search(r\'\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}\', texto)')
    if resultado:
        print("CPF encontrado:", resultado.group())
    else:
        print("CPF inválido ou não encontrado.")

# === EXEMPLO 7: Usando re.match para validar um número de telefone ===
def valida_telefone():
    # O método re.match verifica se o telefone está no formato correto
    texto = "(11) 98765-4321"
    resultado = re.match(r'\(\d{2}\)\s?\d{5}-\d{4}', texto)
    print("\nCódigo:")
    print('resultado = re.match(r\'\\(\\d{2}\\)\\s?\\d{5}-\\d{4}\', texto)')
    if resultado:
        print("Telefone válido:", resultado.group())
    else:
        print("Telefone inválido ou não encontrado.")

# === EXEMPLO 8: Usando re.sub para limpar tags HTML ===
def remove_tags_html():
    # O método re.sub remove todas as tags HTML do texto
    texto = "<p>Este é um <b>exemplo</b> de texto com <a href='#'>link</a>.</p>"
    texto_limpo = re.sub(r'<[^>]*>', '', texto)
    print("\nCódigo:")
    print('texto_limpo = re.sub(r\'<[^>]*>\', \'\', texto)')
    print("Texto sem tags HTML:", texto_limpo)

# === EXEMPLO 9: Usando re.search para verificar um nome de domínio ===
def verifica_dominio():
    # O método re.search verifica se o domínio está no formato correto
    texto = "O site é www.exemplo.com.br"
    resultado = re.search(r'\b(?:[a-z0-9-]+\.)+[a-z]{2,}\b', texto)
    print("\nCódigo:")
    print('resultado = re.search(r\'\\b(?:[a-z0-9-]+\\.)+[a-z]{2,}\\b\', texto)')
    if resultado:
        print("Domínio encontrado:", resultado.group())
    else:
        print("Domínio não encontrado.")

# Função principal para exibir todos os exemplos
def executar_exemplos():
    busca_primeiro_email()       # Exemplo 1
    verifica_inicio_palavra()    # Exemplo 2
    substitui_emails()           # Exemplo 3
    divide_texto()               # Exemplo 4
    remove_espacos_extras()      # Exemplo 5
    valida_cpf()                 # Exemplo 6
    valida_telefone()            # Exemplo 7
    remove_tags_html()           # Exemplo 8
    verifica_dominio()           # Exemplo 9

# Executa todos os exemplos
if __name__ == "__main__":
    executar_exemplos()
