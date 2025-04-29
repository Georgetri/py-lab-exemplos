import pandas as pd
import os

# Criando o plano de estudos conforme a solicitação
data = {
    "Dia": [
        "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"
    ],
    "9h - 10h": [
        "Tecnólogo em IA", "Tecnólogo em IA", "Tecnólogo em IA", "Tecnólogo em IA", "Tecnólogo em IA"
    ],
    "10h - 11h": [
        "Tecnólogo em IA", "Tecnólogo em IA", "Tecnólogo em IA", "Tecnólogo em IA", "Tecnólogo em IA"
    ],
    "11h - 11:30h": [
        "Tecnólogo em IA", "Tecnólogo em IA", "Tecnólogo em IA", "Tecnólogo em IA", "Tecnólogo em IA"
    ],
    "11:30h - 12:30h": [
        "Intervalo de Almoço", "Intervalo de Almoço", "Intervalo de Almoço", "Intervalo de Almoço", "Intervalo de Almoço"
    ],
    "12:30h - 13:30h": [
        "Jdev Treinamento", "Rasmoo", "Jdev Treinamento", "Rasmoo", "Jdev Treinamento"
    ],
    "14h - 15h": [
        "IA Expert Academy", "IA Expert Academy", "IA Expert Academy", "IA Expert Academy", "IA Expert Academy"
    ],
    "15h - 16h": [
        "Jdev Treinamento", "Rasmoo", "Jdev Treinamento", "Rasmoo", "Jdev Treinamento"
    ],
    "16h - 17h": [
        "Jdev Treinamento", "Rasmoo", "Jdev Treinamento", "Rasmoo", "Jdev Treinamento"
    ]
}

# Convertendo para DataFrame
df = pd.DataFrame(data)

# Definindo o caminho para salvar o arquivo no diretório atual
file_path = os.path.join(os.getcwd(), 'plano_estudos_ia_organizado_v3.ods')

# Salvando como um arquivo .ods (LibreOffice Calc)
df.to_excel(file_path, index=False, engine='odf')

print(f"Arquivo salvo com sucesso em: {file_path}")
