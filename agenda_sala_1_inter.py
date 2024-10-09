# interface.py

import tkinter as tk
from agenda_sala_1 import Agenda

# Inicializando a agenda
agenda = Agenda()

# Funções de controle
def adicionar_compromisso():
    data = entry_data.get()
    descricao = entry_descricao.get()
    agenda.adicionar_compromisso(data, descricao)
    listar_compromissos()

def remover_compromisso():
    indice = int(entry_indice.get()) - 1
    agenda.remover_compromisso(indice)
    listar_compromissos()

def listar_compromissos():
    text_lista.delete(1.0, tk.END)
    compromissos = agenda.listar_compromissos()
    for i, comp in enumerate(compromissos, start=1):
        text_lista.insert(tk.END, f"{i}. {comp['data']} - {comp['descricao']}\n")

# Criando a interface gráfica
class AgendaInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agenda Simples")

        # Campos de Adicionar Compromisso
        label_data = tk.Label(self, text="Data:")
        label_data.grid(row=0, column=0, padx=10, pady=5)
        label_data["font"] = ("Arial", 12)

        global entry_data
        entry_data = tk.Entry(self)
        entry_data.grid(row=0, column=1, padx=10, pady=5)
        entry_data["width"] = 30

        label_descricao = tk.Label(self, text="Descrição:")
        label_descricao.grid(row=1, column=0, padx=10, pady=5)
        label_descricao["font"] = ("Arial", 12)

        global entry_descricao
        entry_descricao = tk.Entry(self)
        entry_descricao.grid(row=1, column=1, padx=10, pady=5)
        entry_descricao["width"] = 30

        btn_adicionar = tk.Button(self, text="Adicionar", command=adicionar_compromisso)
        btn_adicionar.grid(row=2, column=0, columnspan=2, pady=10)
        btn_adicionar["width"] = 15
        btn_adicionar["font"] = ("Arial", 10)

        # Campo para Remover Compromisso
        label_indice = tk.Label(self, text="Índice:")
        label_indice.grid(row=3, column=0, padx=10, pady=5)
        label_indice["font"] = ("Arial", 12)

        global entry_indice
        entry_indice = tk.Entry(self)
        entry_indice.grid(row=3, column=1, padx=10, pady=5)
        entry_indice["width"] = 5

        btn_remover = tk.Button(self, text="Remover", command=remover_compromisso)
        btn_remover.grid(row=4, column=0, columnspan=2, pady=10)
        btn_remover["width"] = 15
        btn_remover["font"] = ("Arial", 10)

        # Textbox para Listar Compromissos
        global text_lista
        text_lista = tk.Text(self, width=50, height=10)
        text_lista.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        text_lista["font"] = ("Arial", 10)

# Executando a interface
if __name__ == "__main__":
    app = AgendaInterface()
    app.mainloop()
