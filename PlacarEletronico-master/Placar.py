from tkinter import *



janela = Tk()

time1Escudo = PhotoImage(file = "time1.bmp")
janela.title("teste")
janela.geometry("800x600+300+400")

class interface ():
    def __init__(self):
        self.titulo = Label(janela,bg = "red",text = "Nome do Torneio",font = "arial")
        self.titulo.pack(side = TOP,fill = X)

        self.time1 = Label(janela,bg = "blue",width = 30)
        self.time1.pack(side = LEFT, fill = Y)


        self.time1Nome = Label(self.time1, fg = "blue", text = "Nome Do time ", font = "Verdana",width = 30)
        self.time1Nome.pack(side = TOP, anchor = CENTER, fill =X)

        self.time1Imagem = Label(self.time1, image = time1Escudo)
        self.time1Nome.pack(side = TOP, anchor = CENTER)




interface()
janela.mainloop()
