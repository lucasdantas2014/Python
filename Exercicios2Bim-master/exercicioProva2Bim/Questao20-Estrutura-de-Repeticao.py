calcular = True
while(calcular == True):
    valor = int(input("Digite um número:"))
    m = valor
    fatorial = m *(m -1 )
    if(valor > 0 and valor < 16):
        while(m > 2):
            m = m - 1
            fatorial = fatorial * (m - 1)
        print("A fatorial de", valor, "é:", fatorial)

    else:
        print("O NÚMERO INFORMADO TEM QUE SER POSITIVO E MENOR QUE 16")
        print("Tente Novamente")
    resposta = int(input("Digite 1 se quiser continuar ou 2 se quiser parar:"))
    if(resposta == 1):
        calcular = True
    else:
        calcular = False
print("Volte Sempre")