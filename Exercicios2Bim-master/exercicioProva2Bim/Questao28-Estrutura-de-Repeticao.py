Qcd=eval(input("Digite quantos cds você comprou:"))
valorTotal = 0
for cd in  range(1,Qcd + 1,1):
    print("Digite o valor do cd",cd)
    Vcd=eval(input())
    valorTotal = valorTotal + Vcd
media = valorTotal /Qcd
print("Cada cd custou em media:",media,"R$")
print("Foi gasto",valorTotal,"R$,no total")