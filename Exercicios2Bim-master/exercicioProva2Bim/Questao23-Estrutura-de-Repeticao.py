#Variaveis Iniciais
n=eval(input("Digite um número:"))
primos=[]
divisoes = 0
#Primeira condiciona
if(n >=0):
    #Repetição
    for numero in (range(1,n+1,1)):
        divisores = 0
        for teste in range(1,numero +1,1):
            verificacao = numero % teste
            divisoes = divisoes + 1
            if(verificacao == 0):
                divisores = divisores + 1
        if(divisores == 2):
            primos = primos + [numero]

else:
    # Repetição
    for numero in (range(-1, n - 1, -1)):
        divisores = 0
        for teste in range(-1, numero - 1, -1):
            verificacao = numero % teste
            divisoes = divisoes + 1
            if (verificacao == 0):
                divisores = divisores + 1
        if (divisores == 2):
            primos = primos + [numero]
print("Os números primos entre 1 e",n,"são:",primos)
print("Para chegar a esse resultado foram prescisas",divisoes,"divisões:")


