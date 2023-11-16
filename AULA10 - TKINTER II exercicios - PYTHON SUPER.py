# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR UMA FRASE E MOSTRE NA TELA QUANTAS VOGAIS, QUANTAS CONSOANTES E QUANTOS ESPAÇOS VAZIOS CONTÉM AQUELA FRASE.
# from tkinter import *

# def contar_letras():
#     frase = frase_input.get()
#     countv = 0
#     countc = 0
#     counte = 0
#     for letra in frase:
#         if letra.lower() in "aeiou":
            
#             countv += 1
            
#         elif letra.lower() in "bcdfghjklmnpqrstvxywz":
            
#             countc = countc + 1
#         elif letra == " ":
            
#             counte += 1
#     resultado.configure(text=f"""
#                             A frase '{frase}' :
#                             Contém {countv} VOGAIS!
#                             Contém {countc} CONSOANTES!
#                             Contém {counte} ESPAÇOS!
#                             """)
#     frase_input.delete(0, END)

# janela = Tk()
# janela.title("CONTADOR DE LETRAS")
# janela.geometry("400x300")

# frase = Label(text="Digite uma frase qualquer idiota: ", font="bold", fg="red")
# frase.pack()

# frase_input = Entry(width=100)
# frase_input.pack()

# resultado = Label(text="")
# resultado.pack()

# botao = Button(janela, text="EXECUTAR", command=contar_letras)
# botao.pack()

# janela.mainloop()


# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR UMA COR DO SEMÁFORO E MOSTRE NA TELA UMA MENSAGEM CUSTOMIZADA DE ACORDO COM A ESCOLHA DO USUÁRIO
# SE ELE DIGITAR 'verde' MOSTRE NA TELA 'Acelera' DA COR VERDE
# SE ELE DIGITAR 'amarelo' MOSTRE NA TELA 'Atenção' DA COR AMARELO
# SE ELE DIGITAR 'vermelho' MOSTRE NA TELA 'Pare!' DA COR VERMELHO
# SE ELE DIGITAR OUTRA COR MOSTRE NA TELA 'Cor inválida' DA COR AZUL
import time
# janela = Tk()
# janela.title("JOGO DO SEMÁFORO")
# janela.configure(bg="white")
# janela.geometry("600x400")

# def cores():
#     cor = texto_input.get()
#     if cor.lower() == "verde":
#         time.sleep(1)
#         resultado.configure(text="ACELERA", fg="green")
#         botao.configure(bg="green")
#     elif cor.lower() == "amarelo":
#         time.sleep(1)
#         resultado.configure(text="ATENÇÃO", fg="yellow", font="bold")
#         botao.configure(bg="yellow")
#     elif cor.lower() == "vermelho":
#         time.sleep(1)
#         resultado.configure(text="PARE", fg="red")
#         botao.configure(bg="red")
#     else:
#         time.sleep(1)
#         resultado.configure(text="COR INVÁLIDA", fg="blue")
#         botao.configure(bg="blue")
    
#     texto_input.delete(0, END)

# texto = Label(text="DIGITE UMA COR DO SEMÁFORO:", font="calibri", fg="#662737", bg="#b69fff")
# texto.pack()

# texto_input = Entry(fg="black", bg="#fff2f7")
# texto_input.pack()

# resultado = Label(text="", fg="white", bg="white")
# resultado.pack()

# botao = Button(janela, text="*RESULTADO*", command=cores)
# botao.pack()




# janela.mainloop()
# janela = Tk()
# janela.title("Semáforo Modelo 2") # CRIANDO UM NOVO PROGRAMA A PARTIR DOS CLIQUES DOS BOTOES E SUAS CORES"
# janela.geometry("400x300")

# def vermelho():
#     resultado.configure(text="SINAL VERMELHO, PARE!", bg="red")

# def amarelo():
#     resultado.configure(text="SINAL AMARELO, ATENÇÃO!", bg="yellow")

# def verde():
#     resultado.configure(text="SINAL AZUL, PARE!", bg="green")

# botao_vermelho = Button(width=10, bg="red", command=vermelho)
# botao_vermelho.pack()

# botao_amarelo = Button(width=10, bg="yellow", command=amarelo)
# botao_amarelo.pack()

# botao_verde = Button(width=10, bg="green", command=verde)
# botao_verde.pack()

# resultado = Label(text=" ")
# resultado.pack()

# janela.mainloop()

# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR UMA SENHA E MOSTRE NA TELA SE ELA É UMA SENHA FORTE OU FRACA
# UMA SENHA FORTE CONTÉM:
# PELO MENOS UMA LETRA
# PELO MENOS UM NÚMERO
# NO MÍNIMO 8 CARACTERS
from tkinter import *
janela = Tk()
janela.title("VERIFICADOR DE SENHA")
janela.geometry("400x300")
janela.configure(bg="#657ecd")

def verificacao():
    senha = senha_input.get()
    tem_letra = False
    tem_numero = False
    if len(senha) >= 8:
        for caracter in senha:
            if caracter.lower() in "abcdefghijklmnopqrstuvxywz":
                tem_letra = True
            elif caracter in "1234567890":
                tem_numero = True
        if tem_numero == True and tem_letra == True:
                resultado.configure(text="SENHA FORTE, PARABÉNS!")
        else:
            resultado.configure(text="SENHA FRACA!")
    else:
        resultado.configure(text="SENHA FRACA!")     


senha = Label(text="Digite uma Senha forte", bg='#657ecd')
senha.pack()

obs = Label(text="""OBS: A senha deve SER MAIOR QUE 8 CARACTERES
E CONTER LETRAS E NÚMEROS!""", fg='red', bg='#657ecd')
obs.pack()
           

senha_input = Entry(width=10)
senha_input.pack()

resultado = Label(text="", bg="#657ecd")
resultado.pack()

botao = Button(janela, text="*CLIQUE PARA CONFERIR!*", command=verificacao)
botao.pack()

janela.mainloop()

