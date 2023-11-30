# class Moto:
#     def __init__(self, marca, modelo, cilindradas):
#         self.marca = marca
#         self.modelo = modelo
#         self.cilindradas = cilindradas

#     def empinar(self):
#         return f"A moto {self.modelo} está empinando!"

# moto1 = Moto("Honda", "Bros", 160)
# moto2 = Moto(marca="Suzuky", modelo="SPIN", cilindradas=400)

# print(moto1.empinar())

# class Serie:
#     def __init__(self, nome, temporadas, genero):
#         self.nome = nome
#         self.temporadas = temporadas
#         self.genero = genero

#     def maratonar(self):
#         return f"{serie1.nome} está sendo maratonada!"


# serie1 = Serie("O MAGICO DE OZ", 4, "INFANTIL")

# serie1.maratonar()
# print(f" --> EM EXECUÇÃO: {serie1.maratonar()}")
# print(f"INFO: {serie1.nome} possui {serie1.temporadas} temporadas!")

# n = str(input("Digite o nome da série: "))
# t = int(input("Quantas TEMPORADAS: "))
# g = str(input("Qual genero: "))

# serie2 = Serie(nome=n, temporadas=t, genero=g)

# print(f"""NOME DA SÉRIE: {serie2.nome}
# TEMPORADAS: {serie2.temporadas}
# GENERO: {serie2.genero}
# """)

# class Filme:
#     def __init__(self, nome, genero, elenco_principal, ano_lancamento):
#         self.nome = nome
#         self.genero = genero
#         self.elenco_principal = elenco_principal
#         self.ano_lancamento = ano_lancamento

#     def informacoes(self):
#         return f"""NOME DA SÉRIE: {self.nome}, 
# GENERO: {self.genero} 
# ELENCO PRINCIPAL: {self.elenco_principal} 
# ANO LANÇAMENTO: {self.ano_lancamento}"""

#     def protagonista(self):
#         return f"O protagonista é: {self.elenco_principal[0]}"

# nome = str(input("Digite o nome do filme: "))
# genero = str(input("Qual genero: "))
# elenco_principal = []
# ano_lancamento = int(input("Digite o ano de lançamento: "))


# while True:
#     elenco = str(input("Digite o nome do elenco ou aperte 0 para sair: "))
#     elenco_principal.append(elenco)
#     if elenco == "0":
#         elenco_principal.pop()
#         break


# filme1 = Filme(nome=nome, genero=genero, elenco_principal= elenco_principal, ano_lancamento=ano_lancamento)

# filme2 = Filme("DRAGON BALL", "AÇÃO", ["RENAN", "JOAO", "DAVI"], 1982)

# print(filme1.informacoes())

# print(filme1.protagonista())

# print(type(filme2))

# AULA 12 - SUPER CLASSES POO (PROGRAMAÇÃO ORIENTADA A OBJETO) II

# class Animal: # (CLASSE SUPER)
#     def __init__(self, nome, raca, especie):
#         self.nome = nome
#         self.raca = raca
#         self.especie = especie

# class cachorro(Animal):
#     def __init__(self, nome, raca, especie, peso):
#         super().__init__(nome, raca, especie) # SUPER são todos os atributos do PY (CLASSE SUPER)
#         self.peso = peso

# class Gato(Animal):
#     def __init__(self, nome, raca, especie, cor_do_olho):
#         super().__init__(nome, raca, especie)
#         self.cor_do_olho = cor_do_olho

# gato1 = Gato(nome="Salem", raca="Siames", especie="Felino", cor_do_olho="Azul")

# cachorro1 = cachorro(nome="Alika", raca="Cockspen", especie="canino", peso=10)

# class Funcionario: #SUPER CLASSE
#     def __init__(self, nome:str, telefone:int, cpf:int, endereco:str):
#         self.nome = nome
#         self.telefone = telefone
#         self.cpf = cpf
#         self.endereco = endereco

#     def bater_ponto(self):
#         return f"O {self.nome} bateu o ponto!"

# class gerente(Funcionario): #SUB CLASSE
#     def __init__(self, nome:str, telefone:int, cpf:int, endereco:str, senha_do_cofre:int):
#         super().__init__(nome, telefone, cpf, endereco)
#         self.senha_do_cofre = senha_do_cofre

#     def demitir(self, nome_do_demitido): #SUB CLASSE
#         return f"O gerente {self.nome} demitiu {nome_do_demitido}"

# class atendente(Funcionario):
#     def __init__(self, nome, telefone, cpf, endereco, numero_cracha, numero_caixa):
#         super().__init__(nome, telefone, cpf, endereco)
#         self.numero_cracha = numero_cracha
#         self.numero_caixa = numero_caixa
#     def fechar_caixa(self):
#         return f"O {self.nome} fechou o {self.numero_caixa}"

# gerente1 = gerente(nome="RENAN", telefone=859993334, cpf=43321033387, endereco="Rua Pedro Rocha, n. 92", senha_do_cofre=22)

# atendente1 = atendente("KARINY", 88124433,  9853442340, "Rua Pedro Rocha", 10, 1) 

# print(gerente1.senha_do_cofre)

# print(gerente1.bater_ponto())

# print(atendente1.cpf)

# print(gerente1.demitir("João"))

# print(gerente1.demitir(atendente1.nome))

# print(atendente1.fechar_caixa())



