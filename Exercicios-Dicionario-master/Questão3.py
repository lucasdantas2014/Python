produtos = {}
a1 = True

def cadastrarPrduto(produtos, produto, preco):
    produtos[produto] = preco

def exibirProdutos(produtos):
    items = produtos.items()
    for item in items:
        print("Produto-",item[0],"Preço-",item[1])

def removerProduto(produtos,produto):
    produtos.pop(produto)


def exibirCaroProduto(produtos):
    items = produtos.items()
    produtosCaros = []
    caro = 0
    produtoCaro = ""
    for item in items:
      if (item[1] > caro):
        caro = item[1]
        produtoCaro = item[0]
        a = 1
      
      elif(item[1] == caro):
        produtosCaros.append(item)
        a = 0

     else:
        None

   if(a == 0):
        print("Os produtos mais caros são: ",produtosCaros)

   else:
        print("O produto  -->>",produtoCaro,"Preço-->>",caro)
        

def exibirBaratoProduto(produtos):
    items = produtos.items()
    produtosBaratos = []
    barato = 99999999999999999999999999999999999999999999999999999999999999999999999999
    produtoBarato = ""
    a = 1
    for item in items:
        if (item[1] < barato):
            barato = item[1]
            produtoBarato = item[0]
            a = 1

       elif(item[1] == barato):
            produtosBaratos.append(item)
            a = 0

       else:
            None

   if(a == 0):
        print("Os produtos mais baratos são: ",produtosBaratos)

   else:
        print("O produto  -->>",produtoBarato,"Preço-->>",barato)

while(a1 == True):
    print(" 1- Cadastrar Produto \n 2- Exibir Produtos \n 3- Remover Produto \n 4- Exibir Produto Mais Caro \n 5- Exibir Produto Mais Barato;")
    escolha = int(input("Digite  numero  da opção que você deseja executar:"))

   if(escolha == 1):
      produto = str(input("Digite o nome do produto a ser adicionado a lista: "))
      preco = float(input("Digite o preço do produto informado: "))
      cadastrarPrduto (produtos,produto, preco )
      
    elif(escolha == 2):
      exibirProdutos(produtos)
      
    elif(escolha == 3):
      produto = str(input("Digite o nome do produto a ser retirado da lista: "))
      removerProduto(produtos, produto)
      
    elif(escolha == 4):
      exibirCaroProduto(produtos)
      
    elif(escolha == 5):
      exibirBaratoProduto(produtos)
      
    else:
      print("A opção escolhida não exite.Tente Novamente")
