# processamento do [0-4] 
# for com range mostra os índices
for i in range(0,5): 
    print(i, end=" ")    


for num in range(4,-1,-1):
    print(num, end=" ")
    

soma = 0
for num in range(1,6): # Vai de 1 até 5
    soma += num
    print(num, end=" ")
print("\nsoma dos elementos do for:", soma)


palavra = 'sorvete'
for letra in palavra:
    print(letra, end=" ")
    if letra == 'e':
        print("\nAchou a letra E")


lista = [1,5,3,8]
for i, valor in enumerate(lista):
    print(f" lista[{i}] = {valor}")


# Aqui imprime os valores contidos na lista
# A lista transforma os inteiros em float se houver apenas 1 número float
valores_vendas = [250.0 , 480.0, 300] 
for i in valores_vendas:
    print(i)


# percorre ordenado
for valor in sorted([3, 1, 2]):
    print(valor)


# set remove duplicados ao iterar na lista
for valor in set([1,2,2,3,4]):
    print(valor,end=" ")


# iterando dicionário
cliente = {"nome": "Ana", "idade": 25}
for chave, valor in cliente.items():
    print(chave, valor)
    
