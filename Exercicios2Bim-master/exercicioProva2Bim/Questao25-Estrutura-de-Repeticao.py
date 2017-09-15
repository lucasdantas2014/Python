continuar = True
soma = 0
contador = 0
while(continuar == True):
    idade=eval(input("Digite sua idade:"))
    soma = soma + idade
    resposta=int(input("Digite 1 se ainda falta dizer a idade de alguém, ou outro número qualquer para se ja tiver dito todas as idade:"))
    contador = contador + 1
    if (resposta == 1):
        continuar = True
    else:
        continuar = False
media = soma / contador
if (media >= 0 and media <= 25):
    print("Essa é uma turma jovem")
elif(media >= 26 and media <= 60):
    print("Essa é uma turma adulta,")
    print("A media de idade desta turma é",media)
elif(media > 60):
    print("Essa é uma turma idosa")
    print("A media de idade desta turma é", media)
else:
    print("As idades são inválidas(Não pode ter idades negatvas)")
    print("A media de idade desta turma é", media)