""" === CADASTRO DE VEÍCULOS USANDO LISTAS COM DICIONÁRIOS """

veiculos = []

while True:
    print("\n ===🚙 CADASTRO DE VEÍCULOS 🚗 === ")
    marca = input("Marca:")
    cor = input("Cor: ")
    ano = int(input("Ano de fabricação: "))
    km = float(input("Quilometragem(km):"))

    # Criar um dicionário com os dados informados
    carro = {
        "marca":marca,
        "cor":cor,
        "ano":ano,
        "km":km
    }

    # Adicionar o dicionário na lista
    veiculos.append(carro)

    # Pergunta se o usuário quer continuar a cadastrar veículos
    continuar = int(input("Cadastrar + veículos?[1=SIM|0=NÃO]:"))
    if not continuar: break

# Exibir os veículos cadastrados
print("\n ===== 🚙 LISTA DE VEÍCULOS CADASTRADOS 🚗 =====")
print(f"{'Nº':<3} {'MARCA':<10} {'COR':<10} {'ANO':<2} {'KM':>6}")

for i,c in enumerate(veiculos, start=1):
    print(f"{i}. {c['marca']:<10} {c['cor']:<10} {c['ano']:<6} {c['km']:<12}")



""" 
texto = 'ABC'
print(f" '{texto:<10}' ")  # esquerda
print(f" '{texto:>10}' ")  # direita
print(f" '{texto:^10}' ")  # centralizado

"""






