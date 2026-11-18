""""   Ler 5 números e dizer qual é o maior e o menor. """""

vetor = []
maior , menor = 0 , 0

for i in range(5):
    valor = int(input(f"Entre com o {i + 1}º número: "))
    vetor.append(valor)

    if i == 0:      # Esta condição será testada apenas no 1º loop, quando o contador i = 0; Abaixo, todas as variáveis são uniformizados os seus valores
        maior = menor = valor   # Em python, a atribuição encadeada é da direita para a esquerda: A variável valor atribui para menor que atribui para maior.
    else:
        if valor < menor:
            menor = valor

        if valor > maior:
            maior = valor

print(f"Vetor: {vetor}")
print(f"Maior:{maior} , Menor:{menor}")







