"""
Desafio 6 – Troca de posições pares e ímpares
Leia um vetor de N elementos e troque os valores das posições pares com os das ímpares.
Exemplo: [10, 20, 30, 40, 50, 60] → [20, 10, 40, 30, 60, 50]
Dica: use range(0, len(vetor) - 1, 2) para avançar de dois em dois índices.
"""
vetor = [10,20,30,40,50,60]
vetor2 = [100,200,300,400,500,600]
aux = 0
i = 0
while i < len(vetor)-1:
    aux = vetor[i]
    vetor[i] = vetor[i+1]
    vetor[i+1] = aux
    i += 2
print(vetor)

print("-"*25)

i = 0
for _ in vetor2:      # percorre só para contar iterações, não usa elemento diretamente
    if i < len(vetor2) - 1:
        aux = vetor2[i]
        vetor2[i] = vetor2[i + 1]
        vetor2[i + 1] = aux
    i += 2           # avança de dois em dois para pegar o próximo par

print(vetor2)

