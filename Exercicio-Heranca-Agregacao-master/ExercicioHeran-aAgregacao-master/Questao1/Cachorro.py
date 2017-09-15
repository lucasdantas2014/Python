from Questao1.Animal import Animal

class Cachorro (Animal):
    def __init__ (self, raca, nome, peso, habitat):
        super (Cachorro, self).__init__(nome,peso,habitat)
        self.raca = raca

    def brincar(self):
        print("brincando")

    def vigiar (self):
        print ("Vigiando")
