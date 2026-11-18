"""
    Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo.
    Depois, mostrar na tela a altura média das pessoas, e mostrar também a porcentagem
    de pessoas com menos de 16 anos, bem como os nomes dessas pessoas caso houver.
"""
pessoas = []
soma_altura = 0.0
cont_idade = 0

while True:
    num: int = int(input("Quantas pessoas serão cadastradas [1-5]:"))
    if 1 <= num <= 5:
        break
    print("⚠️ Número fora do intervalo. Tente novamente.")

i: int
for i in range(num):
    print("===== Cadastro de Pessoas =====")
    nome = input("Digite o nome:")
    idade = int(input(f"Digite a idade do(a) {nome}:"))
    altura = float(input(f"Digite a altura do(a) {nome}:"))

    pessoa = {"nome":nome , "idade":idade, "altura":altura}
    pessoas.append(pessoa)
    soma_altura += altura

    if idade < 16:
        cont_idade += 1

media = soma_altura / num

print("="*15, "PESSOAS CADASTRADAS","="*15)
for i in range(len(pessoas)):
    p = pessoas[i]
    print(f"{i+1}. Nome:{p['nome']} , Idade:{p['idade']} anos, Altura:{p['altura']}m")



print(f"Altura média das pessoas: {media:.2f}m")
print(f"Porcentagem de pessoas com menos de 16 anos: {(cont_idade/num * 100):.1f}%")