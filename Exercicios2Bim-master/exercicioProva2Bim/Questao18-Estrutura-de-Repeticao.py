valores=eval(input("Digite uma lista de numeros:"))
soma = 0
loop1 = 0
for x in valores:
    if(loop1 == 0):
        maior = x
        menor = x
        soma = x + soma
        loop1 = 1
    else:
        if(x < menor):
            menor = x
        elif(x > maior):
            maior = x
        soma = x + soma
        a = x
print("O menor número da lista é:",menor)
print("O maior número da lista é:",maior)
print("O resultado da soma dos números da lista é:",soma)
