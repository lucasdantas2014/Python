turmas=int(input("Digite o número de turmas que há:"))
soma = 0
for turma in range(1,turmas + 1,1):
    print("Na turma", turma)
    verificacao = True
    while(verificacao == True):
        alunos = int(input("Quantos alunos há:"))
        if(alunos <= 40 and alunos >= 0):
            soma = soma + alunos
            verificacao=False
        else:
            print("Tente novamente(OBS:O número de alunos por sala não pode ser superior a 40)")
            verificacao=True


media = soma / turmas
print("A media de alunos é:",media)

