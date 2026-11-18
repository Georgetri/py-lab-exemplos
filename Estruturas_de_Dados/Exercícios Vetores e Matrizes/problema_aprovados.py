""" USAR LISTA COM DICIONÁRIO
Fazer um programa para ler um conjunto de N nomes de alunos, bem como as notas que eles tiraram
no 1º e 2º semestres. Cada uma dessas informações deve ser armazenada em uma lista com dicionário.
Depois, imprimir os nomes dos alunos aprovados, considerando aprovados aqueles cuja média
das notas seja maior ou igual a 6.0 (seis). Exemplo: Digite nome, primeira e segunda nota do 1o aluno:
Joao Silva   7.0   8.5    """

alunos = []

while True:
    num = int(input("Quantos alunos serão registrados? digite entre [1-4] :"))
    if 1 <= num <= 4:
        break
    print("⚠️ Número fora do intervalo. Tente novamente.")

# Prenchendo o dicionário dentro do vetor alunos (lista em python)
for i in range(num):
    nome = input("Digite o nome do aluno:")
    nota_1 = float(input(f"Digite a 1ª nota do aluno(a) {nome}:"))
    nota_2 = float(input(f"Digite a 2ª nota do aluno(a) {nome}:"))
    media = round((nota_1 + nota_2) / 2 , 1)
    alunos.append({'nome':nome,'nota_1':nota_1,'nota_2':nota_2,'media':media})

# Imprimindo a lista de dicionários :<10 e :<5 são usados para alinhamento
for aluno in alunos:
    print(f"Aluno(a):{aluno['nome']:<5}" 
          f"1ª nota:{aluno['nota_1']:<5}" 
          f"2ª nota:{aluno['nota_2']:<5}"
          f"média:{aluno['media']:.1f}")

# Imprime somente alunos aprovados com média >= 6.0
# Lembrando que se acessa os valores do dicionário pela sua chave
print("\nAlunos aprovados:")
for aluno in alunos:
    if aluno['media'] >= 6:
        print(f"Aluno(a):{aluno['nome']} aprovado com média:{aluno['media']:.1f}")






