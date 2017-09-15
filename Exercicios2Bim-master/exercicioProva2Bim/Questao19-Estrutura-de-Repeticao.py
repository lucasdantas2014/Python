#VAriaveis
valores=eval(input("Digite uma lista de numeros:"))
soma = 0
loop1 = 0
teste = True
#Repetiçao para teste de confirmaçao da condiçao
for n in valores:
    if(n < 0 or n > 1000):
        teste = False
#Teste da Condiçao
if(teste  == True):
#Comandos se a condição der verdadeira
    for x in valores:
        if(loop1 == 0):
            maior = x
            menor = x
            soma = x + soma
            loop1 = 1
        else:
            if(x < menor):
                menor = x
            if(x > maior):
                maior = x
            soma = x + soma
            a = x
    print("O menor número da lista é:",menor)
    print("O maior número da lista é:",maior)
    print("O resultado da soma dos números da lista é:",soma)
#COmandos para condição falsa
else:
    print("Valores Inválidos")