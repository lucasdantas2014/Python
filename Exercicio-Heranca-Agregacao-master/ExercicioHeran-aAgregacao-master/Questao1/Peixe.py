from Questao1.Animal import Animal
from Questao1.Cauda import Cauda

class Peixe (Animal):
    def __init__(self, cauda, nome, peso, habitat, tipo):
        super(Peixe,self).__init__(nome,peso,habitat)
        self.cauda = Cauda(tipo)
