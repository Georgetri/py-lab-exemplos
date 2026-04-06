"""
Troca de posições pares e ímpares
Leia um vetor de N elementos e troque os valores das posições pares com os das ímpares.
Por exemplo:[10, 20, 30, 40, 50, 60] → [20, 10, 40, 30, 60, 50].
Dica: use range(0, len(vetor) - 1, 2) para avançar de dois em dois índices. range(início, fim, passo)
for i in range(0, len(vetor) - 1, 2):
    vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
"""
vetor = [10, 20, 30, 40, 50, 60]

for i in range(0, len(vetor) - 1, 2):   # range(Básico_Início,fim,passo)
    aux = vetor[i]            # guarda o valor da posição atual (par)
    vetor[i] = vetor[i + 1]   # substitui o valor da posição atual pelo da próxima
    vetor[i + 1] = aux       # agora a próxima posição recebe o valor guardado

print(vetor)
