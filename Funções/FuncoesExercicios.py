
def fahrenheit(celsius):
    f = (9 * celsius + 160) / 5
    return f

celsius = float(input("Entre com a temperatura em graus Celsius:"))
temp = fahrenheit(celsius)
print(f" Temperatura Celsius {celsius}º, para Fahrenheit: {temp}º")

print("----------------------------------------------------")

def consumo_combustivel(tempo,velocidade):
    distancia = tempo * velocidade
    consumo = distancia / 12
    return consumo

combustivel_gasto = consumo_combustivel(2,90)
print("Consumo de gasolina:",combustivel_gasto,"litros")