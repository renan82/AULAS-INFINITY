from tkinter import *

def delete():
    sexo_input.delete(0, END)
    nome_input.delete(0, END)

def saudacao():
    nome = nome_input.get()
    sexo = sexo_input.get()
    if sexo.upper() == "F":
        resultado.configure(text=f"Seja bem vinda {nome}!")
        delete()
    else:
        resultado.configure(text=f"Seja bem vindo {nome}!")
        delete()



janela = Tk()
janela.title("               *** PROGAMA DO NOIADO ***")
janela.configure(bg="green")
janela.geometry("400x300")

# https://mybrandnewlogo.com/pt/gerador-de-paleta-de-cores (PALETA DE CORES)
texto = Label(text="Título da tela", foreground="black", background="pink", font="bold") #foreground pode-se usar "fg" e background "bg"
texto.pack()

nome_texto = Label(text= "Digite seu nome: ", fg="red", bg="black")
nome_texto.pack()

nome_input = Entry(width=19)
nome_input.pack()

sexo_texto = Label(text= "Digite seu sexo: ", fg="white", bg="black")
sexo_texto.pack()

sexo_input = Entry()
sexo_input.pack()

resultado = Label(text="", bg="green")
resultado.pack()

botao = Button(janela, text="Enviar", command=saudacao, bg="#20dad8")
botao.pack()




janela.mainloop()



