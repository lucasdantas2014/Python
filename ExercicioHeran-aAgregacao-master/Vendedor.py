from Funcionario import Funcionario
from Produto import Produto

class Vendedor (Funcionario):
 def __init__(self,valorVenda, salario, matricula,nome, idade, genero,nome,valor):
   super(Vendedor,self).__init__(self, salario, matricula,nome, idade, genero)
   self.valorVendas = valorVenda
   self.vendas = [Produto(nome,valor)]
