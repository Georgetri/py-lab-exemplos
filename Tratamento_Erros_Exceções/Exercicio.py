lista = []
print("Digite dois números decimais para preencher a lista:")

while len(lista) < 2:
    try:
        num = float(input(f"Insira o {len(lista)+1}º número decimal: "))
    except ValueError as e:
        print("Erro, valor não pode ser convertido:", e)
    except ZeroDivisionError as e:
        print(f"Erro: divisão por zero não é permitida! ({e})")
    except IndexError as e:
        print(f"Erro: índice fora dos limites da lista! ({e})")
    except KeyboardInterrupt:
        print("\nUsuário interrompeu a execução")
        break
    else:
        lista.append(num)
        print("Número adicionado com sucesso!")

# Tenta fazer a divisão dos dois números após preencher a lista
if len(lista) == 2:
    try:
        resultado = lista[0] / lista[1]
    except ZeroDivisionError as e:
        print(f"Erro: divisão por zero não é permitida! ({e})")
    else:
        print(f"\nResultado da divisão: {lista[0]} / {lista[1]} = {resultado}")
else:
    print("\nA lista não foi preenchida corretamente. Divisão não realizada.")


print("\nLista final:", lista[0], lista[1])
