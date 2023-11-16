# DIFERENÇA ENTRE O .pack() E O .grid()
# from tkinter import *
# janela = Tk()
# janela.title("USANDO O GRID")
# janela.geometry("600x400")
# janela.configure(bg="#ced7f7")

# nome_texto = Label(text="Digite seu nome", bg="#ced7f7")
# nome_texto.grid(row=1, column=1) #row --> LINHA e column --> COLUNA

# nome_input = Entry(width=20)
# nome_input.grid(row=1, column=2)

# botao = Button(janela, text="CLIQUE AQUI", width=20)
# botao.grid(row=2, column=1, columnspan=2)

# janela.mainloop()

# ENTENDENDO O MODO PLACE, DIFERENTE DO GRID E DO PACK
from tkinter import *
janela = Tk()
janela.title("USANDO O PLACE")
janela.geometry("600x400")
janela.configure(bg="#ced7f7")

nome_texto = Label(text="Digite seu nome", bg="#ced7f7")
nome_texto.place(x=10, y=10)

nome_input = Entry()
nome_input.place(x=105, y=10)

botao = Button(janela, text="* E N V I A R *", width=31)
botao.place(x=5, y=35)


janela.mainloop()