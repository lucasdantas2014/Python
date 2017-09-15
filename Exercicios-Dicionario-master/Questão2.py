funcionarios = {}

def adicionarFuncionario(matricula,nome):
  funcionarios[matricula] = nome

def buscarFuncionario(matricula):
  print(funcionarios.get(matricula))
  
def exibirFuncionarios(funcionarios):
  items =  funcionarios.items()
  for item in items:
    print(item[0],item[1])
    
while(True):
  print("1-Adicionar funcionario;\n 2-Buscar funcionario;\n 3-Exibir funcionarios.")
  escolha = int(input("Digite o número correspondente a ação que voê deseja executar:"))
  
  if(escolha == 1):
    matricula = eval(input("Digite o numero da sua matricula:"))
    nome = str(input("Digite o nome do funcionário:"))
    adicionarFuncionario(matricula,nome)
  
  elif(escolha == 2):
    matricula = eval(input("Digite a matricula:"))
    buscarFuncionario(matricula)
    
  elif(escolha == 3):
    exibirFuncionarios(funcionarios)
      
  else:
      print("Opção Inválida, TENTE NOVAMENTE!")
