"""  Diferença entre vizinhos
Ler N números inteiros e gerar outro vetor onde cada elemento é a diferença absoluta entre dois vizinhos.
Exemplo: [5, 8, 3, 7] → [|8-5|, |3-8|, |7-3|] → [3, 5, 4]
Dica: use range(len(vetor) - 1) para acessar pares consecutivos.
"""
vetor = [5,8,3,7]
diferenca = []

for i in range(len(vetor) - 1):  # range(3)
    """
        O índice 3 existe no vetor, mas não deve ser usado como i porque 
        o algoritmo acessa também i+1, e isso causaria erro.
        Por isso o range para em i=2. 0,1,2 Se o range fosse até o 3, 
        o código iria tentar acessar o índice 4 [i+1] que não existe
    """
    x = vetor[i]
    y = vetor[i+1]
    aux = 0
    if x > y:
        aux = y
        y = x
        x = aux
    diferenca.append(y - x)

print(diferenca)


