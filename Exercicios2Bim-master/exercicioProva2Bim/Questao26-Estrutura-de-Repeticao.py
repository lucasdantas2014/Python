eleitores=int(input("Digite o númerode eleitores:"))
candidato1 = 0
candidato2 = 0
candidato3 = 0
for eleitor in range(1,eleitores + 1,1):
    votovalido = False
    #Verificação do voto
    while(votovalido==False):
         voto=int(input("Digite 1 para votar no candidato1, ou 2 para o candidato2, ou 3 para o candidato3:"))
         if (voto == 1 ):
            votovalido = True
            candidato1 = candidato1 + 1

         elif (voto == 2 ):
             votovalido = True
             candidato2 = candidato2 + voto

         elif (voto == 3 ):
             votovalido = True
             candidato3 = candidato3 + voto

         else:
             votovalido = False
             print("Voto Inválido.TENTE NOVAMENTE")
print("O candidato1 ganhou",candidato1,"votos")
print("O candidato2 ganhou",candidato2,"votos")
print("O candidato3 ganhou",candidato3,"votos")