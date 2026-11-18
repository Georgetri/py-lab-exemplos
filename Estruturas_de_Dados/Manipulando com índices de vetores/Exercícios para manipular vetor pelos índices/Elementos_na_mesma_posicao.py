"""
    Ler dois vetores A e B do mesmo tamanho e gerar um vetor C com os elementos que são iguais e estão na mesma posição nos dois.
    Exemplo: A = [1, 3, 5, 7, 9] B = [1, 4, 5, 6, 9] C = [1, 5, 9]
    Dica: percorra com for i in range(len(A)): e compare A[i] == B[i].
"""
A = [1, 3, 5, 7, 9]
B = [1, 4, 5, 6, 9]
C = []
for i in range(len(A)):
    if A[i] == B[i]:
        C.append(A[i])

print(C)

