from model.Contato import Contato

class Agenda ():
    def __init__(self, propietario):
        self.propietario = propietario
        self.contatos = []

    def contarContatos(self):
        return len(self.contatos)

    def incluirContato(self,contato):
        self.contatos.append(contato)


    def listarContato(self):
        return self.contatos

    def excluirContato(self,nome):
        auxiliar = 0
        for contato in self.contatos:
            if (contato.pessoa.nome == nome):
                del self.contatos[auxiliar]
                print("contato: " + nome  + " removido com sucesso\n")
                break
            auxiliar +=1
