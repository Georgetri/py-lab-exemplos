"""
EXEMPLO LISTAS COM DICIONÁRIOS — ALUNOS, PROFESSORES E TURMAS
- Somente estruturas básicas (listas de dicionários, for, while, if, print)
- Ligações: aluno["turma_id"]  <->  turma["id"]  ,  turma["professor_id"]  <->  professor["id"]
"""
# -----------------------
# DADOS INICIAIS (fixos)
# -----------------------

alunos = [
    {"id": 1, "nome": "Ana",    "idade": 20, "turma_id": 101},
    {"id": 2, "nome": "João",   "idade": 22, "turma_id": 101},
    {"id": 3, "nome": "Carlos", "idade": 19, "turma_id": 102},
]
professores = [
    {"id": 201, "nome": "Prof. Maria", "disciplina": "Matemática"},
    {"id": 202, "nome": "Prof. Paulo", "disciplina": "História"},
]

turmas = [
    {"id": 101, "nome": "Turma A", "professor_id": 201},
    {"id": 102, "nome": "Turma B", "professor_id": 202},
]

# --------------------------------------------------------
# ALUNOS -> TURMAS (mostrar a turma de cada aluno)
# --------------------------------------------------------
print("=== ALUNOS E SUAS TURMAS ===")
for aluno in alunos:
    turma_nome = "(não encontrada)"
    for turma in turmas:
        if turma["id"] == aluno["turma_id"]:
            turma_nome = turma["nome"]
            break
    print("Aluno:", aluno["nome"], "| Idade:", aluno["idade"], "| Turma:", turma_nome)

print()  # linha em branco

# --------------------------------------------------------
# PROFESSORES -> TURMAS (mostrar turmas de cada professor)
# --------------------------------------------------------
print("=== PROFESSORES E SUAS TURMAS ===")
for prof in professores:
    print("Professor:", prof["nome"], "-", prof["disciplina"])
    encontrou = False
    for turma in turmas:
        if turma["professor_id"] == prof["id"]:
            print("  Leciona na turma:", turma["nome"])
            encontrou = True
    if not encontrou:
        print("  (não possui turmas)")

print()  # linha em branco

# --------------------------------------------------------
# TURMAS -> PROFESSOR + ALUNOS (visão cruzada)
# --------------------------------------------------------
print("=== TURMAS, SEUS PROFESSORES E ALUNOS ===")
for turma in turmas:
    # achar professor da turma
    professor_da_turma = "(não encontrado)"
    for prof in professores:
        if prof["id"] == turma["professor_id"]:
            professor_da_turma = prof["nome"] + " - " + prof["disciplina"]
            break

    print("Turma:", turma["nome"], "| Professor:", professor_da_turma)
    print("Alunos desta turma:")

    tem_alunos = False
    for aluno in alunos:
        if aluno["turma_id"] == turma["id"]:
            print("  -", aluno["nome"])
            tem_alunos = True

    if not tem_alunos:
        print("  (sem alunos)")
    print()  # separa uma turma da outra

# --------------------------------------------------------
# INTERAÇÃO SIMPLES NO SEU ESTILO (while + validação)
# Consultar alunos de uma turma pelo ID
# --------------------------------------------------------
print("=== CONSULTA: ALUNOS POR TURMA (POR ID) ===")
print("Turmas disponíveis:")
for turma in turmas:
    print("ID:", turma["id"], "| Nome:", turma["nome"])

while True:
    turma_id_digitado = int(input("Digite o ID da turma para listar os alunos: "))
    existe = False
    for turma in turmas:
        if turma["id"] == turma_id_digitado:
            existe = True
            break
    if existe:
        break
    print("⚠️  ID de turma não encontrado. Tente novamente.")

print("Alunos da turma escolhida:")
tem_alunos = False
for aluno in alunos:
    if aluno["turma_id"] == turma_id_digitado:
        print(" -", aluno["nome"])
        tem_alunos = True
if not tem_alunos:
    print("(sem alunos)")

# --------------------------------------------------------
# CONSULTA SIMPLES 2: Turmas de um professor (por ID)
# --------------------------------------------------------
print()
print("=== CONSULTA: TURMAS DE UM PROFESSOR (POR ID) ===")
print("Professores disponíveis:")
for prof in professores:
    print("ID:", prof["id"], "| Nome:", prof["nome"])

while True:
    prof_id_digitado = int(input("Digite o ID do professor para listar as turmas: "))
    existe = False
    for prof in professores:
        if prof["id"] == prof_id_digitado:
            existe = True
            break
    if existe:
        break
    print("⚠️  ID de professor não encontrado. Tente novamente.")

print("Turmas do professor escolhido:")
tem_turma = False
for turma in turmas:
    if turma["professor_id"] == prof_id_digitado:
        print(" -", turma["nome"])
        tem_turma = True
if not tem_turma:
    print("(sem turmas)")

print()
