n=eval(input("Digite quantos termos terá a série de Fibonacci:"))
if(n >= 0):
    t = 0
    x = 0
    y = 1
    while (t < n):
        print(x)
        x = x + y
        t = t + 1
        if(t < n):
            print(y)
            y = y + x
            t = t + 1

else:
    print("O valor não pode ser negativo")
