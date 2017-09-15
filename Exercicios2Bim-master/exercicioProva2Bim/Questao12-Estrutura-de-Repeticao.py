valor=eval(input("Digite um número entre 1 a 10:"))
if (valor >= 1 and valor <= 10):
    n=1
    print("Tabuada de",valor,":")
    while(n <= 10):
        resultadoM = valor * n
        print(valor,"x",n,"=",resultadoM)
        n = n + 1
else:
    print("O número informado é Inválido")
