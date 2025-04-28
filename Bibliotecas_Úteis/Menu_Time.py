import time

# Função 1: Exemplo de time.time()
def tempo_atual():
    tempo = time.time()
    print(f"Tempo atual em segundos desde 1970-01-01: {tempo}\n")

# Função 2: Exemplo de time.sleep()
def dormir_por_2_segundos():
    print("Dormindo por 2 segundos...")
    time.sleep(2)
    print("Acordei após 2 segundos!\n")

# Função 3: Medindo o tempo de execução
def medir_execucao():
    inicio = time.time()
    for i in range(1000000):
        pass  # Simulação de código demorado
    fim = time.time()
    print(f"Tempo de execução do loop: {fim - inicio} segundos\n")

# Função 4: Exemplo de time.localtime()
def obter_tempo_local():
    tempo_local = time.localtime()
    print(f"Data e hora local: {tempo_local}\n")

# Função 5: Exemplo de time.asctime()
def tempo_legivel():
    tempo_local = time.localtime()
    tempo_legivel = time.asctime(tempo_local)
    print(f"Data e hora formatada com asctime: {tempo_legivel}\n")

# Função 6: Exemplo de time.strftime()
def tempo_formatado():
    tempo_local = time.localtime()
    formato_personalizado = time.strftime("%d/%m/%Y %H:%M:%S", tempo_local)
    print(f"Data formatada: {formato_personalizado}\n")

# Função 7: Exemplo de time.strptime()
def converter_string_para_data():
    data_string = "25/12/2025 15:30:00"
    tempo_convertido = time.strptime(data_string, "%d/%m/%Y %H:%M:%S")
    print(f"Data convertida de string: {tempo_convertido}\n")

# Função 8: Exemplo de time.mktime()
def converter_structtime_para_segundos():
    tempo_convertido = time.strptime("25/12/2025 15:30:00", "%d/%m/%Y %H:%M:%S")
    segundos = time.mktime(tempo_convertido)
    print(f"Segundos desde 1970 para a data convertida: {segundos}\n")

# Função 9: Calculando diferença de tempo
def calcular_diferenca_temporal():
    tempo_inicial = time.mktime(time.strptime("01/01/2020 00:00:00", "%d/%m/%Y %H:%M:%S"))
    tempo_final = time.mktime(time.strptime("01/01/2021 00:00:00", "%d/%m/%Y %H:%M:%S"))
    diferenca_tempo = tempo_final - tempo_inicial
    print(f"Diferença em segundos entre 01/01/2020 e 01/01/2021: {diferenca_tempo} segundos\n")

# Função 10: Exemplo de time.perf_counter()
def medir_tempo_preciso():
    inicio_preciso = time.perf_counter()
    for i in range(1000000):
        pass  # Código de exemplo
    fim_preciso = time.perf_counter()
    print(f"Tempo de execução com alta precisão: {fim_preciso - inicio_preciso} segundos\n")

# Função 11: Exemplo de time.process_time()
def medir_tempo_cpu():
    inicio_cpu = time.process_time()
    for i in range(1000000):
        pass  # Código de exemplo
    fim_cpu = time.process_time()
    print(f"Tempo de CPU: {fim_cpu - inicio_cpu} segundos\n")

# Função 12: Exemplo de time.gmtime()
def tempo_utc():
    tempo_utc = time.gmtime()
    print(f"Hora UTC (GMT): {tempo_utc}\n")

# Função 13: Exemplo de time.monotonic()
def medir_temporal_monotonico():
    inicio_monotonic = time.monotonic()
    time.sleep(1)  # Dorme por 1 segundo
    fim_monotonic = time.monotonic()
    print(f"Tempo monotônico: {fim_monotonic - inicio_monotonic} segundos\n")

# Função de Menu
def exibir_menu():
    print("\n--- Menu de Exemplos com a Biblioteca time ---")
    print("1. Tempo atual (time.time())")
    print("2. Dormir por 2 segundos (time.sleep())")
    print("3. Medir tempo de execução")
    print("4. Obter tempo local (time.localtime())")
    print("5. Tempo formatado com asctime()")
    print("6. Tempo formatado com strftime()")
    print("7. Converter string para data (time.strptime())")
    print("8. Converter struct_time para segundos (time.mktime())")
    print("9. Calcular diferença de tempo entre duas datas")
    print("10. Medir tempo preciso (time.perf_counter())")
    print("11. Medir tempo de CPU (time.process_time())")
    print("12. Tempo UTC (time.gmtime())")
    print("13. Medir tempo monotônico (time.monotonic())")
    print("0. Sair")

# Função principal que vai chamar as outras funções dependendo da escolha do usuário
def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (0-13): ")

        if escolha == "1":
            tempo_atual()
        elif escolha == "2":
            dormir_por_2_segundos()
        elif escolha == "3":
            medir_execucao()
        elif escolha == "4":
            obter_tempo_local()
        elif escolha == "5":
            tempo_legivel()
        elif escolha == "6":
            tempo_formatado()
        elif escolha == "7":
            converter_string_para_data()
        elif escolha == "8":
            converter_structtime_para_segundos()
        elif escolha == "9":
            calcular_diferenca_temporal()
        elif escolha == "10":
            medir_tempo_preciso()
        elif escolha == "11":
            medir_tempo_cpu()
        elif escolha == "12":
            tempo_utc()
        elif escolha == "13":
            medir_temporal_monotonico()
        elif escolha == "0":
            print("Saindo...")
            break  # Encerra o loop e sai do programa
        else:
            print("Opção inválida! Tente novamente.")

# Chama a função principal
if __name__ == "__main__":
    main()
