valorI=eval(input("Digite o valor inicial do intervalo:"))
valorF=eval(input("Digite o valor final do intervalo:"))
if (valorI <= valorF):
    intervalo = valorI + 1
    soma = 0
    while(intervalo < valorF):
        print(intervalo)
        soma = intervalo + soma
        intervalo = intervalo + 1
    print("O resultado da soma dos números que estão no intervalo é:",soma)
else:
    print("Valores Invalidos(O valor inicial não pode ser maior que o final)")
