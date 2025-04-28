idade = int(input("Digite a idade do usuario: "))

if idade < 0:
    print("Idade inválida")
else:
    if idade >= 0 and idade <= 12:
        print("O usuário é uma criança")
    elif 13 >= idade < 18:
        print("O usuário é adolescente")
    else:
        print("O usuário é um adulto")





#         elif 600 <= score_credito < 700: # o score de crédito está entre 600 e 699