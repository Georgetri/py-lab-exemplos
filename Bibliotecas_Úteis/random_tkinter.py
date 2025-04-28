import tkinter as tk
from tkinter import messagebox
import random

# Funções que serão acionadas pelos botões
def gerar_aleatorio():
    resultado.set(f"Número entre 0.0 e 1.0: {random.random():.4f}")

def gerar_inteiro():
    num = random.randint(1, 100)
    resultado.set(f"Int aleatório entre 1 e 100: {num}")

def gerar_float():
    num = round(random.uniform(1.0, 50.0), 3)
    resultado.set(f"Float entre 1.0 e 50.0: {num}")

def sortear_nome():
    nomes = ["Alice", "Bruno", "Carlos", "Diana", "Eva"]
    nome = random.choice(nomes)
    resultado.set(f"Nome sorteado: {nome}")

def mega_sena():
    numeros = sorted(random.sample(range(1, 61), 6))
    resultado.set(f"Mega-Sena: {numeros}")

# Criar janela principal
janela = tk.Tk()
janela.title("Explorando Random com Tkinter")
janela.geometry("400x300")
janela.resizable(False, False)

# Variável de resultado
resultado = tk.StringVar()
resultado.set("Escolha uma opção para gerar")

# Layout - Título
titulo = tk.Label(janela, text="Gerador Aleatório", font=("Helvetica", 16, "bold"))
titulo.pack(pady=10)

# Botões de ação
btn1 = tk.Button(janela, text="Número Aleatório", width=25, command=gerar_aleatorio)
btn2 = tk.Button(janela, text="Número Inteiro (1 a 100)", width=25, command=gerar_inteiro)
btn3 = tk.Button(janela, text="Número Float (1.0 a 50.0)", width=25, command=gerar_float)
btn4 = tk.Button(janela, text="Sortear Nome", width=25, command=sortear_nome)
btn5 = tk.Button(janela, text="Mega-Sena", width=25, command=mega_sena)

btn1.pack(pady=3)
btn2.pack(pady=3)
btn3.pack(pady=3)
btn4.pack(pady=3)
btn5.pack(pady=3)

# Resultado
label_resultado = tk.Label(janela, textvariable=resultado, fg="blue", font=("Arial", 12))
label_resultado.pack(pady=10)

# Iniciar loop da interface
janela.mainloop()
