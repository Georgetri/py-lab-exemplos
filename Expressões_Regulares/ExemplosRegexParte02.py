import re

# ----------------------------------------------
# 16. Remover HTML tags de um texto
texto = "<p>Este é um <b>exemplo</b> com HTML.</p>"
texto_sem_html = re.sub(r'<[^>]+>', '', texto)
print("16. Texto sem HTML:", texto_sem_html)
# Regex: <[^>]+>
# Explicação: Remove qualquer conteúdo entre '<' e '>' (tags HTML).

# ----------------------------------------------
# 17. Encontrar códigos postais (CEP formato brasileiro)
texto = "Endereço: Rua X, 123 - CEP: 12345-678."
ceps = re.findall(r'\b\d{5}-\d{3}\b', texto)
print("17. CEP encontrado:", ceps)
# Regex: \b\d{5}-\d{3}\b
# Explicação: Captura CEP no formato 00000-000.

# ----------------------------------------------
# 18. Validar número de telefone (formato brasileiro com DDD)
texto = "Contatos: (11) 91234-5678 ou (21) 2233-4455."
telefones = re.findall(r'\(\d{2}\)\s?\d{4,5}-\d{4}', texto)
print("18. Telefones encontrados:", telefones)
# Regex: \(\d{2}\)\s?\d{4,5}-\d{4}
# Explicação: Captura números de telefone com DDD, com ou sem 9º dígito.

# ----------------------------------------------
# 19. Encontrar palavras repetidas seguidas (ex: "muito muito")
texto = "Ele está muito muito feliz!"
repetidas = re.findall(r'\b(\w+)\s+\1\b', texto, flags=re.IGNORECASE)
print("19. Palavras repetidas:", repetidas)
# Regex: \b(\w+)\s+\1\b
# Explicação: Captura palavras que se repetem em sequência (case-insensitive).

# ----------------------------------------------
# 20. Remover links de um texto
texto = "Confira em https://site.com ou http://outro.com agora."
texto_sem_links = re.sub(r'https?://[^\s]+', '', texto)
print("20. Texto sem links:", texto_sem_links.strip())
# Regex: https?://[^\s]+
# Explicação: Remove URLs que começam com http ou https.

# ----------------------------------------------
# 21. Extrair domínios de e-mails
texto = "Emails: ana@gmail.com, joao@empresa.com.br"
dominios = re.findall(r'@([\w.-]+)', texto)
print("21. Domínios de e-mails:", dominios)
# Regex: @([\w.-]+)
# Explicação: Captura a parte após o '@' (domínio).

# ----------------------------------------------
# 22. Encontrar palavras que terminam com "mente" (advérbios em PT-BR)
texto = "Ele falou calmamente e claramente."
adverbios = re.findall(r'\b\w+mente\b', texto)
print("22. Advérbios encontrados:", adverbios)
# Regex: \b\w+mente\b
# Explicação: Captura palavras terminadas com "mente".

# ----------------------------------------------
# 23. Encontrar valores monetários (R$)
texto = "Os preços são R$ 10,00 e R$ 1500.50."
valores = re.findall(r'R\$\s?\d{1,3}(?:[\.,]\d{3})*[\.,]\d{2}', texto)
print("23. Valores encontrados:", valores)
# Regex: R\$\s?\d{1,3}(?:[\.,]\d{3})*[\.,]\d{2}
# Explicação: Captura valores monetários com vírgula ou ponto como separador decimal.

# ----------------------------------------------
# 24. Extrair palavras que contenham números (ex: "modelo3", "v2")
texto = "Versões: modelo3, v2, teste, data2025."
palavras_numeros = re.findall(r'\b\w*\d+\w*\b', texto)
print("24. Palavras com números:", palavras_numeros)
# Regex: \b\w*\d+\w*\b
# Explicação: Captura palavras que têm pelo menos um número.

# ----------------------------------------------
# 25. Identificar palavras duplicadas não consecutivas
texto = "Hoje é hoje e amanhã será amanhã."
duplicadas = re.findall(r'\b(\w+)\b(?=.*\b\1\b)', texto, flags=re.IGNORECASE)
print("25. Palavras duplicadas:", set(duplicadas))
# Regex: \b(\w+)\b(?=.*\b\1\b)
# Explicação: Encontra palavras que aparecem mais de uma vez (não necessariamente seguidas).

# ----------------------------------------------
# 26. Remover números de um texto
texto = "Casa 123, rua ABC 456."
texto_sem_numeros = re.sub(r'\d+', '', texto)
print("26. Texto sem números:", texto_sem_numeros.strip())
# Regex: \d+
# Explicação: Remove todos os dígitos.

# ----------------------------------------------
# 27. Encontrar siglas (2 ou mais letras maiúsculas)
texto = "O modelo foi treinado com dados da NASA e da OMS."
siglas = re.findall(r'\b[A-Z]{2,}\b', texto)
print("27. Siglas encontradas:", siglas)
# Regex: \b[A-Z]{2,}\b
# Explicação: Captura palavras com duas ou mais letras maiúsculas.

# ----------------------------------------------
# 28. Dividir texto por pontuação (tokenizar sentenças)
texto = "Olá! Tudo bem? Vamos aprender regex. É divertido."
sentencas = re.split(r'[.!?]\s*', texto)
print("28. Sentenças:", [s for s in sentencas if s])
# Regex: [.!?]\s*
# Explicação: Divide o texto por ., ! ou ? seguido de espaços.

# ----------------------------------------------
# 29. Encontrar palavras com letras repetidas (ex: "cooool")
texto = "Isso é cooool e incrííível!"
repetidas_letras = re.findall(r'\b\w*(\w)\1\1\w*\b', texto)
print("29. Palavras com letras repetidas:", repetidas_letras)
# Regex: \b\w*(\w)\1\1\w*\b
# Explicação: Captura palavras com pelo menos três letras repetidas consecutivas.

# ----------------------------------------------
# 30. Validar senhas fortes (mínimo 8 caracteres, letra maiúscula, minúscula e número)
senhas = ["SenhaFraca", "Forte123", "Senha@2025"]
for senha in senhas:
    valida = re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', senha)
    print(f"30. Senha '{senha}' é forte?", bool(valida))
# Regex: ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$
# Explicação: Verifica se a senha tem pelo menos 8 caracteres, uma letra minúscula, uma maiúscula e um número.

# ----------------------------------------------
