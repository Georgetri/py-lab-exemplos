pessoas = []

n = int(input("Quantas pessoas deseja adicionar? "))

for i in range(n):
    nome = input(f"Nome da {i+1}ª pessoa: ")
    idade = int(input("Idade: "))
    pessoas.append({"nome": nome, "idade": idade})

print(pessoas)
