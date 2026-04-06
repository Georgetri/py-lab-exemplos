# Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo,
# crie uma estrutura de repetição para percorrer cada elemento do dicionário para gravar cada aluno em um novo arquivo de texto
# – Cada aluno deve ocupar uma linha do novo arquivo de texto
# – O formato deve ser: nome,nota (Pedro,8.0)
# – Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

# for aluno, nota in alunos.items():
#     print(f"Aluno:{aluno},nota:{nota}")

with open("alunos.txt",'w') as arquivo:
    for aluno, nota in alunos.items():
        arquivo.write(f'{aluno},{nota}\n')

with open("alunos.txt","r") as arquivo:
    for linha in arquivo:
        print(linha)