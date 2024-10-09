# agenda.py

class Agenda:
    def __init__(self):
        self.compromissos = []

    def adicionar_compromisso(self, data, descricao):
        self.compromissos.append({"data": data, "descricao": descricao})

    def listar_compromissos(self):
        return self.compromissos

    def remover_compromisso(self, indice):
        if 0 <= indice < len(self.compromissos):
            del self.compromissos[indice]
