import unicodedata
import re
from collections import Counter
import json

# 1. Remover acentos de uma string
print("1. Remover acentos:")
def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    )

texto = "Olá, você está bem?"
print("Texto original:", texto)
print("Texto sem acentos:", remover_acentos(texto))
print("-------------------------")

# 2. Sanitizar input do usuário
print("2. Sanitizar input:")
entrada = "   João Da SILVA  "
entrada = entrada.strip().lower().title()
print("Entrada formatada:", entrada)  # João Da Silva
print("-------------------------")

# 3. Validar formato simples de e-mail
print("3. Validar e-mail:")
def email_valido(email):
    return "@" in email and "." in email.split("@")[-1]

print("exemplo@email.com é válido?", email_valido("exemplo@email.com"))
print("emailsemarroba.com é válido?", email_valido("emailsemarroba.com"))
print("-------------------------")

# 4. Extrair números de um texto
print("4. Extrair números:")
texto = "Pedido nº 12345 enviado em 03/04/2025"
numeros = re.findall(r'\d+', texto)
print("Números encontrados:", numeros)
print("-------------------------")

# 5. Encontrar palavras com letra maiúscula
print("5. Palavras com maiúsculas:")
frase = "Hoje João e Maria foram ao Parque da Cidade"
palavras = re.findall(r'\b[A-Z][a-z]*\b', frase)
print("Palavras com maiúscula:", palavras)
print("-------------------------")

# 6. Contar frequência de palavras
print("6. Frequência de palavras:")
texto = "python é bom e Python é divertido porque Python é simples"
print(texto)
palavras = texto.lower().split()
contagem = Counter(palavras)
print("Contagem:", contagem)
print("-------------------------")

# 7. Interpolar string com .format()
print("7. Interpolação com .format():")
template = "Olá, {nome}. Você tem {pontos} pontos no sistema."
mensagem = template.format(nome="Carlos", pontos=150)
print(mensagem)
print("-------------------------")

# 8. Gerar slug de URL
print("8. Gerar slug:")
def gerar_slug(texto):
    texto = remover_acentos(texto)
    texto = texto.lower()
    texto = re.sub(r'[^a-z0-9\s-]', '', texto)
    texto = re.sub(r'[\s\-]+', '-', texto).strip('-')
    return texto

print("Slug gerado:", gerar_slug("Título do Post: Python é top!"))
print("-------------------------")

# 9. Limpar texto para salvar em arquivo
print("9. Limpar texto:")
texto = "   Texto com \n quebra de linha \t e tabulação   "
texto = texto.strip().replace("\n", " ").replace("\t", " ")
print("Texto limpo:", texto)
print("-------------------------")

# 10. Converter string JSON em dicionário
print("10. JSON <-> dicionário:")
json_str = '{"nome": "Lucas", "idade": 30}'
dicionario = json.loads(json_str)
print("Nome no JSON:", dicionario["nome"])
json_str_convertido = json.dumps(dicionario, indent=2)
print("JSON formatado:")
print(json_str_convertido)
print("-------------------------")
