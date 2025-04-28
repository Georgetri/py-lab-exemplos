from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 14)
        self.cell(0, 10, 'Plano de Estudos e Carreira - IA e Machine Learning (UniCesumar)',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Helvetica', '', 11)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Objetivo
pdf.chapter_title('Objetivo Final')
pdf.chapter_body("Se tornar um(a) profissional completo(a) em IA, capaz de desenvolver soluções usando Machine Learning, IA Generativa e Visão Computacional, com base ética, criativa e inovadora.")

# Cronograma por série
cronograma = {
    "Series 1 a 3 - Fundamentos": """Foco: bases matematicas, logica de programacao e banco de dados.
Estude:
- Matematica Aplicada
- Algoritmos e Logica de Programacao
- Banco de Dados e Mineracao
Acoes:
- Aprender Python
- HackerRank, Codewars
- Livro 'Inteligencia Artificial - Russell & Norvig'""",

    "Series 4 a 5 - Comecando com IA e Dados": """Foco: Big Data, ML, Estrutura de Dados, PLN.
Estude:
- Big Data
- IA e Machine Learning
- Processamento de Linguagem Natural
Acoes:
- Scikit-learn
- spaCy, NLTK
- Kaggle""",

    "Series 6 a 7 - Especializacoes em IA": """Foco: IA simbolica, conexionista, visao computacional.
Estude:
- IA Simbolica
- IA Conexionista
- Visao Computacional
Acoes:
- Regras logicas
- TensorFlow/Keras
- OpenCV, YOLO""",

    "Series 8 a 9 - IA Generativa e Inovacao": """Foco: Criatividade com IA, redes generativas.
Estude:
- Tecnicas avancadas de ML
- Computacao Cognitiva
- IA Generativa e GANs
Acoes:
- ChatGPT, Midjourney
- GANs em PyTorch
- Artigos no LinkedIn""",

    "Serie 10 - Encerramento com foco preditivo": """Foco: Analise preditiva e CNNs.
Estude:
- Redes Convolucionais (CNN)
- Analise Preditiva
Acoes:
- Projetos reais (vendas, churn)
- TCC aplicado
- Apresentacao empresarial"""
}

# Adiciona os capitulos
for title, body in cronograma.items():
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Plano de carreira
pdf.chapter_title('Plano de Carreira Recomendada')
pdf.chapter_body("""Etapas sugeridas:
1. Fundamentos Tecnicos (6-12 meses): Python, logica, banco de dados
2. Inicio com ML (1 ano): Regressao, classificacao
3. Especializacao em IA (1 ano): Visao computacional, PLN
4. IA Generativa (6 meses): GANs, ChatGPT
5. Portfolio e Freelancer: GitHub, LinkedIn, projetos
6. Emprego ou Empreender: Aplicacao pratica dos conhecimentos""")

# Exporta o PDF
pdf.output("Plano_Estudios_Carreira_IA_Unicesumar.pdf")
