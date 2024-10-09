# agenda.py

class Agenda:
    def __init__(self):
        self.compras = []

    def adicionar_compromisso(self, data, descricao):
        self.compras.append({"data": data, "descricao": descricao})
        return "Compromisso adicionado."

    def remover_compromisso(self, indice):
        try:
            self.compras.pop(indice)
            return "Compromisso removido."
        except IndexError:
            return "Compromisso não encontrado."

    def listar_compromissos(self):
        if not self.compras:
            return "Nenhum compromisso agendado."
        return "\n".join([f"{i+1}. {comp['data']} - {comp['descricao']}" for i, comp in enumerate(self.compras)])
