M1 = float(input("Insira a primeira nota: "))
M2 = float(input("Insira a segunda nota: "))
M3 = float(input("Insira a terceira nota: "))

media = (M1 + M2 + M3) / 3

if media > 4.0 and media < 6.0:
    print("Aluno pegou exame")
    nota_exame = float(input("Insira a nota do exame:"))
    if nota_exame > 6.0:
        print("Aluno aprovado")
    else:
        print("O aluno foi reprovado")
else:
    if media <= 4.0:
        print("O aluno foi reprovado")
    else:
        print("O aluno está aprovado")

