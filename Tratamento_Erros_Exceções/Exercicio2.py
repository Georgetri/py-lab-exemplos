lista = []

try:
    lista.append(float(input(f"Insira o {len(lista) + 1}º número decimal: ")))
    lista.append(float(input(f"Insira o {len(lista) + 1}º número decimal: ")))
    divisao = lista[0] / lista[1]
except ValueError as e:
    print("Erro, valor não pode ser convertido:", e)
except ZeroDivisionError as e:
    print(f"Erro: divisão por zero não é permitida! ({e})")
except IndexError as e:
    print(f"Erro: índice fora dos limites da lista! ({e})")
except KeyboardInterrupt:
    print("\nUsuário interrompeu a execução")
else:
    print(f"Lista completa : [{lista[0]}  {lista[1]}]")
    print(f"Valor da divisão: ",round(divisao,2))
