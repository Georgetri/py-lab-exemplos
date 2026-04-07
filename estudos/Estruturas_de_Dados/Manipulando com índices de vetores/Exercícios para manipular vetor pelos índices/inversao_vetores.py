"""        INVERSÃO DE VETOR
Ler um vetor e imprimir seus elementos na ordem inversa, sem usar reversed() nem [::-1].
Dica: percorra com for i in range(len(vetor) - 1, -1, -1).
Exemplo: Entrada: [1, 2, 3, 4]    Saída: [4, 3, 2, 1]   range(Básico_Início, parada, passo)
len(vetor) - 1	começa no último índice
-1 (parada no zero)	indica que deve parar antes de -1 → ou seja, chega até 0
-1 (passo)	anda para trás, decrementando 1 a cada vez
"""
vetor = [10, 20, 30, 40, 50, 60]
fim = len(vetor) - 1

for i in range(len(vetor)-1,-1,-1):
    print(f"índice:{i}: valor:{vetor[i]}")

print("-----------------")

for i in range(len(vetor)//2):
    aux = vetor[fim]
    vetor[fim] = vetor[i]
    vetor[i] = aux
    fim -= 1
print(*vetor)