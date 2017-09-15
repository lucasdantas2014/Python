from Questao2.Pessoa import Pessoa

class Funcionario (Pessoa):
    def __init__(self, salario, matricula,nome, idade, genero):
        Pessoa.__initi__(self,nome,idade,genero)
        self.salario = salario
        self.matricula = matricula

    def calcularINSS(self):
        INSS = salario * 0.11
        return INSS
