import re

# ----------------------------------------------
# 1. Remover caracteres especiais
texto = "Exemplo@# de limpeza!!! 123."
texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
print("1. Texto limpo:", texto_limpo)
# Regex: [^a-zA-Z0-9\s]
# Explicação: Remove tudo que NÃO seja letra, número ou espaço.

# ----------------------------------------------
# 2. Encontrar todos os e-mails no texto
texto = "Contato: maria@example.com e suporte@empresa.org"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
print("2. Emails encontrados:", emails)
# Regex: \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
# Explicação: Captura e-mails no padrão usuário@domínio.

# ----------------------------------------------
# 3. Encontrar todos os números
texto = "Temos 12 gatos, 5 cachorros e 2 coelhos."
numeros = re.findall(r'\d+', texto)
print("3. Números encontrados:", numeros)
# Regex: \d+
# Explicação: Encontra uma ou mais ocorrências de dígitos (0-9).

# ----------------------------------------------
# 4. Separar todas as palavras
texto = "Tokenização básica de palavras!"
palavras = re.findall(r'\b\w+\b', texto)
print("4. Palavras encontradas:", palavras)
# Regex: \b\w+\b
# Explicação: Captura palavras isoladas (alfa-numéricas).

# ----------------------------------------------
# 5. Remover espaços duplicados
texto = "Este   é  um    exemplo."
texto_corrigido = re.sub(r'\s+', ' ', texto)
print("5. Texto com espaços corrigidos:", texto_corrigido.strip())
# Regex: \s+
# Explicação: Substitui múltiplos espaços por apenas um.

# ----------------------------------------------
# 6. Encontrar hashtags
texto = "Amo #Python e #MachineLearning!"
hashtags = re.findall(r'#\w+', texto)
print("6. Hashtags encontradas:", hashtags)
# Regex: #\w+
# Explicação: Detecta palavras começando com '#'.

# ----------------------------------------------
# 7. Encontrar menções (@username)
texto = "Obrigado @usuario1 e @usuario2 pelo apoio!"
usuarios = re.findall(r'@\w+', texto)
print("7. Usuários mencionados:", usuarios)
# Regex: @\w+
# Explicação: Captura nomes de usuários mencionados com '@'.

# ----------------------------------------------
# 8. Encontrar palavras com letra maiúscula inicial
texto = "O Brasil é um país lindo."
palavras_maiusculas = re.findall(r'\b[A-Z][a-z]*\b', texto)
print("8. Palavras com inicial maiúscula:", palavras_maiusculas)
# Regex: \b[A-Z][a-z]*\b
# Explicação: Palavras que começam com letra maiúscula.

# ----------------------------------------------
# 9. Encontrar números decimais
texto = "O preço é 123.45 ou talvez 67.89."
decimais = re.findall(r'\d+\.\d+', texto)
print("9. Números decimais encontrados:", decimais)
# Regex: \d+\.\d+
# Explicação: Captura números no formato decimal (com ponto).

# ----------------------------------------------
# 10. Encontrar frases curtas (até 5 palavras)
texto = "A vida é bela. Estude bastante! Tudo passa."
frases_curtas = re.findall(r'([A-Z][^\.!?]{1,50}[\.!?])', texto)
print("10. Frases curtas:", frases_curtas)
# Regex: ([A-Z][^\.!?]{1,50}[\.!?])
# Explicação: Frases que começam em maiúscula e terminam em ., ! ou ? (máx 50 caracteres).

# ----------------------------------------------
# 11. Detectar URLs
texto = "Nosso site é https://www.exemplo.com e também http://outro.net"
urls = re.findall(r'https?://[^\s]+', texto)
print("11. URLs encontradas:", urls)
# Regex: https?://[^\s]+
# Explicação: Detecta URLs iniciando com http:// ou https://

# ----------------------------------------------
# 12. Extrair datas no formato DD/MM/AAAA
texto = "As datas são 15/04/2025 e 30/12/2024."
datas = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', texto)
print("12. Datas encontradas:", datas)
# Regex: \b\d{2}/\d{2}/\d{4}\b
# Explicação: Captura datas no formato dia/mês/ano.

# ----------------------------------------------
# 13. Encontrar palavras com 5 letras exatas
texto = "Hoje é um belo dia para andar no parque."
palavras_cinco_letras = re.findall(r'\b\w{5}\b', texto)
print("13. Palavras com 5 letras:", palavras_cinco_letras)
# Regex: \b\w{5}\b
# Explicação: Captura palavras com exatamente 5 letras.

# ----------------------------------------------
# 14. Encontrar tudo que está entre aspas
texto = 'Ele disse: "Aprenda Python" e também "Pratique sempre".'
entre_aspas = re.findall(r'"(.*?)"', texto)
print("14. Textos entre aspas:", entre_aspas)
# Regex: "(.*?)"
# Explicação: Captura o conteúdo dentro de aspas duplas.

# ----------------------------------------------
# 15. Verificar se o texto começa com letra maiúscula
texto = "Começar corretamente."
match = re.match(r'^[A-Z]', texto)
print("15. Começa com maiúscula?", bool(match))
# Regex: ^[A-Z]
# Explicação: Verifica se o primeiro caractere é uma letra maiúscula.

# ----------------------------------------------
