valor=eval(input("Digite um número:"))
m = valor
fatorial = m *(m -1 )
if(valor >= 0):
    while(m > 2):
        m = m - 1
        fatorial = fatorial * (m - 1)
    print("A fatorial de", valor, "é:", fatorial)
else:
    print("O número informado não pode ser negativo")