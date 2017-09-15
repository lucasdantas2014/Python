semana = {}
def adicionarDia(posicao, dia):
  semana[posicao] = dia

def exibirDias(dias):
  dias =  semana.items()
  for dia in dias :
    print(dia[0],dia[1])

while (True):
  print("Opções:\n 1-Adicionar Dia \n 2- Exibir Dias")
  escolha = int(input("Digite o número correspondente ao que desejas executar: "))
  
  if (escolha == 1):
    posicao = int(input("Digite a posicao do dia: "))
    dia = str(input("Digite o dia que deseja adicionar: "))
    adicionarDia(posicao,dia)
  
  elif (escolha == 2):
    exibirDias(semana)
    
  else:
    print("A opção digitada não existe, TENTE NOVAMENTE: ")
