import mysql.connector

db_config = {"host": "localhost", "user": "root", "password": "mysqladmin102030", "database": "locadora"}

conexao = mysql.connector.connect(**db_config) ## ** (asterisco asterisco) é para quebrar a variável db_config. ## LINHA QUE SE CONECTA NO BANCO DE DADOS

cursor = conexao.cursor()
cursor.execute("SELECT * FROM filme")
lista_de_filmes = cursor.fetchall() ## fetchall -> GUARDAR TABELA NA VARIÁVEL


# for filme in lista_de_filmes:
#     print(filme)


    
# cursor.execute(""" INSERT INTO filme (nome, genero, ano, preco)
#                VALUES
#                ("As Branquelas", "Comédia", 2020, 4.50) 
#                """)
# conexao.commit() ## COMANDO COMMIT --> CONFIRMAR/SALVAR AS ALTERAÇÕES (AS ALTERAÇÕES SÃO ADICIONAR, EDITAR E DELETAR)

cursor.execute("""DELETE FROM filme WHERE id = 12""")

nome = str(input("Digite o nome do filme: "))
genero = str(input("Digite o genero do filme: "))
ano = int(input("Digite o ano do filme: "))
preco = float(input("Digite o preço do filme: "))

cursor.execute(f"""INSERT INTO filme (nome, genero, ano, preco)
               VALUES
               ("{nome}", "{genero}", {ano}, {preco})
               """)
conexao.commit()





# cursor.close() ##FECHA A EXECUÇÃO
# conexao.close() ## FECHA A CONEXÃO




