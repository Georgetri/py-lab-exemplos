"""  EXEMPLO DE UMA LISTA DE DICIONÁRIOS """

# Alunos: nota_final será preenchida a partir das 3 notas da sua disciplina
alunos = [
    {"nome": "Ana",    "idade": 20, "disciplina": "Matemática", "nota_final": 0.0, "status": ""},
    {"nome": "João",   "idade": 22, "disciplina": "História",   "nota_final": 0.0, "status": ""},
    {"nome": "Carlos", "idade": 19, "disciplina": "Português",  "nota_final": 0.0, "status": ""}
]

# Disciplinas: cada disciplina guarda as 3 notas de cada aluno que a cursa
disciplinas = [
    {
        "nome_disciplina": "Matemática",
        "alunos": [
            {"nome_aluno": "Ana",    "nota1": 0.0, "nota2": 0.0, "nota3": 0.0}
        ]
    },
    {
        "nome_disciplina": "História",
        "alunos": [
            {"nome_aluno": "João",   "nota1": 0.0, "nota2": 0.0, "nota3": 0.0}
        ]
    },
    {
        "nome_disciplina": "Português",
        "alunos": [
            {"nome_aluno": "Carlos", "nota1": 0.0, "nota2": 0.0, "nota3": 0.0}
        ]
    }
]


media_idade = sum(a["idade"] for a in alunos) / len(alunos)
print(f"Média das idades: {media_idade:.1f}")
