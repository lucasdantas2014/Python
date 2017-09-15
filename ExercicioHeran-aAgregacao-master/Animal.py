class Animal():
    def __init__(self,nome,peso,habitat):
        self.nome = nome
        self.peso = peso
        self.habitat = habitat

    def mover (self):
        print( self.nome + " se movendo")

    def comunicar (self):
        print (self.nome + " se comunicando")
