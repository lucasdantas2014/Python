def output (texto):
    print(texto)

def tamanho (texto):
    TamanhoTexto = len(texto)
    return TamanhoTexto

def maisculo (texto):
    MaiusculoTexto = texto.upper()
    return MaiusculoTexto

def minusculo (texto):
    MinusculoTexto = texto.lower()
    return MinusculoTexto

def find (texto):
    busca = str(input("Digite a letra que deseja encontrar:"))
    contador = 0
    for letra in texto:
        if (letra == busca):
            contador = contador + 1
    print("A letra",busca,"é encontrada",contador,"vezes no texto")
