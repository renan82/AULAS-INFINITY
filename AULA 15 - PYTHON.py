class Pessoa:
    def __init__(self, nome, maconheiro):
        self.nome = nome
        self.maconheiro = maconheiro

    def fumar(self):
        self.maconheiro = True
        if self.maconheiro == True:
            return f"{self.nome} está fumando.."
        else:
            print("não está")

    def Cadastro(self):
        self.cadastro = []
        while True:
        
            nome = input("Digite um nome para adicionar ou 'SAIR': ")
            self.cadastro.append(nome)
            if nome == "SAIR":
                break

nome = input("Digite seu nome: ")

nome1 = Pessoa(nome, "sim")

nome1.Cadastro()

print(nome1.fumar())
