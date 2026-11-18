"""
MODELO DIDÁTICO — ALUNOS, PROFESSORES, TURMAS (com muitos-para-muitos)
- Convenções de IDs: id_aluno, id_turma, id_professor
- Atributos da TURMA: id_turma, nome_turma, turno (pertencem só à turma)
- Relações:
    • ALUNO -> TURMA  (N → 1): aluno guarda id_turma
    • TURMA <-> PROFESSOR (N ↔ N): tabela de ligação turmas_professores
"""

# -----------------------
# DADOS (fixos para o exemplo)
# -----------------------

alunos = [
    {"id_aluno": 1, "nome": "Ana",    "idade": 20, "id_turma": 101},
    {"id_aluno": 2, "nome": "João",   "idade": 22, "id_turma": 101},
    {"id_aluno": 3, "nome": "Carlos", "idade": 19, "id_turma": 102},
    {"id_aluno": 4, "nome": "Bianca", "idade": 21, "id_turma": 103},
]

professores = [
    {"id_professor": 201, "nome": "Prof. Maria",  "disciplina": "Matemática"},
    {"id_professor": 202, "nome": "Prof. Paulo",  "disciplina": "História"},
    {"id_professor": 203, "nome": "Prof. Helena", "disciplina": "Português"},
]

turmas = [
    {"id_turma": 101, "nome_turma": "1º Ano - A", "turno": "Manhã"},
    {"id_turma": 102, "nome_turma": "1º Ano - B", "turno": "Tarde"},
    {"id_turma": 103, "nome_turma": "1º Ano - C", "turno": "Noite"},
]

# TABELA DE LIGAÇÃO (N↔N): cada linha diz que um professor leciona em uma turma
turmas_professores = [
    {"id_turma": 101, "id_professor": 201},  # 101 tem Maria (Matemática)
    {"id_turma": 101, "id_professor": 203},  # 101 tem Helena (Português)
    {"id_turma": 102, "id_professor": 201},  # 102 tem Maria (Matemática)
    {"id_turma": 102, "id_professor": 202},  # 102 tem Paulo (História)
    {"id_turma": 103, "id_professor": 202},  # 103 tem Paulo (História)
]

# -----------------------
# LISTAGENS BÁSICAS
# -----------------------

print("=== TURMAS (atributos próprios) ===")
for t in turmas:
    print("id_turma:", t["id_turma"], "| nome_turma:", t["nome_turma"], "| turno:", t["turno"])
print()

print("=== PROFESSORES ===")
for p in professores:
    print("id_professor:", p["id_professor"], "| nome:", p["nome"], "| disciplina:", p["disciplina"])
print()

print("=== ALUNOS (e sua turma) ===")
for a in alunos:
    nome_turma = "(não encontrada)"
    turno_turma = "-"
    # procurar a turma do aluno
    for t in turmas:
        if t["id_turma"] == a["id_turma"]:
            nome_turma = t["nome_turma"]
            turno_turma = t["turno"]
            break
    print("Aluno:", a["nome"], "| Idade:", a["idade"], "| Turma:", nome_turma, "| Turno:", turno_turma)
print()

# -----------------------
# TURMA -> PROFESSORES (usando a tabela de ligação)
# -----------------------

print("=== TURMAS E SEUS PROFESSORES (N↔N) ===")
for t in turmas:
    print("Turma:", t["nome_turma"], "| Turno:", t["turno"])
    tem_prof = False

    # procurar linhas na ligação com id_turma igual
    for lig in turmas_professores:
        if lig["id_turma"] == t["id_turma"]:
            # achar o professor dessa ligação
            for p in professores:
                if p["id_professor"] == lig["id_professor"]:
                    print("  -", p["nome"], "(", p["disciplina"], ")")
                    tem_prof = True

    if not tem_prof:
        print("  (sem professores)")
print()

# -----------------------
# PROFESSOR -> TURMAS (N↔N invertido)
# -----------------------

print("=== PROFESSORES E AS TURMAS EM QUE LECIONAM (N↔N) ===")
for p in professores:
    print("Professor:", p["nome"], "-", p["disciplina"])
    tem_turma = False

    # procurar linhas na ligação com id_professor igual
    for lig in turmas_professores:
        if lig["id_professor"] == p["id_professor"]:
            # achar a turma dessa ligação
            for t in turmas:
                if t["id_turma"] == lig["id_turma"]:
                    print("  -", t["nome_turma"], "(turno:", t["turno"] + ")")
                    tem_turma = True

    if not tem_turma:
        print("  (sem turmas)")
print()

# -----------------------
# TURMA -> ALUNOS (N→1 já existente)
# -----------------------

print("=== ALUNOS POR TURMA ===")
for t in turmas:
    print("Turma:", t["nome_turma"])
    tem_aluno = False
    for a in alunos:
        if a["id_turma"] == t["id_turma"]:
            print("  -", a["nome"])
            tem_aluno = True
    if not tem_aluno:
        print("  (sem alunos)")
print()

print(">>> Fim. Modelo N↔N simples, claro e didático.")
