class Livro:
    def __init__(self, titulo, autor, id, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponivel = disponivel
    
    def adicionar_livro(self):
        livro = str(input("QUAL LIVRO DESEJA ADICIONAR: ").upper())
        autor = str(input("QUAL O AUTOR DO LIVRO: ").upper())
        identificacao = str(input("QUAL A NUMERAÇÃO DO LIVRO: ").upper())
        disponivel = True
        Livro1 = Livro(titulo=livro, autor=autor, id=identificacao, disponivel=disponivel)
        return Livro1

Livro1.adicionar_livro()

class Membro:
    def __init__(self, nome, numero_menbros, historico_livro):
        self.nome = nome
        self.numero_menbros = numero_menbros
        self.historico_livro = historico_livro


class Biblioteca:
    def __init__(self, catalogo, registro):
        self.catalogo = catalogo
        self.registro = registro
    
    def adicionar(self):
        livro = str(input("QUAL LIVRO DESEJA ADICIONAR: ").upper())
        autor = str(input("QUAL O AUTOR DO LIVRO: ").upper())
        identificacao = str(input("QUAL A NUMERAÇÃO DO LIVRO: ").upper())
        disponivel = True
    def emprestimo(self):
        
    def devolucao(self):

    def pesquisa(self):
#         


while True:
    menu = str(input("""O QUE DESEJA FAZER:
1 - ADICIONAR LIVRO
2 - ADICIONAR MEMBRO
3 - TOMAR EMPRÉSTIMO POR MEMBRO
4 - REGISTRAR DEVOLUCAO
5 - PESQUISAR LIVRO
6 - SAIR
"""))
    if menu == "1":
        adicionar = str(input("NOME DO LIVRO: ").upper())
        autor = str(input("AUTOR DO LIVRO:"))
        ident = int(input("ID DO LIVRO: "))
        Livro1 = Livro(nome=adicionar, numero_membros=autor, id=ident, disponivel="Sim")

        

    
    
    
    
    
    
    
    
    
    
    
    
    if menu == "2":
        devolver = str(input("Qual livro deseja devolver: ").upper())
        livros.append(devolver)
        print("LIVRO DEVOLVIDO COM SUCESSO")
    if menu == "3":
        emp = str("QUAL LIVRO DESEJA EMPRESTADO: ")
            if emp in self.catalogo:
                print("Livro disponível")
    if menu == "4":
        print("OBRIGADO, VOLTE SEMPRE!")
        break

            