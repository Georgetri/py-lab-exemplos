import time

print("\n 🕰️ O time é extremamente útil quando você precisa medir a performance de um código, "
      "criar delays no seu programa, ou trabalhar com datas e horas.\n")
print()
# 1. Pegando o tempo atual em segundos desde a "época" (1970-01-01)
tempo_atual = time.time()
print(f"Tempo atual (segundos desde 1970-01-01): {tempo_atual}")

# 2. Usando time.sleep() - Fazendo o programa "dormir" por alguns segundos
print("\nDormindo por 2 segundos...")
time.sleep(2)  # Programa "dorme" por 2 segundos
print("Mais 2 segundos...")
time.sleep(2)
print("Acordei após 2 segundos!")

# 3. Medindo o tempo de execução de um código
inicio = time.time()
for i in range(1000000):
    pass  # Simulação de um código de longo tempo
fim = time.time()
print(f"\nTempo de execução do loop: {fim - inicio} segundos")

antes = time.time()
lista = []
for i in range(0,10000): # Executando o for 10 mil vezes
    lista.append(i)
depois = time.time()
print(f"Tempo de execução do loop For de 0 a 10 mil: {depois - antes} segundos")

# 4. Trabalhando com a função time.localtime()
# Isso nos dá a data e hora local em um formato estruturado (tupla)
tempo_local = time.localtime()
print(f"\nData e hora local (time.localtime()): {tempo_local}")

# 5. Convertendo para um formato legível com time.asctime()
data_legivel = time.asctime(tempo_local)
print(f"\nData legível com time.asctime(): {data_legivel}")

# 6. Convertendo para um formato customizado com time.strftime()
formato_personalizado = time.strftime("%d/%m/%Y %H:%M:%S", tempo_local)
print(f"\nData formatada com time.strftime(): {formato_personalizado}")

# 7. Convertendo uma string para um objeto de tempo com time.strptime()
# Aqui vamos pegar uma string no formato específico e convertê-la para o tipo de dado struct_time
data_string = "25/12/2025 15:30:00"
tempo_convertido = time.strptime(data_string, "%d/%m/%Y %H:%M:%S")
print(f"\nConvertendo string para tempo (time.strptime): {tempo_convertido}")

# 8. Usando time.mktime() para converter struct_time de volta para segundos desde 1970
segundos = time.mktime(tempo_convertido)
print(f"\nSegundos desde 1970 para a data convertida: {segundos}")

# 9. Calculando o tempo em segundos entre duas datas
tempo_inicial = time.mktime(time.strptime("01/01/2020 00:00:00", "%d/%m/%Y %H:%M:%S"))
tempo_final = time.mktime(time.strptime("01/01/2021 00:00:00", "%d/%m/%Y %H:%M:%S"))
diferenca_tempo = tempo_final - tempo_inicial
print(f"\nDiferença em segundos entre 01/01/2020 e 01/01/2021: {diferenca_tempo} segundos")

# 10. Trabalhando com time.perf_counter() - Medindo o tempo de alta precisão
inicio_preciso = time.perf_counter()
for i in range(1000000):
    pass
fim_preciso = time.perf_counter()
print(f"\nTempo de execução com alta precisão (perf_counter): {fim_preciso - inicio_preciso} segundos")

# 11. Obtendo o tempo em formato de contagem crescente com time.process_time()
# Esse tempo não é afetado por mudanças de sistema, ele conta o tempo de CPU
inicio_cpu = time.process_time()
for i in range(1000000):
    pass
fim_cpu = time.process_time()
print(f"\nTempo de CPU (process_time): {fim_cpu - inicio_cpu} segundos")

# 12. Trabalhando com time.gmtime() - Convertendo para UTC (hora universal coordenada)
tempo_utc = time.gmtime()
print(f"\nHora UTC (time.gmtime()): {tempo_utc}")

# 13. Usando time.monotonic() - Tempo monotônico, útil para intervalos
inicio_monotonic = time.monotonic()
time.sleep(1)  # Dorme por 1 segundo
fim_monotonic = time.monotonic()
print(f"\nTempo monotônico: {fim_monotonic - inicio_monotonic} segundos")

# 14. Verificando se o código foi executado com sucesso utilizando a função time.time()
print(f"\nVerificando tempo atual com time.time() novamente: {time.time()}")

print("\n")

'''
🔍 Explicações detalhadas para cada função do código:

time.time(): Retorna o tempo em segundos desde a "época" (1970-01-01). Pode ser útil para cálculos de tempo e medir a duração de eventos.

time.sleep(segs): Faz o programa "dormir" por um determinado número de segundos. Muito usado para pausas ou esperas em execuções.

Medir o tempo de execução: Usamos time.time() para capturar o tempo inicial e final, e subtraímos para saber quanto tempo o código levou para ser executado.

time.localtime(): Retorna o tempo local como uma estrutura struct_time (um tipo de dado semelhante a uma tupla com valores como ano, mês, dia, etc.).

time.asctime(): Converte a estrutura struct_time em uma string legível, no formato "Day Mon Date hh:mm:ss Year".

time.strftime(format, t): Converte a estrutura struct_time para uma string formatada. O format permite que você escolha como deseja mostrar a data/hora, e você pode usar placeholders como %d, %m, %Y, %H, %M, %S, etc.

time.strptime(string, format): Converte uma string de data/hora em um objeto struct_time de acordo com o formato fornecido.

time.mktime(t): Converte uma estrutura struct_time (obtida com time.strptime(), por exemplo) de volta para segundos desde a "época".

Calcular a diferença entre duas datas: Usando mktime(), podemos calcular a diferença em segundos entre duas datas (útil para medir a duração entre eventos).

time.perf_counter(): Retorna o tempo com alta precisão. Usado para medir intervalos de tempo com precisão de frações de segundo. Ideal para benchmarking.

time.process_time(): Retorna o tempo de CPU consumido pelo processo. Útil para medir o tempo de execução do código, mas não inclui o tempo de espera (como o tempo de inatividade do sistema).

time.gmtime(): Retorna a hora em UTC (Coordinated Universal Time), ou seja, o horário sem considerar o fuso horário local.

time.monotonic(): Retorna o tempo de uma "contagem crescente" que não é afetada por ajustes no sistema de relógio. Usado para medir intervalos de tempo, pois nunca diminui.

📚 Resumo das Funções:
Funções de Tempo Atual: time.time(), time.localtime(), time.gmtime()

Funções de Formatação: time.asctime(), time.strftime(), time.strptime()

Funções de Medição de Tempo: time.perf_counter(), time.process_time(), time.monotonic()

Funções de Controle de Fluxo: time.sleep()

Funções de Cálculo de Intervalos: time.mktime()
'''