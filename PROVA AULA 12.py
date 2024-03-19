class Material:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def exibir_informacoes(self):
        print(f" TÍTULO: {self.titulo} - AUTOR: {self.autor}")

class Livro(Material):
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero= genero

    def exibir_informacoes(self):
        print(f" GENERO do Livro {self.titulo}: {self.genero}")

class Revista(Material):
    def __init__(self, titulo, autor, edicao):
        self.titulo = titulo
        self.autor = autor
        self.edicao= edicao

    def exibir_informacoes(self):
        print(f" A EDIÇÃO DO LIVRO {self.titulo}, do Autor {self.autor} é a {self.edicao} edição!")

livro1 = Livro("O Mágico de OZ", "Jonnhy Deep", "Fantasia")

livro2 = Livro("50 TONS DE CINZA", "Maria Carrey", "Romance")

revista1 = Revista("CAPRICHO", "João da Penha", "3a edição")

revista2 = Revista("EXAME", "Carlito Pamplona", "1a edição")

print("A seguir algumas informações sobre os Livros e Revistas cadastrados:")
print("-" * 8)

livro1.exibir_informacoes()

livro2.exibir_informacoes()

revista1.exibir_informacoes()

revista2.exibir_informacoes()