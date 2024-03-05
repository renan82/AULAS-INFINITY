class Elevador:
    def __init__(self, totalcapacidade, atualcapacidade, totalandar, andaratual):
        self.totalcapacidade = totalcapacidade
        self.atualcapacidade = atualcapacidade
        self.totalandar = totalandar
        self.andaratual = andaratual
    
    def subir(self):
        andar = int(input("Qual andar quer ir? "))
        if andar <= 20:
            print(f"Você está no andar {self.andaratual}, SUBINDO até o {andar}!")
        else:
            print("VOCÊ JÁ ESTÁ NO ANDAR MAIS ALTO!")
    
    def descer(self):
        andar = int(input("Qual andar quer ir? "))
        terreo = 0
        if andar == terreo:
            print(f"Você já está no térreo !")
        else:
            print(f"DESCENDO ATÉ O {andar}!")

    def entrar(self):
        if atualcapacidade == 15:
            print(" --> O ELEVADOR ESTÁ CHEIO!")
        else:
            print(" --> Entrando uma pessoa...")
    
    def sair(self):
        if self.atualcapacidade == 0:
            print("NÃO TEM NINGUEM NO ELEVADOR...")
        else:
            print("SAINDO DO ELEVADOR..!")

atualcapacidade = int(input("Quantas pessoas tem no elevador? "))
andaratual = int(input("Em que andar você está: "))


elevador1 = Elevador(totalcapacidade=15, atualcapacidade=atualcapacidade, totalandar=20, andaratual=andaratual)

while True:
    
    menu1 = print("""=== MENU ELEVADOR ==
                 1 - SUBIR 
                 2- DESCER 
                 3 - ENTRAR NO ELEVADOR
                 4 - SAIR DO ELEVADOR
                 5 - SAIR DO MENU""")
    menu = int(input("ESCOLHA UMA OPÇÃO: "))
    
    if menu == 1:
        elevador1.subir()
    if menu == 2:
        elevador1.descer()
    if menu == 3:
        elevador1.entrar()
    if menu == 4:
        elevador1.sair()
    if menu == 5:
        print("FINALIZANDO...")
        break
    





    



