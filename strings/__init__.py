python = 'Hello, Word'
print(python)

maiuscula = python.upper()
print(maiuscula)

minuscula = maiuscula.lower()
print(minuscula)

primeira_maiuscula = minuscula.capitalize()
print(primeira_maiuscula)

metade_palavra = python[0:5]
print(metade_palavra)

ultimas_letras = python[7:]
print(ultimas_letras)

a = 'casaco'
b = a.replace('aco','inha')
c = a.replace('o','a')
print(a,b,c)
print(a.find('s'))
print(len(a))

j = ' amigo '
print('Conta o tamanho da string com espaço:',len(j))
f = j.strip()
print('strip() Tira o espaço da string antes e depois:',len(f))

n1 = 14
n2 = 16

print(f'Dividindo {n1} por {n2} = {n1/n2}')
