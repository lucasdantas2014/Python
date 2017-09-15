notas=eval(input("Digite as notas:"))
soma = 0
contador = 0
for n in notas:
    soma = soma + n
    contador = contador + 1
media = soma / contador
print("A media das notas é:",media)