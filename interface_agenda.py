# interface.py

import tkinter as tk
from view_agenda import Agenda

# Funções de controle
def adicionar_compromisso():
    data = entry_data.get()
    descricao = entry_descricao.get()
    if data and descricao:
        resultado = agenda.adicionar_compromisso(data, descricao)
        atualizar_status(resultado)
        listar_compromissos()
    else:
        atualizar_status("Data e descrição são obrigatórios.")

def remover_compromisso():
    try:
        indice = int(entry_indice.get()) - 1
        resultado = agenda.remover_compromisso(indice)
        atualizar_status(resultado)
        listar_compromissos()
    except ValueError:
        atualizar_status("Índice inválido. Digite um número.")

def listar_compromissos():
    compromissos = agenda.listar_compromissos()
    text_lista.config(state=tk.NORMAL)
    text_lista.delete(1.0, tk.END)
    text_lista.insert(tk.END, compromissos)
    text_lista.config(state=tk.DISABLED)

def atualizar_status(mensagem):
    label_status.config(text=mensagem)

# Inicializando a agenda
agenda = Agenda()

# Criando a interface gráfica
root = tk.Tk()
root.title("Agenda Pessoal")

# Frame para Adicionar Compromisso
frame_adicionar = tk.Frame(root, padx=10, pady=10)
frame_adicionar.grid(row=0, column=0, padx=10, pady=10)

label_data = tk.Label(frame_adicionar, text="Data:")
label_data.grid(row=0, column=0, pady=5)
entry_data = tk.Entry(frame_adicionar, width=20)
entry_data.grid(row=0, column=1, pady=5)

label_descricao = tk.Label(frame_adicionar, text="Descrição:")
label_descricao.grid(row=1, column=0, pady=5)
entry_descricao = tk.Entry(frame_adicionar, width=20)
entry_descricao.grid(row=1, column=1, pady=5)

btn_adicionar = tk.Button(frame_adicionar, text="Adicionar", command=adicionar_compromisso, width=15)
btn_adicionar.grid(row=2, column=0, columnspan=2, pady=10)

# Frame para Remover Compromisso
frame_remover = tk.Frame(root, padx=10, pady=10)
frame_remover.grid(row=1, column=0, padx=10, pady=10)

label_indice = tk.Label(frame_remover, text="Índice para remover:")
label_indice.grid(row=0, column=0, pady=5)
entry_indice = tk.Entry(frame_remover, width=5)
entry_indice.grid(row=0, column=1, pady=5)

btn_remover = tk.Button(frame_remover, text="Remover", command=remover_compromisso, width=15)
btn_remover.grid(row=1, column=0, columnspan=2, pady=10)

# Textbox para Listar Compromissos
frame_lista = tk.Frame(root, padx=10, pady=10)
frame_lista.grid(row=2, column=0, padx=10, pady=10)

text_lista = tk.Text(frame_lista, width=40, height=10, state=tk.DISABLED)
text_lista.grid(row=0, column=0)

# Label de Status
label_status = tk.Label(root, text="", pady=10)
label_status.grid(row=3, column=0, pady=5)

# Executando a interface
root.mainloop()
