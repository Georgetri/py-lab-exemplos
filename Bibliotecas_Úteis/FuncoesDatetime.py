import datetime

# Criando um objeto datetime com a data e hora atuais
agora = datetime.datetime.now()
hoje = datetime.date.today()
horario = datetime.datetime(2025,4,27,17,18,30)
print(f"\n => Hoje:{hoje}, Agora: {agora}")
print("Dia:",agora.day, "| Mês:", agora.month, "| Ano:", agora.year)
print("Horário com data:",horario, "| Horas:", horario.hour,"| Minutos:", horario.minute,"| Segundos:", horario.second)
print()

# 1️⃣ dir(): mostra todos os métodos e atributos disponíveis do objeto ou módulo
print("🔍 Métodos e atributos disponíveis em datetime:")
print(dir(datetime))  # Mostra tudo que o módulo datetime oferece

print("\n🔍 Métodos e atributos disponíveis no objeto agora:")
print(dir(agora))  # Mostra tudo que o objeto datetime possui

# 2️⃣ help(): exibe a documentação da classe, função ou objeto
print("\n📘 Documentação da classe datetime.datetime:")
# Comentado para não ocupar muito espaço — descomente para testar:
# help(datetime.datetime)

# 3️⃣ type(): mostra o tipo do objeto
print("\n📎 Tipo do objeto 'agora':")
print(type(agora))  # <class 'datetime.datetime'>

# 4️⃣ vars(): mostra os atributos __dict__ de objetos personalizados
print("\n📦 Usando vars() no objeto 'agora':")
try:
    print(vars(agora))
except TypeError:
    print("⚠️ vars() não funciona com objetos integrados como datetime.datetime")

# 5️⃣ getattr(): acessa atributos dinamicamente
print("\n🔑 Acessando atributos com getattr()")
print("Ano:", getattr(agora, 'year'))
print("Mês:", getattr(agora, 'month'))
print("Dia:", getattr(agora, 'day'))

# 6️⃣ hasattr(): verifica se o objeto tem certo atributo
print("\n📍 Verificando atributos com hasattr()")
print("O objeto tem o atributo 'day'?", hasattr(agora, 'day'))        # True
print("O objeto tem o atributo 'banana'?", hasattr(agora, 'banana'))  # False

# 7️⃣ callable(): verifica se um objeto pode ser chamado (como função)
print("\n🔄 Verificando se o objeto é chamável (callable)")
print("datetime.datetime.now é chamável?", callable(datetime.datetime.now))  # True
print("O objeto 'agora' é chamável?", callable(agora))  # False

# Extra: usando getattr de forma dinâmica
atributos_para_mostrar = ['year', 'month', 'day', 'hour', 'minute']
print("\n🔁 Mostrando vários atributos usando getattr em loop:")
for attr in atributos_para_mostrar:
    valor = getattr(agora, attr)
    print(f"{attr.capitalize()}: {valor}")

