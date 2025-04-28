from datetime import datetime, date, time, timedelta

def mostrar_data_hora_atual():
    print("📅 Data e hora atual")
    agora = datetime.now()
    print("Data e hora completa:", agora)
    print("Somente data:", agora.date())
    print("Somente hora:", agora.time())
    print()

def criar_datas_horas():
    print("🧱 Criando datas e horas")
    natal = date(2023, 12, 25)
    hora_evento = time(14, 30)
    data_hora = datetime(2023, 12, 25, 14, 30)

    print("Data de Natal:", natal)
    print("Hora do evento:", hora_evento)
    print("Data e hora do evento:", data_hora)
    print()

def formatar_datas():
    print("📝 Formatando datas com strftime")
    agora = datetime.now()
    print("Formato DD/MM/AAAA:", agora.strftime("%d/%m/%Y"))
    print("Data completa com nomes:", agora.strftime("%A, %d de %B de %Y"))
    print("Hora formatada:", agora.strftime("%H:%M:%S"))
    print()

def converter_string_para_data():
    print("🔁 Convertendo string para data com strptime")
    data_texto = "27/04/2025"
    data_convertida = datetime.strptime(data_texto, "%d/%m/%Y")
    print("String convertida:", data_convertida)
    print()

def somar_subtrair_datas():
    print("➕➖ Trabalhando com timedelta")
    hoje = datetime.now()
    print("Hoje:", hoje)

    amanha = hoje + timedelta(days=1)
    ontem = hoje - timedelta(days=1)
    mais_duas_horas = hoje + timedelta(hours=2)

    print("Amanhã:", amanha)
    print("Ontem:", ontem)
    print("Daqui a 2 horas:", mais_duas_horas)
    print()

def diferenca_entre_datas():
    print("📏 Diferença entre datas")
    data1 = datetime(2025, 4, 27)
    data2 = datetime(2025, 5, 10)
    diferenca = data2 - data1
    print("Dias de diferença:", diferenca.days)
    print("Diferença total em segundos:", diferenca.total_seconds())
    print()

def comparando_datas():
    print("🔎 Comparando datas")
    hoje = datetime.now()
    evento = datetime(2025, 5, 1)
    if hoje < evento:
        print("O evento ainda vai acontecer.")
    else:
        print("O evento já passou.")
    print()

def partes_da_data():
    print("🧩 Partes da data e hora")
    agora = datetime.now()
    print("Ano:", agora.year)
    print("Mês:", agora.month)
    print("Dia:", agora.day)
    print("Hora:", agora.hour)
    print("Minuto:", agora.minute)
    print("Segundo:", agora.second)
    print()

def dias_para_fim_do_ano():
    print("🎯 Dias restantes até o fim do ano")
    hoje = datetime.now()
    fim_ano = datetime(hoje.year, 12, 31)
    dias_restantes = (fim_ano - hoje).days
    print(f"Dias até o fim do ano: {dias_restantes}")
    print()

def usando_date():
    print("📆 Usando a classe date")
    data_hoje = date.today()
    print("Data de hoje:", data_hoje)
    print("Ano:", data_hoje.year)
    print("Mês:", data_hoje.month)
    print("Dia:", data_hoje.day)
    print("Dia da semana (0=Segunda):", data_hoje.weekday())
    print()

# Chamando todas as funções
mostrar_data_hora_atual()
criar_datas_horas()
formatar_datas()
converter_string_para_data()
somar_subtrair_datas()
diferenca_entre_datas()
comparando_datas()
partes_da_data()
dias_para_fim_do_ano()
usando_date()
dir(datetime)