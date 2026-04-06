"""
    Crie um programa que leia um vetor de N números e desloque todos os elementos
    uma posição à direita, fazendo com que o último elemento vá para o início.
    Exemplo: Entrada: [10, 20, 30, 40, 50]   Saída:   [50, 10, 20, 30, 40]
    • Pense que o índice 0 vai receber o último elemento (len(vetor) - 1),
    • e cada elemento vetor[i] vai passar para a posição i + 1.
"""
vetor = [10,20,30,40,50]
"""
    print("Preencha o vetor com 5 números inteiros:")
    for i in range(5):
        vetor.append(int(input(f"Insira o {i+1}º número: ")))
"""
tam = len(vetor)
i = tam - 1
aux = vetor[tam-1]

for _ in vetor:
    if i > 0 :
      vetor[i] = vetor[i-1]
      i -= 1
    else:
        break
vetor[0] = aux

print(vetor,end=" ")



"""
    vetor = []
    i = 0
    while len(vetor) < 5:
        vetor.append(int(input(f"Insira o {i+1}º número: ")))
        i += 1
    
    print("Vetor preenchido:", vetor)
"""