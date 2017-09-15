valores=eval(input("Digite dez valores:"))
impar=0
par=0
for n in valores:
    if (n % 2 == 0):
        print(n,"é par")
        par = par + 1
    else:
        print(n, "é impar")
        impar = impar + 1
print("Há",par,"valores que são pares")
print("Há",impar,"valores são impares")
