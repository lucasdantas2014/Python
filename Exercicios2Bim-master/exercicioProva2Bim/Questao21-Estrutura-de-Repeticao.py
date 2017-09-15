#Indentificando as variaveis
n=int(input("Digite um número inteiro:"))
divisores = 0
#Repetição para verifição do número
if(n >= 0):
    for x in (range(1,n + 1,1)):
        verificacao =  n % x
        if (verificacao == 0):
            divisores = divisores + 1
else:
    for x in (range(-1,n - 1,-1)):
        verificacao =  n % x
        if (verificacao == 0):
            divisores = divisores + 1

if(divisores == 2):
    print("O número",n,"é primo")
else:
    print("O número",n,"não é primo")






