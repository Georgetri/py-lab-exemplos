import re

# ----------------------------------------------
# 31. Encontrar abreviações (Sr., Dra., etc.)
texto = "Sr. João e Dra. Maria estão presentes."
abreviacoes = re.findall(r'\b[A-Z][a-z]{1,3}\.', texto)
print("31. Abreviações encontradas:", abreviacoes)
# Regex: \b[A-Z][a-z]{1,3}\.
# Explicação: Letra maiúscula + 1 a 3 letras minúsculas + ponto.

# ----------------------------------------------
# 32. Validar datas (DD/MM/AAAA)
datas = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', "Hoje é 27/04/2025.")
print("32. Datas encontradas:", datas)
# Regex: \b\d{2}/\d{2}/\d{4}\b
# Explicação: Dois dígitos + / + dois dígitos + / + quatro dígitos.

# ----------------------------------------------
# 33. Extrair hashtags
texto = "Falando sobre #Python e #MachineLearning!"
hashtags = re.findall(r'#\w+', texto)
print("33. Hashtags:", hashtags)
# Regex: #\w+
# Explicação: Um '#' seguido de letras, números ou underscores.

# ----------------------------------------------
# 34. Extrair menções (@usuario)
texto = "Contatos: @ana, @joao_dev."
mencoes = re.findall(r'@\w+', texto)
print("34. Menções:", mencoes)
# Regex: @\w+
# Explicação: Um '@' seguido de letras, números ou underscores.

# ----------------------------------------------
# 35. Encontrar unidades de medida (kg, cm, mL)
texto = "Preciso de 10kg de arroz e 500mL de leite."
medidas = re.findall(r'\d+\s?(kg|mL|cm|g)', texto)
print("35. Medidas encontradas:", medidas)
# Regex: \d+\s?(kg|mL|cm|g)
# Explicação: Número seguido de unidade (opcional espaço).

# ----------------------------------------------
# 36. Identificar emojis simples (unicode básico)
texto = "Hoje estou 😃! Amanhã talvez 😢."
emojis = re.findall(r'[\U0001F600-\U0001F64F]', texto)
print("36. Emojis encontrados:", emojis)
# Regex: [\U0001F600-\U0001F64F]
# Explicação: Emojis básicos de emoções (carinhas).

# ----------------------------------------------
# 37. Limpar texto para IA (apenas letras)
texto = "Modelo V2.0 está 90% concluído!!!"
texto_limpo = re.sub(r'[^A-Za-zÀ-ÖØ-öø-ÿ\s]', '', texto)
print("37. Texto limpo:", texto_limpo)
# Regex: [^A-Za-zÀ-ÖØ-öø-ÿ\s]
# Explicação: Remove tudo que não for letra ou espaço.

# ----------------------------------------------
# 38. Encontrar palavras negativas (não, jamais)
texto = "Ele não gostou e jamais voltará."
negativas = re.findall(r'\b(não|jamais|nunca|nenhum)\b', texto, flags=re.IGNORECASE)
print("38. Palavras negativas:", negativas)
# Regex: \b(não|jamais|nunca|nenhum)\b
# Explicação: Captura palavras negativas comuns.

# ----------------------------------------------
# 39. Capturar citações ("fala")
texto = 'Ele disse: "Aprender é importante".'
citacoes = re.findall(r'"([^"]+)"', texto)
print("39. Citações:", citacoes)
# Regex: "([^"]+)"
# Explicação: Texto entre aspas.

# ----------------------------------------------
# 40. Quebrar parágrafos por linha vazia
texto = "Primeiro parágrafo.\n\nSegundo parágrafo."
paragrafos = re.split(r'\n\s*\n', texto)
print("40. Parágrafos:", paragrafos)
# Regex: \n\s*\n
# Explicação: Divide por duas quebras de linha (parágrafo).

# ----------------------------------------------
# 41. Extrair pares chave:valor
texto = "nome:João idade:25 cidade:SP"
pares = re.findall(r'(\w+):(\w+)', texto)
print("41. Pares chave-valor:", pares)
# Regex: (\w+):(\w+)
# Explicação: Captura palavra + ':' + palavra.

# ----------------------------------------------
# 42. Validar IPs IPv4
texto = "O servidor está em 192.168.0.1 e o backup em 10.0.0.2."
ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', texto)
print("42. IPs encontrados:", ips)
# Regex: (?:\d{1,3}\.){3}\d{1,3}
# Explicação: Três números com pontos + número final.

# ----------------------------------------------
# 43. Encontrar placas de carro (Brasil novo padrão)
texto = "Meu carro é ABC1D23 e o outro é XYZ9K88."
placas = re.findall(r'\b[A-Z]{3}\d[A-Z]\d{2}\b', texto)
print("43. Placas encontradas:", placas)
# Regex: [A-Z]{3}\d[A-Z]\d{2}
# Explicação: Três letras + um número + uma letra + dois números.

# ----------------------------------------------
# 44. Encontrar palavras só em caixa alta (gritos)
texto = "ATENÇÃO: ESTE AVISO É IMPORTANTE!"
gritos = re.findall(r'\b[A-Z]{2,}\b', texto)
print("44. Palavras em caixa alta:", gritos)
# Regex: \b[A-Z]{2,}\b
# Explicação: Palavras com 2 ou mais letras maiúsculas.

# ----------------------------------------------
# 45. Filtrar nomes próprios (iniciais maiúsculas)
texto = "Maria foi à escola com João."
nomes = re.findall(r'\b[A-Z][a-z]+\b', texto)
print("45. Nomes próprios:", nomes)
# Regex: \b[A-Z][a-z]+\b
# Explicação: Letra maiúscula + sequência de minúsculas.

# ----------------------------------------------
# 46. Separar nomes compostos
texto = "Ana Clara e João Pedro são amigos."
nomes_compostos = re.findall(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b', texto)
print("46. Nomes compostos:", nomes_compostos)
# Regex: [A-Z][a-z]+\s[A-Z][a-z]+
# Explicação: Dois nomes com espaço entre eles.

# ----------------------------------------------
# 47. Detectar horários (ex: 23:45)
texto = "A reunião será às 14:30 e o almoço às 12:00."
horarios = re.findall(r'\b\d{2}:\d{2}\b', texto)
print("47. Horários:", horarios)
# Regex: \b\d{2}:\d{2}\b
# Explicação: Dois dígitos + ':' + dois dígitos.

# ----------------------------------------------
# 48. Extrair termos entre colchetes ou parênteses
texto = "Informações [confidenciais] (importantes)"
termos = re.findall(r'[\[\(](.*?)[\]\)]', texto)
print("48. Termos extraídos:", termos)
# Regex: [\[\(](.*?)[\]\)]
# Explicação: Captura texto dentro de () ou [].

# ----------------------------------------------
# 49. Encontrar textos com símbolos misturados
texto = "Senha segura: p@ssw0rd!"
misturados = re.findall(r'\b\w*[@#$%^&*]\w*\b', texto)
print("49. Palavras com símbolos:", misturados)
# Regex: \b\w*[@#$%^&*]\w*\b
# Explicação: Palavras que possuem pelo menos um símbolo especial.

# ----------------------------------------------
# 50. Capturar comentários simples em código
codigo = "// Este é um comentário\nvar x = 10; /* comentário */"
comentarios = re.findall(r'//.*?$|/\*.*?\*/', codigo, flags=re.DOTALL | re.MULTILINE)
print("50. Comentários encontrados:", comentarios)
# Regex: //.*?$|/\*.*?\*/
# Explicação: Captura comentários de uma linha (//) ou múltiplas linhas (/* */).

# ----------------------------------------------
