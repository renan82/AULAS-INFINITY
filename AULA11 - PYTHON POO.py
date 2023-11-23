class carro:
    def __init__(self, marca, ano, modelo, tem_4_portas):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.tem_4_portas = tem_4_portas

carro1 = carro("Ford", 2021, "KA", True)
carro2 = carro("Fiat", 2007, "Uno", False)
print(f"A marca do carro1 é {carro1.marca} e a marca do carro2 é {carro2.marca}")
carro3 = carro(ano=2023, modelo="HB20", tem_4_portas=True, marca="Hyundai")
if carro3.tem_4_portas == True:
    print("O carro tem 4 portas")
else:
    print("O carro não tem 4 portas")

marca = str(input("Qual a marca do carro: "))
ano = int(input("Qual o ano do carro: "))
modelo = str(input("Qual o modelo do carro: "))
portas = bool(input("O carro tem 4 portas: "))

carro4 = carro(modelo=modelo, marca=marca, tem_4_portas=portas, ano=ano) 
print(carro4.marca)