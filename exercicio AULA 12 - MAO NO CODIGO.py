# Pense em sistema bancário, nesse sistema há 2 contas: conta-corrente e conta
# poupança.

# Ambas possuem um identificado numérico, nome do titular e saldo. Possuem
# também dois métodos: verificar informações, que retorna todas as informações
# daquela conta e, depósito, que adiciona determinado valor ao saldo daquela
# conta.

# Apenas a conta-corrente possui também o método sacar que subtrai
# determinado valor da conta.

# Apenas a conta poupança possui também um atributo chamado juros.

# Quem utilizará esse sistema é um gerente, portanto, o sistema deve permitir que
# ele crie uma conta-correte ou conta poupança nova e, que consiga utilizar
# todas as funções.

class Conta:
    def __init__(self, identificador_numerico:int, nome_titular:str, saldo:float):
        self.identificador_numerico = identificador_numerico
        self.nome_titular = nome_titular
        self.saldo = saldo

    def verificar_informacoes(self):
        return f"O cliente de n. {self.identificador_numerico}, de nome {self.nome_titular}, possui {self.saldo} na sua conta bancária"

    def deposito(self, valor):
        return f"Foi adicionado o {valor} na conta de {self.nome}"

class conta_corrente(Conta):
    def __init__(self, identificador_numerico:int, nome_titular:str, saldo:float):
        super().__init__(self, identificador_numerico, nome_titular, saldo)
    
    def sacar(self, valor_saque):
        return f"Foi sacado a quantia de {valor_saque} da conta, o cliente {self.nome} ficou com {self.saldo - valor_saque}"
    
class conta_poupanca(Conta):
    def __init__(self, identificador_numerico:int, nome_titular:str, saldo:float, juros:float):
        super().__init__(self, identificador_numerico, nome_titular, saldo)
        self.juros = juros

class gerente(Conta):
    def __init__(self, identificador_numerico:int, nome_titular:str, saldo:float):
        super().__init__(self, identificador_numerico, nome_titular, saldo)
    
    def criar_conta(self, nome):
        return f"Conta criada com sucesso para {nome}"

conta1 = Conta(identificador_numerico=1, nome_titular="Renan", saldo=150.000)




