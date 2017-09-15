from Pessoa import Pessoa
from Fornecedor import Fornecedor
from Funcionario import Funcionario

def main():
  joaop = Pessoa("joao","rua:221","98679")
  fo1 = Fornecedor(55.0,30.0,"pedro","rua","98765")
  fu1 = Funcionario(2,1000,10,"juan","R", "98776")
  
  print(joaop.nome)
  print(fo1.endereco)
  print(fo1.obterSaldo())
  print(fu1.telefone)
  print(fu1.calcularSalarioTotal())
  
if __name__ == "__main__":
  main()
