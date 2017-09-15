turmas = {}

def adicionarTurma (turmas, turma,turmaDic):
    turmaDic = {}
    turmas[turma] = turmaDic

def adicionarAluno (turmas, turma, matricula, notas):
    a = turmas[turma]
    a[matricula] = notas

def calcularMediaAluno (turmas,turma, matricula):
    soma = 0
    alunos = turmas[turma]
    aluno = alunos[matricula]
    for nota in aluno:
        soma = soma + nota

    media = soma / len(aluno)
    print("A média do aluno é :", media)

def calcularMediaTurma (turmas, turm):
    turma = turmas[turm]
    somaA = 0
    somaT = 0
    contador = 0
    for notas in turma.values():
        for nota in notas:
            somaA = somaA + nota
            mediaA = somaA / len(notas)
            somaT = mediaA + somaT
            contador = contador + 1
        mediaT = somaT / contador\

    return mediaT

def main ():
    notas = []
    print("1- Adicionar Turma;\n 2- Adicionar Aluno e Notas;\n 3- Calcular média de um Aluno;\n 4- Calcular média de uma Turma."
)
    escolha = int(input("Digite o número correspondente a opção que desejas executar: "))

    if (escolha == 1):
        turma = str(input("Digite o nome da turma,utlizando o padrão do modelo, ano, turma, curso.Exemplo 1BINF -->>"))
        turmaDic = turma + "d"
        adicionarTurma(turmas, turma, turmaDic)

    elif (escolha == 2):
        turma = str(input("Digite o nome da turma em que o aluno se encontra: "))
        matricula = int(input("Digite o número da matricula do aluno: "))
        QNotas = int(input("Digite a quantidade de notas a serem adicionadas"))
        for n in range(1,QNotas + 1):
            nota = float(input("Digite a nota do aluno: "))
            notas.append(nota)
        adicionarAluno(turmas, turma, matricula, notas)

    elif (escolha == 3):
        turma = str(input("Digite o nome da turma em que o aluno: "))
        matricula = int(input("Digite o número da matricula do aluno: "))
        calcularMediaAluno(turmas, turma, matricula)

    elif(escolha == 4):
        turm = str(input("Digite o nome da turma: "))
        print("A média da turma -->>", calcularMediaTurma(turmas, turm))
                         
    else:
        print("Opção Inválida. TENTE novamente")


if ( __name__ == "__main__" or __name__ == "builtins"):
    a = True
    while(a == True):
        main()
