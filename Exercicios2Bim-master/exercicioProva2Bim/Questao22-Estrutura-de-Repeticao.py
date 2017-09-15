#Indentificando as variaveis
n=int(input("Digite um número inteiro:"))
Qdivisores = 0
divisores=[]
#Repetição para verifição do número
if(n >= 0):
    for x in (range(1,n + 1,1)):
        verificacao =  n % x
        if (verificacao == 0):
            Qdivisores = Qdivisores + 1
            divisores = divisores + [x]
else:
    for x in (range(-1,n - 1,-1)):
        verificacao =  n % x
        if (verificacao == 0):
            Qdivisores = Qdivisores + 1
            if(x != -1 or x != n ):
                Qdivisores = Qdivisores + 1
                divisores = divisores + [x]

if(Qdivisores == 2):
    print("O número",n,"é primo")
else:
    print("O número",n,"não é primo")
    print("Seus divisores são",divisores)