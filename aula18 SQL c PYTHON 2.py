import mysql.connector

db_config = {"host": "localhost", "user": "root", "password": "mysqladmin102030", "database": "locadora"}

conexao = mysql.connector.connect(**db_config) ## ** (asterisco asterisco) é para quebrar a variável db_config. ## LINHA QUE SE CONECTA NO BANCO DE DADOS

cursor = conexao.cursor()

lista_de_filmes = cursor.fetchall()

def consultar_banco(consulta):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor
    cursor.execute(consulta)
    lista = cursor.fetchall()
    cursor.close()
    conexao.close()
    return lista

def bulir_no_banco(consulta):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor
    cursor.execute(consulta)
    lista1 = cursor.fetchall()
    cursor.close()
    conexao.close()
    return lista1

consulta = f"""INSERT INTO filmes (nome, genero, ano, preco)
            VALUES
            ("{nome}", "{genero}", {ano}, {preco})"""

todos_os_filmes = consultar_banco(consulta="SELECT * FROM filme")
filmes_pos_2005 = bulir_no_banco(consulta="SELECT * FROM filme WHERE ano > 2005")

## CRIE UM MENU PARA A LOCADORA ADICIONAR, VER TODOS OS FILMES, EDITAR FILME, DELETAR FILME, E SAIR) VER FASTAPI