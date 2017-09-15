import random
executar = "iniciar"
def jogo():
    valorSecreto = random.randint(1,100)
    chances = 3

    while(chances >= 1):
        if(chances == 1):
            print("\nÚltima Chance")
        else:
            print("\nnvocê tem",chances,"chances")
        tentativa = int(input("Tente advinhar o numero secreto entre 1 e 100:"))
        if(tentativa > valorSecreto):
            print("O valor secreto é menor que o valor digitadof")
        elif(tentativa < valorSecreto):
            print("O valor secreto é maior que o valor digitado")
        else:
            print("Parabéns você acertou o número")
            print("Você é o cara e merece nota maxima no ENEM")
            chances = 0
        chances = chances - 1
        if (chances == 0):
            print("\nfim de jogo, vitoria da maquina.")
            print("O número secreto era:",valorSecreto)

while(executar != "fim"):
    jogo()
    executar = str(input("\nSe vocês deseja encerrar digite- fim, se deseja continuar digite- continuar:"))

