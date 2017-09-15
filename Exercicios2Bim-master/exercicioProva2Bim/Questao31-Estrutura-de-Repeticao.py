while(True):
    numproduto = []
    n = 1
    c = 0
    Cvalor = []
    Tvalor = 0
    while(n != 0):
        c = c + 1
        valor=eval(input("Digite o valor do produto:"))
        Cvalor = Cvalor + [valor]
        Tvalor = Tvalor + 1
        n = valor
        numproduto = numproduto + [c]
    for produto in range(1,c,c):
