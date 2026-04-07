"""EXEMPLO DE UMA LISTA DE DICIONÁRIOS — ALUNOS, PROFESSORES E TURMAS

Objetivo:
- Demonstrar listas de dicionários e cruzar dados entre elas.
- Não usar funções (apenas código direto, ideal para exercícios de lógica).
- Exibir tabelas organizadas e relatórios simples.

Entidades:
- alunos: id, nome, idade, nota, turma_id
- professores: id, nome, disciplina, salario
- turmas: id, nome, professor_id, turno, sala, capacidade
"""

# -----------------------------
# DADOS (listas de dicionários)
# -----------------------------

alunos = [
    {"id": 1, "nome": "Ana", "idade": 20, "nota": 8.5, "turma_id": 101},
    {"id": 2, "nome": "João", "idade": 22, "nota": 7.3, "turma_id": 101},
    {"id": 3, "nome": "Carlos", "idade": 19, "nota": 9.1, "turma_id": 102},
    {"id": 4, "nome": "Marina", "idade": 21, "nota": 8.2, "turma_id": 102},
    {"id": 5, "nome": "Bianca", "idade": 20, "nota": 6.9, "turma_id": 103},
    {"id": 6, "nome": "Rafael", "idade": 23, "nota": 7.8, "turma_id": 103},
]

professores = [
    {"id": 201, "nome": "Ana Souza", "disciplina": "Matemática", "salario": 4800.00},
    {"id": 202, "nome": "Carlos Lima", "disciplina": "Física", "salario": 5100.00},
    {"id": 203, "nome": "Marina Alves", "disciplina": "Português", "salario": 4650.00},
    {"id": 204, "nome": "João Ribeiro", "disciplina": "História", "salario": 4400.00},
]

turmas = [
    {"id": 101, "nome": "1º Sem. - Exatas", "professor_id": 201,
     "turno": "Manhã", "sala": "A-101", "capacidade": 40},
    {"id": 102, "nome": "2º Sem. - Linguagens", "professor_id": 203,
     "turno": "Tarde", "sala": "B-202", "capacidade": 35},
    {"id": 103, "nome": "3º Sem. - Ciências", "professor_id": 202,
     "turno": "Noite", "sala": "C-303", "capacidade": 45},
]

# --------------------------------
# ÍNDICES AUXILIARES (para juntar)
# --------------------------------

prof_por_id = {p["id"]: p for p in professores}
turma_por_id = {t["id"]: t for t in turmas}

# -----------------------
# RELATÓRIOS E IMPRESSÕES
# -----------------------

print("\n=== 👩‍🎓 LISTA DE ALUNOS ===")
print(f"{'ID':<4} {'Nome':<12} {'Idade':>5} {'Nota':>6} {'Turma':>5}")
print("-" * 38)
for a in alunos:
    print(f"{a['id']:<4} {a['nome']:<12} {a['idade']:>5} {a['nota']:>6.1f} {a['turma_id']:>5}")

media_idade = sum(a["idade"] for a in alunos) / len(alunos)
print(f"\nMédia das idades: {media_idade:.1f}")

print("\n=== 👩‍🏫 LISTA DE PROFESSORES ===")
print(f"{'ID':<4} {'Nome':<18} {'Disciplina':<12} {'Salário (R$)':>14}")
print("-" * 54)
for p in professores:
    print(f"{p['id']:<4} {p['nome']:<18} {p['disciplina']:<12} {p['salario']:>14.2f}")

media_salario = sum(p["salario"] for p in professores) / len(professores)
print(f"\nMédia salarial: R$ {media_salario:.2f}")

print("\n=== 🏫 LISTA DE TURMAS ===")
print(f"{'ID':<4} {'Nome':<24} {'Turno':<8} {'Sala':<6} {'Cap.':>4} {'Prof. (id)':>11}")
print("-" * 64)
for t in turmas:
    print(f"{t['id']:<4} {t['nome']:<24} {t['turno']:<8} {t['sala']:<6} "
          f"{t['capacidade']:>4} {t['professor_id']:>11}")

# ------------------------------------------------------
# CRUZAMENTO: TURMA → PROFESSOR (join por professor_id)
# ------------------------------------------------------

print("\n=== 🔗 TURMA × PROFESSOR ===")
print(f"{'Turma':<24} {'Professor':<18} {'Disciplina':<12} {'Turno':<8} {'Sala':<6}")
print("-" * 72)
for t in turmas:
    prof = prof_por_id.get(t["professor_id"])
    nome_prof = prof["nome"] if prof else "(desconhecido)"
    disc = prof["disciplina"] if prof else "-"
    print(f"{t['nome']:<24} {nome_prof:<18} {disc:<12} {t['turno']:<8} {t['sala']:<6}")

# ----------------------------------------------------------------
# CRUZAMENTO: ALUNOS POR TURMA (contagem e média de notas por turma)
# ----------------------------------------------------------------

print("\n=== 🧮 RESUMO POR TURMA (qtd. alunos e média de notas) ===")
print(f"{'Turma':<24} {'Qtd.':>4} {'Média Nota':>12}")
print("-" * 44)

# Agrupar alunos por turma_id
alunos_por_turma = {}
for a in alunos:
    turma_id = a["turma_id"]
    if turma_id not in alunos_por_turma:
        alunos_por_turma[turma_id] = []
    alunos_por_turma[turma_id].append(a)

for t in turmas:
    grupo = alunos_por_turma.get(t["id"], [])
    qtd = len(grupo)
    media_nota = (sum(x["nota"] for x in grupo) / qtd) if qtd > 0 else 0.0
    print(f"{t['nome']:<24} {qtd:>4} {media_nota:>12.2f}")

# -------------------------------------------------------
# LISTAGEM: ALUNOS DETALHADOS POR TURMA (com professor)
# -------------------------------------------------------

print("\n=== 🧾 ALUNOS POR TURMA (com professor responsável) ===")
for t in turmas:
    prof = prof_por_id.get(t["professor_id"])
    nome_prof = prof["nome"] if prof else "(desconhecido)"
    print(f"\nTurma: {t['nome']} | Professor: {nome_prof} | Turno: {t['turno']} | Sala: {t['sala']}")
    print(f"{'ID':<4} {'Aluno':<12} {'Idade':>5} {'Nota':>6}")
    print("-" * 36)
    grupo = alunos_por_turma.get(t["id"], [])
    if not grupo:
        print("(sem alunos)")
    else:
        for a in grupo:
            print(f"{a['id']:<4} {a['nome']:<12} {a['idade']:>5} {a['nota']:>6.1f}")

# -------------------------------------------------------
# CONSULTAS EXEMPLO (sem funções, apenas lógica direta)
# -------------------------------------------------------

# 1) Buscar turma pelo nome e mostrar seu professor
termo_turma = "2º Sem. - Linguagens"
turma_encontrada = None
for t in turmas:
    if t["nome"].lower() == termo_turma.lower():
        turma_encontrada = t
        break

print("\n=== 🔎 CONSULTA: PROFESSOR DE UMA TURMA ===")
if turma_encontrada:
    prof = prof_por_id.get(turma_encontrada["professor_id"])
    if prof:
        print(f"Turma: {turma_encontrada['nome']} → Professor: {prof['nome']} "
              f"({prof['disciplina']})")
    else:
        print("Professor não encontrado para a turma.")
else:
    print("Turma não encontrada.")

# 2) Listar todas as turmas de um professor (por nome)
termo_prof = "Carlos Lima"
print("\n=== 🔎 CONSULTA: TURMAS DE UM PROFESSOR ===")
prof_id_alvo = None
for p in professores:
    if p["nome"].lower() == termo_prof.lower():
        prof_id_alvo = p["id"]
        break

if prof_id_alvo is not None:
    print(f"Professor: {termo_prof}")
    achou = False
    for t in turmas:
        if t["professor_id"] == prof_id_alvo:
            print(f"- {t['nome']} | Turno: {t['turno']} | Sala: {t['sala']}")
            achou = True
    if not achou:
        print("(sem turmas)")
else:
    print("Professor não encontrado.")

# 3) Listar alunos de uma turma específica (por id)
turma_id_consulta = 103
print("\n=== 🔎 CONSULTA: ALUNOS DE UMA TURMA ===")
print(f"Turma ID: {turma_id_consulta}")
grupo = alunos_por_turma.get(turma_id_consulta, [])
if not grupo:
    print("(sem alunos)")
else:
    for a in grupo:
        print(f"- {a['nome']} (nota {a['nota']:.1f})")

print("\n✔️ Fim do exemplo completo (sem funções).")
