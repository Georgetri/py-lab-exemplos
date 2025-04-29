import re

# E-mail simples
print(re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',
                 'Contate-nos em suporte@example.com ou vendas@empresa.org.'))
# ['suporte@example.com', 'vendas@empresa.org']

# Número inteiro
print(re.findall(r'\b\d+\b', 'Hoje temos 23 alunos e 7 professores.'))
# ['23', '7']

# Número decimal
print(re.findall(r'\b\d+\.\d+\b', 'O preço é 12.50 reais e a taxa é 0.99.'))
# ['12.50', '0.99']

# CEP brasileiro (formato 00000-000)
print(re.findall(r'\b\d{5}-\d{3}\b', 'Meu CEP é 12345-678 e o da empresa é 98765-432.'))
# ['12345-678', '98765-432']

# CEP brasileiro sem hífen (formato 00000000)
print(re.findall(r'\b\d{8}\b', 'Informe seu CEP: 12345678 ou 87654321.'))
# ['12345678', '87654321']

# URL começando com http ou https
print(re.findall(r'https?://[^\s]+', 'Acesse http://example.com ou https://secure.site.org para mais informações.'))
# ['http://example.com', 'https://secure.site.org']

# URL básica (aceita www também)
print(re.findall(r'(https?://|www\.)[^\s]+', 'Visite www.exemplo.com e também https://site.com.br.'))
# ['www.exemplo.com', 'https://site.com.br']

# Telefone brasileiro (formato (00) 00000-0000)
print(re.findall(r'\(\d{2}\)\s\d{5}-\d{4}', 'Me ligue em (11) 91234-5678 ou (21) 99876-5432.'))
# ['(11) 91234-5678', '(21) 99876-5432']

# Placa de carro brasileira antiga (ABC-1234)
print(re.findall(r'\b[A-Z]{3}-\d{4}\b', 'As placas são ABC-1234 e XYZ-9876.'))
# ['ABC-1234', 'XYZ-9876']

# CPF brasileiro (000.000.000-00)
print(re.findall(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b', 'CPF válido: 123.456.789-00 e outro: 987.654.321-99.'))
# ['123.456.789-00', '987.654.321-99']

# CNPJ brasileiro (00.000.000/0000-00)
print(re.findall(r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b', 'Empresa registrada com CNPJ: 12.345.678/0001-95.'))
# ['12.345.678/0001-95']

# Hashtag em redes sociais
print(re.findall(r'#\w+', 'Tópicos: #Python #Regex #Programação'))
# ['#Python', '#Regex', '#Programação']

# Menção de usuário (@usuario)
print(re.findall(r'@\w+', 'Mensagem para @joao e @maria no Instagram.'))
# ['@joao', '@maria']

# Data no formato DD/MM/AAAA
print(re.findall(r'\b\d{2}/\d{2}/\d{4}\b', 'As datas são 28/04/2025 e 01/01/2026.'))
# ['28/04/2025', '01/01/2026']

# Horário no formato HH:MM
print(re.findall(r'\b\d{2}:\d{2}\b', 'A reunião será às 14:30 ou às 09:45.'))
# ['14:30', '09:45']

# Código postal americano (ZIP code: 5 dígitos ou 5+4 dígitos)
print(re.findall(r'\b\d{5}(?:-\d{4})?\b', 'Endereços: 90210 e 12345-6789.'))
# ['90210', '12345-6789']

# Palavras que começam com letra maiúscula
print(re.findall(r'\b[A-Z][a-z]*\b', 'Olá Mundo Bom Dia Programador'))
# ['Olá', 'Mundo', 'Bom', 'Dia', 'Programador']

# Arquivos de imagem (jpg, png, gif)
print(re.findall(r'\b\w+\.(jpg|png|gif)\b', 'Fotos: imagem1.jpg banner.png logo.gif'))
# ['jpg', 'png', 'gif']

# Palavra que termina com "ção"
print(re.findall(r'\b\w+ção\b', 'A programação é uma paixão que leva à inovação.'))
# ['programação', 'paixão', 'inovação']

# Extraindo palavras entre aspas
print(re.findall(r'"([^"]+)"', 'Ele disse: "Vamos aprender Regex" e ela respondeu: "Claro!"'))
# ['Vamos aprender Regex', 'Claro!']
