import re

# . (ponto) - qualquer caractere exceto nova linha
print(re.findall(r'a.c', 'abc a9c a#c acc a c'))
# ['abc', 'a9c', 'a#c', 'acc']

# ^ (início da string)
print(re.findall(r'^Olá', 'Olá mundo! Olá de novo!'))
# ['Olá']

# $ (fim da string)
print(re.findall(r'mundo!$', 'Olá mundo! Este é o mundo!'))
# ['mundo!']

# * (zero ou mais repetições)
print(re.findall(r'ab*c', 'ac abc abbc abbbc'))
# ['ac', 'abc', 'abbc', 'abbbc']

# + (uma ou mais repetições)
print(re.findall(r'ab+c', 'ac abc abbc abbbc'))
# ['abc', 'abbc', 'abbbc']

# ? (zero ou uma vez)
print(re.findall(r'ab?c', 'ac abc abbc abbbc'))
# ['ac', 'abc']

# {n} (exatamente n repetições)
print(re.findall(r'a{3}', 'aa aaa aaaa aaaaa'))
# ['aaa', 'aaa', 'aaa']

# {n,} (pelo menos n repetições)
print(re.findall(r'a{2,}', 'a aa aaa aaaa'))
# ['aa', 'aaa', 'aaaa']

# {n,m} (entre n e m repetições)
print(re.findall(r'a{2,3}', 'a aa aaa aaaa'))
# ['aa', 'aaa', 'aa']

# [] (colchetes - conjunto de caracteres)
print(re.findall(r'[aeiou]', 'Python é ótimo!'))
# ['o', 'e', 'o', 'i', 'o']

# [^] (negação - qualquer caractere que NÃO esteja no conjunto)
print(re.findall(r'[^aeiou ]', 'Python é ótimo!'))
# ['P', 'y', 't', 'h', 'n', 'é', 't', 'm', '!']

# | (OU lógico)
print(re.findall(r'cachorro|gato', 'Eu tenho um cachorro e um gato.'))
# ['cachorro', 'gato']

# () (agrupamento)
print(re.findall(r'(ha)+', 'haha hahahaha ha'))
# ['ha', 'ha', 'ha']

# \d (qualquer dígito)
print(re.findall(r'\d+', 'Hoje é dia 29 de abril de 2025'))
# ['29', '2025']

# \D (qualquer caractere que não seja dígito)
print(re.findall(r'\D+', '123abc456def'))
# ['abc', 'def']

# \w (qualquer caractere alfanumérico ou "_")
print(re.findall(r'\w+', 'Olá_mundo123!'))
# ['Olá_mundo123']

# \W (qualquer caractere não alfanumérico)
print(re.findall(r'\W+', 'Olá mundo! Como vai?'))
# [' ', '!', ' ', ' ', '?']

# \s (qualquer espaço em branco)
print(re.findall(r'\s+', 'Linha 1\nLinha 2\tLinha 3'))
# ['\n', '\t']

# \S (qualquer caractere que não seja espaço em branco)
print(re.findall(r'\S+', 'Espaço e\ttexto\nmais texto'))
# ['Espaço', 'e', 'texto', 'mais', 'texto']

# \. (ponto literal)
print(re.findall(r'\.', 'exemplo.com outro.exemplo'))
# ['.', '.']
