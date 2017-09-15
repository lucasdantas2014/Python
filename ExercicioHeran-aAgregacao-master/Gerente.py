from Questao2.Funcionario import Funcionario

class Funcionario (Funcionario):
    def __init__(self, salario, matricula,nome, idade, genero, nomeGerencia):
        Funcionario.__initi__(self,salario,matricula,nome,idade,genero)
        self.nomeGerencia = nomeGerencia
