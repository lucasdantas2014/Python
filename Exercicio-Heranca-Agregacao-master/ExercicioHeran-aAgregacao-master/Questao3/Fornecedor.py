from Questao3.Pessoa import Pessoa

class Fornecedor(Pessoa):
  def __init__(self, valorCredito, valorDivida,nome, endereco, telefone):
    
    super(Fornecedor,self).__init__(nome,endereco,telefone)
    self.valorCredito = valorCredito
    self.valorDivida = valorDivida
    
  def obterSaldo(self):
    return self.valorCredito - self.valorDivida
  
