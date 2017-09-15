from Questao3.Pessoa import Pessoa

class Funcionario(Pessoa):
  def __init__(self,codigoSetor, salarioBase, imposto,nome,endereco,telefone):
    super(Funcionario,self).__init__(nome,endereco,telefone)
    self.codigoSetor = codigoSetor
    self.salarioBase = salarioBase
    self.imposto = imposto
    
  def calcularSalarioTotal(self):
    return (self.salarioBase - (self.salarioBase * (self.imposto / 100)))
    
    
