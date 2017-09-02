# encoding: utf-8
from model.Agenda import Agenda
from model.Contato import Contato
from model.Pessoa import Pessoa
from model.Telefone import Telefone
import json
import datetime
from datetime import date

def CriarAgenda():
    while(True):
        try:
            print(">---Criar Nova Agenda---<")
            nome = str(input("\nDigite o nome do propietário da agenda:\n"))
            dia = int(input("Digite o dia do seu nascmento:"))
            mes = int(input("Digite o numero do mes em que você nasceu:"))
            ano = int(input("Digite o ano em que você nasceu:"))
            nascimento = date(ano,mes,dia)
            email = str(input("Digite o email do propietario: "))

            propietario = Pessoa(nome,nascimento,email)
            agenda = Agenda(propietario)
            return agenda

        except ValueError:
            print("\nVocê digitou um valor inválido tente novamente\nDica: Digite um valor inteiro e um dia possivel no ano:")


def incluirContato(agenda):
    #Criando Objeto Pessoa
    nome = str(input("Digite o nome do conntato:"))
    trueAuxiliar = True
    telefones = []

    while(trueAuxiliar):
        try:
            dia = int(input("Digite o dia do seu nascmento:"))
            mes = int(input("Digite o numero do mes em que você nasceu:"))
            ano = int(input("Digite o ano em que você nasceu:"))
            nascimento = date(ano,mes,dia)


            email = str(input("Digite o email do contato:"))
            pessoa = Pessoa(nome,nascimento,email)

            #Criando Objeto Telefone
            print("\nAdicionar Telefone:")
            numero = int(input("\nDigite o numero do telefone:"))
            ddd = int(input("Digite o ddd do telefone:"))
            codigoPais = int(input("Digie o codigo do Pais\n"))

            telefones.append(Telefone(numero,ddd,codigoPais))
            trueAuxiliar = False
        except ValueError:
            print("\n!!!Valor Inválido, Dica: Digite um valor inteiro e que esteja dentro da quantidade de meses e dias possiveis!!!\n")

    #Criacao do objeto Telefone
    while(True):
        try:
            resposta = int(input("Digite:\n 1-Incluir outro telefone;\n 2- Sair salvar contato."))
            if (resposta == 1):

                print("Adicionar outro telefone")
                numero = int(input("\nDigite o numero do telefone:"))
                ddd = int(input("Digite o ddd do telefone:"))
                codigoPais = int(input("Digie o codigo do Pais\n"))
                telefones.append(Telefone(numero,ddd,codigoPais))

            elif (resposta == 2):
                break

            else:
                print("\n!!!Resposta Inválida!!!\n")

        except ValueError:
            print("\n!!!Digite um número INTEIRO!!!\n")

    #Instanciação e inclusao de contato
    criacao = date.today()
    contato = Contato(criacao,pessoa,telefones)
    agenda.incluirContato(contato)



def listarContatos(agenda):
    lista = agenda.listarContato()
    for contato in lista:
        print("Contato: " +contato.pessoa.nome)
        print("nasc: " + str(contato.pessoa.nascimento))
        print("email: " + contato.pessoa.email)
        contador = 1
        print("::::TELEFONES::::")
        for telefone in contato.telefones:
            print("\nTelefone" + str(contador))
            print("nº:",telefone.numero)
            print("DDD:",telefone.ddd)
            print("Codigo do País:",telefone.codigoPais)

def removerContato(agenda):
    nome = str(input("Digite o nome do contato a ser removido:"))
    agenda.excluirContato(nome)

def buscarContato(agenda):
    nome = str(input("Digite o nome do contato a ser buscado:"))
    auxiliar = 0
    for contato in agenda.contatos:
      if (contato.pessoa.nome == nome):
          print("Contato: " +contato.pessoa.nome)
          print("nasc: " + str(contato.pessoa.nascimento))
          print("email: " + contato.pessoa.email)
          contador = 1
          print("::::TELEFONES::::")
          for telefone in contato.telefones:
              print("\nTelefone" + str(contador))
              print("nº:",telefone.numero)
              print("DDD:",telefone.ddd)
              print("Codigo do País:",telefone.codigoPais)
          break
      auxiliar +=1

def quantidadeContatos(agenda):
    print(agenda.contarContatos())


def default_parser(obj):
    if getattr(obj, "__dict__",None):
        return obj.__dict__

    elif type(obj) == datetime:
        return obj.isoformat()

    else:
        return str(obj)

def extrairSalvar(agenda):
    #Transformando Contato
    auxiliarContato = 0


    salvarAgenda = str(json.dumps(agenda,default = default_parser,indent=4))
    arquivo = open("agenda.json", "w",encoding="utf-8")
    arquivo.write(salvarAgenda)
    arquivo.close()


def main():
    agenda = None
    continuar = True
    telefones = []

    try:
        arquivo = open("agenda.json" ,"r",encoding="utf-8")
        jsontest = json.loads(arquivo.read())
        arquivo.close()
        contatos = []

        for contato in jsontest["contatos"]:
            for telefone in contato["telefones"]:
                numero = telefone["numero"]
                ddd = telefone["ddd"]
                codigoPais = telefone["codigoPais"]
                telefone = Telefone(numero,ddd,codigoPais)
                telefones.append(telefone)

            criacao = contato["criacao"]
            nome = contato["pessoa"]["nome"]
            nascimento = contato["pessoa"]["nascimento"]
            email = contato ["pessoa"]["email"]
            pessoa = Pessoa(nome,nascimento,email)
            contato = Contato(criacao,pessoa,telefones)
            contatos.append(contato)

        nome = jsontest["propietario"]
        agenda = Agenda(nome)
        agenda.contatos = contatos


    except FileNotFoundError:
        agenda = CriarAgenda()

    while(continuar):
        try:
            escolha = int(input("\nDigite o número correspondente a opção deejada:\n\n 1-Criar Agenda;\n 2-Incluir Contato;\n 3-Listar Contatos;\n 4-Remover Contato;\n 5-Buscar Contato; \n 6- Contar Quantidade de Contatos;\n 7- Sair e salvar.\n---->>"))

            if (escolha == 1):
                agenda = CriarAgenda()

            elif (escolha == 2):
                incluirContato(agenda)

            elif (escolha == 3):
                listarContatos(agenda)


            elif (escolha == 4):
                removerContato(agenda)

            elif (escolha == 5):
                buscarContato(agenda)

            elif (escolha == 6):
                quantidadeContatos(agenda)

            elif (escolha == 7):
                extrairSalvar(agenda)
                break

            else:
                print("Opção Inválida")

        except ValueError:
            print("\n---\n!!!!Digite um número inteiro!!!\n---")

if (__name__ == "__main__"):
    main()
