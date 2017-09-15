base=eval(input("Digite um valor para ser a base da potenciação:"))
expoente=eval(input("Digite um valor para se o expoente da potenciação:"))
n = 1
resultado = 1
if(expoente >= 0):
    while(n <= expoente):
        resultado = base * resultado
        n = n + 1
    print(resultado)
elif(expoente < 0):
    base = 1/base
    expoente= expoente*(-1)
    while (n <= expoente):
        resultado = base * resultado
        n = n + 1
    print(resultado)

