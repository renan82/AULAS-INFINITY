# class televisao():
#     def __init__(self, marca, polegadas, smart, preco, apps):
#         self.marca = marca
#         self.polegadas = polegadas
#         self.smart = smart
#         self.preco = preco
#         self.apps = apps

# tv1 = televisao(marca="Gradiente", polegadas=50, smart=True, preco=2.500, apps=["NETFLIX", "AMAZON", "TELECINE"])

# print(tv1.apps)

# tv2= televisao(marca="LG", polegadas=42, smart=False, preco=1.350, apps=["NETFLIX", "GOOGLE"])

# marca = str(input("Digite a marca da TV: ").upper())
# polegadas = int(input("Digite as polegadas da TV: "))
# smart = bool(input("A TV é SMART ? ").upper())
# if smart == "SIM":
#     smart = True
# else:
#     smart = False
# preco = float(input("Qual o preço da TV? "))
# apps = []
# while True:
#     app = str(input("Quais os aplicativos da TV, quando terminar digite 0 para sair ? "))
#     apps.append(app)
#     if app == "0":
#         apps.pop()
#         break

# tv3 = televisao(marca=marca, polegadas=polegadas, smart=smart, preco=preco, apps=apps)
# print(tv3.marca)
# print(tv3.polegadas)
# print(tv3.smart)
# print(tv3.apps)
# print(tv3.preco)

# class JOGO():
#     def __init__(self, nome, ano_lancamento, genero, preco, estoque):
#         self.nome = nome
#         self.ano_lancamento = ano_lancamento
#         self.genero = genero
#         self.preco = preco
#         self.estoque = estoque

# jogo1 = JOGO("GTA", 2000, "Ação", 350.50, True)

# print(jogo1)

# nome = str(input("Qual nome do JOGO:? "))
# ano_lancamento = int(input("Qual ano de lançamento do JOGO:? "))
# genero = str(input("Qual genero do JOGO:? "))
# preco = float(input("Qual preço do JOGO:? "))
# estoque = bool(input("O JOGO tem no estoque? ").upper())
# if estoque == "SIM":
#     estoque = True
# else:
#     estoque = False

# jogo2 = JOGO(nome=nome, ano_lancamento=ano_lancamento, genero=genero, preco=preco, estoque=estoque)

# if jogo2.preco > 300:
#     print(f" O PREÇO DE {jogo2.preco} TA CARO, ESPERE A BLACK FRAUDE!")
# else:
#     print("O preço tá bom, COMPRE LOGO SEU IDIOTA!")

# if jogo2.estoque == True:
#     print("JOGO DISPONÍVEL NO ESTOQUE")

# class carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.velocidade_atual = 0

#     def ligar(self):
#         return f"O {self.modelo} está ligado"
    
#     def acelerar(self, velocidade):
#         self.velocidade_atual = self.velocidade_atual + 10
#         return self.velocidade_atual
    
#     def freiar(self, velocidade):
#         if  self.velocidade_atual <= 10:
#             self.velocidade_atual = 0
#         else:
#             self.velocidade_atual = self.velocidade_atual - 10
#         return self.velocidade_atual
    
    




# carro1 = carro("CHEVROLET", "GOL", 2020)

# print(carro1.acelerar(10))
# print(carro1.freiar(3))

# class cachorro:
#     def __init__(self, nome, raca, idade, cor, adestrado):
#         self.nome = nome
#         self.raca = raca
#         self.idade = idade
#         self.cor = cor
#         self.adestrado = adestrado
    
#     def comer(self):
#         print("**************")
#         return f"A {self.nome} começou a comer!"
    
#     def dormir(self):
#         print("**************")
#         return f"A {self.nome} agora vai dormir!"
    
#     def adestrado1(self):
#         print("**************")
#         if self.adestrado == False:
#             return f"A {self.nome} não é adestrada!"
#         if self.adestrado == True:
#             return f"A {self.nome} é adestrada!"
                

# cachorro1 = cachorro(nome="ZUKY", raca="YORKSHIRE", idade=3, cor="MARROM", adestrado=True)

# print(cachorro1.dormir())

# print(cachorro1.comer())

# print(cachorro1.adestrado1())

class Fatura:
    def __init__(self, nome, preco, quantidade_de_item):
        self.nome = nome
        self.preco = preco
        self.quantidade_de_item = quantidade_de_item
        
    def  gerar_fatura(self):
        valor_total = self.preco * self.quantidade_de_item
        return f"O item {self.nome} pelo preço unitário a {self.preco}, na quantidade solicitada de {self.quantidade_de_item}, tem-se o valor total da nota na quantia de {valor_total}"
        

    fatura1 = Fatura(nome="MOUSE", preco=35, quantidade_de_item=3)

    fatura1.gerar_fatura()




