# from tkinter import *

# janela = Tk()
# janela.title("               *** MEDIA DO ALUNO ***")
# janela.configure(bg="pink")
# janela.geometry("400x300")

# def calcular(n1, n2, n3):
#     nota1 = float(nota1_input.get())
#     nota2 = float(nota2_input.get())
#     nota3 = float(nota3_input.get())
#     media = (nota1 + nota2 + nota3) /3
   
#     if media1 == 10:
#         resultado.configure(text=f"Nota 10, brabo!", fg="blue")
#     elif media1 >= 7 and media1 < 10:
#         resultado.configure(text=f"Nota boa, Aprovado!", fg="green")
        
#     elif media1 < 7:
#         resultado.configure(text=f"Nota ruim, REPROVADO!", fg="red")
#     else:
#         resultado.configure(text=f"NOTAS INVÁLIDAS, fg="red")

# nota1 = Label(text="Digite a primeira nota do aluno: ")
# nota1.pack()

# nota1_input = Entry(width=10)
# nota1_input.pack()

# nota2 = Label(text="Digite a segunda nota do aluno: ")
# nota2.pack()

# nota2_input = Entry()
# nota2_input.pack()

# nota3 = Label(text="Digite a segunda nota do aluno: ")
# nota3.pack()

# nota3_input = Entry()
# nota3_input.pack()


# resultado = Label(text="", bg="green")
# resultado.pack()

# botao = Button(janela, text=f"CALCULAR MEDIA", command=calcular)
# botao.pack()

# janela.mainloop()




# https://mybrandnewlogo.com/pt/gerador-de-paleta-de-cores

# from tkinter import *

# telinha = Tk()
# telinha.title("Aula Infinity")
# telinha.configure(bg="#ff60a9")
# telinha.geometry("400x300")



# def saudacao():
#     sexo = sexo_input.get()
#     nome = nome_input.get()

#     if sexo.upper() == "F":
#         resultado.configure(text=f"Seja vem vinda {nome}")
#     elif sexo.upper() == "M":
#         resultado.configure(text=f"Seja vem vindo {nome}")
#     else:
#         resultado.configure(text=f"Seja vem vinde {nome}")

#     sexo_input.delete(0, END)
#     nome_input.delete(0, END)



# titulo = Label(text="Título da telinha", bg="#ff60a9")
# titulo.pack()

# nome_texto = Label(text="Digite o seu nome: ", bg="#ff60a9")
# nome_texto.pack()

# nome_input = Entry(width=18)
# nome_input.pack()

# sexo_texto = Label(text="Digite seu sexo [M | F]", bg="#ff60a9")
# sexo_texto.pack()

# sexo_input = Entry()
# sexo_input.pack()

# resultado = Label(text="", bg="#ff60a9")
# resultado.pack()

# teste = ""


# botao = Button(telinha, text="Enviar", command=saudacao)
# botao.pack()



# telinha.mainloop()




# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR 3 NOTAS E MOSTRA NA TELA QUAL A MÉDIA DESSAS NOTAS
# SE ELE TIROU 10 UMA MENSAGEM COM "Tu é brabo" da cor azul
# SE ELE TIROU ACIMA DE 7 UMA MENSAGEM COM "Aprovado" da cor verde
# SE ELE TIROU ABAIXO DE 7 UMA MSANGEM COM "Reprovado" da cor vermelho





# from tkinter import *

# janela = Tk()
# janela.title("Média")
# janela.geometry("300x300")


# def calcular():
#     nota1 = float(nota1_input.get())
#     nota2 = float(nota2_input.get())
#     nota3 = float(nota3_input.get())
#     media = (nota1 + nota2 + nota3) / 3

#     if media == 10:
#         resultado.configure(text="Tu é brabo", fg="blue")
#     elif media >=7 and media <10:
#         resultado.configure(text="Aprovado", fg="green")
#     elif media < 7 and media >= 0:
#         resultado.configure(text="Reprovado", fg="red")
#     else:
#         resultado.configure(text="Notas inválidas", fg="yellow")



        


# nota1_texto = Label(text="Digite a primeira nota: ")
# nota1_texto.pack()

# nota1_input = Entry()
# nota1_input.pack()

# nota2_texto = Label(text="Digite a segunda nota: ")
# nota2_texto.pack()

# nota2_input = Entry()
# nota2_input.pack()

# nota3_texto = Label(text="Digite a terceira nota: ")
# nota3_texto.pack()

# nota3_input = Entry()
# nota3_input.pack()

# resultado = Label(text="")
# resultado.pack()


# botao = Button(janela, text="CLIQUE PARA CALCULAR A MÉDIA", command=calcular)
# botao.pack()


# janela.mainloop()








# from tkinter import *

# janela = Tk()
# janela.title("Média")
# janela.geometry("300x300")


# def calcular():
#     nota1 = float(nota1_input.get())
#     nota2 = float(nota2_input.get())
#     nota3 = float(nota3_input.get())
#     media = (nota1 + nota2 + nota3) / 3

#     if media == 10:
#         resultado.configure(text="Tu é brabo", fg="blue")
#     elif media >=7 and media <10:
#         resultado.configure(text="Aprovado", fg="green")
#     elif media < 7 and media >= 0:
#         resultado.configure(text="Reprovado", fg="red")
#     else:
#         resultado.configure(text="Notas inválidas", fg="yellow")



        


# nota1_texto = Label(text="Digite a primeira nota: ")
# nota1_texto.pack()

# nota1_input = Entry()
# nota1_input.pack()

# nota2_texto = Label(text="Digite a segunda nota: ")
# nota2_texto.pack()

# nota2_input = Entry()
# nota2_input.pack()

# nota3_texto = Label(text="Digite a terceira nota: ")
# nota3_texto.pack()

# nota3_input = Entry()
# nota3_input.pack()

# resultado = Label(text="")
# resultado.pack()


# botao = Button(janela, text="Calcular Média", command=calcular)
# botao.pack()


# janela.mainloop()




# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR UMA FRASE E MOSTRA NA TELA QUANTAS VEZES CADA VOGAL APARECE NA FRASE QUE ELE DIGITOU, POR EXEMPLO:
# "A aula hoje ta muito massa"
# a - 6
# e - 1
# i - 1
# o - 2
# u - 2
from tkinter import * 
janela = Tk()
janela.title("MÉDIA DO ALUNO")
janela.geometry("600x400")

def contar():
    frase = frase_input.get()
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    
    for letra in frase:
        if letra.lower() == "a":
            contador_a = contador_a + 1
        elif letra.lower() == "e":
            contador_e = contador_a + 1
        elif letra.lower() == "i":
            contador_e = contador_a + 1
        elif letra.lower() == "e":
            contador_e = contador_a + 1
        elif letra.lower() == "e":
            contador_e = contador_a + 1

    resultado.configure(text=f"""
                        Quantidade de vogais:
                        a - {contador_a}
                        e - {contador_e}
                        i - {contador_i}
                        o - {contador_o}
                        u - {contador_u}
                        """)

    

frase_texto = Label(text="Digite sua frase: ")
frase_texto.pack()

frase_input = Entry(width=20)
frase_input.pack()

resultado = Label(text="")
resultado.pack()

botao = Button(text="CLIQUE PARA PROSSEGUIR", command=contar)
botao.pack()

janela.mainloop()



