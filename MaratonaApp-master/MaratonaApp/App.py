from model.Pessoa import Pessoa
from model.Cliente import Cliente
from model.Funcionario import Funcionario
from model.Maratona import Maratona

def main():
    funcionario = Funcionario("José")
    cliente = Cliente("maria")
    maratona = Maratona()
    maratona.correr(cliente)
    maratona.correr(funcionario)

if __name__ == "__main__":
    main()
