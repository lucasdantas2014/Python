print("Panificadora Pão de Ontem - Tabela de preços")
preco=eval(input("Digite o preço do pão:"))
for pao in range(1,51,1):
    print(pao,"- R$",pao * preco)

