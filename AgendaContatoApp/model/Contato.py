import json

class Contato():

    def __init__(self, criacao, pessoa, telefones):
        self.criacao = criacao
        self.pessoa = pessoa
        self.telefones = telefones


    def listarTelefones(self):
        return self.telefones
