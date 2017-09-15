from Carro import Carro
from Hibrido import Hibrido

def main():

    cor = input("Digite a cor do seu carro:")
    modelo = input("Digite o modelo do seu carro:")
    ano = input("Digite o ano do seu carro:")

    carro1 = Carro(cor,modelo,ano)

    carros = [carro1]

    cor = input("Digite a cor do seu Hibrido:")
    modelo = input("Digite o modelo do seu Hibrido:")
    ano = input("Digite o ano do seu Hibrido:")

    hibrido1 = Hibrido(cor,modelo,ano)

    hibridos = [hibrido1]
    carro1.acelerar()

    hibrido1.freiar()
    hibrido1.carregarBateria()
    
  #Identidade
    Carro2 = Carro ("amarelo","Ferrari",12)
    Carro3  = carro1
    print(carro1)
    print(carro2)
    print(Carro 3)
    
    
    while(True):
        escolha = int(input("\n\n\n O que desejas:\n 1-acelerar Carro\n 2-freiarCarro\n3-acelerarHibrido\n5- CriarCarro\n6-CriarHibrido"))

        if(escolha == 1):
            numero = int(input("Digite o numero do seu carro\n:"))
            carros[numero].acelerar()

        elif(escolha == 2):
            numero = int(input("Digite o numero do seu carro:\n"))
            carros[numero].freiar()

        elif(escolha == 3):
            numero = int(input("Digite o numero do seu Hibrido:\n"))
            carros[numero].acelerar()

        elif(escolha == 5):

            cor = input("Digite a cor do seu carro:")
            modelo = input("Digite o modelo do seu carro:")
            ano = input("Digite o ano do seu carro:\n")

            carro = Carro(cor,modelo,ano)

            carros.append(carro)

        elif(escolha == 6):

            cor = input("Digite a cor do seu Hibrido:")
            modelo = input("Digite o modelo do seu Hibrido:")
            ano = input("Digite o ano do seu Hibrido:\n")

            hibrido = Hibrido(cor,modelo,ano)

            hibridos.append(carro)










if __name__ == '__main__':
    main()








   #t  T
 # (
