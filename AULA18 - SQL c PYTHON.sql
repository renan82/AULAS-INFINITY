CREATE DATABASE locadora;
USE locadora;

CREATE TABLE filme(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
	genero VARCHAR(30),
    ano YEAR,
	preco FLOAT
    );
    
CREATE TABLE cliente(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    idade CHAR(3),
    endereco VARCHAR (255)
	);

INSERT INTO filme (nome, genero, ano, preco)
VALUES
("Magico de Oz", "aventura", 1957, 3.50),
("De volta para o futuro", "ficção", 1982, 7.20),
("Avatar", "ficção", 2004, 4.99),
("Alladin", "infantil", 2000, 4),
("Os Goonies", "aventura", 1975, 6.40),
("Os indomáveis", "Western", 2012, 5.20),
("It II", "terror", 2017, 12.50),
("Os idiotas", "ação", 2018, 8.50),
("Estelar", "ficção", 2015, 5.50),
("Titanic", "suspense", 2001, 4.50);

INSERT INTO cliente (nome, idade, endereco)
VALUES
("Renan", 41, "Rua Maria Tomasia, 170, ap 505, Fortaleza-CE"),
("Roberta", 42, "Rua Marcos Macedo, 810, ap 704, Fortaleza-CE"),
("Davi", 38, "Rua Leonardo Mota, 400, ap 1201, Fortaleza-CE"),
("Kariny", 42, "Rua Maria Tomasia, 170, ap 505, Fortaleza-CE"),
("Gracy", 66, "Rua Maria Mirian F de Souza, 88, ap 133, Fortaleza-CE");

CREATE TABLE aluguel(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    id_filme INT,
    FOREIGN KEY (id_cliente)  REFERENCES cliente (id),
    FOREIGN KEY (id_filme)  REFERENCES filme (id)
    );
    

INSERT INTO aluguel (id_cliente, id_filme)
VALUES
(1, 3),
(1, 5),
(2, 1),
(2, 2),
(2, 8),
(5, 7),
(5, 9),
(5, 10);

UPDATE filme SET nome = "Nárnia", genero = "Fantasia", ano = 2003, preco = 4.50 WHERE id = 4;

DELETE FROM filme WHERE id = 6;

SELECT * FROM filme;

SELECT nome, ano FROM filme WHERE ano > 2010;

SELECT nome, preco FROM filme WHERE preco < 5;

SELECT cliente.nome, filme.nome
FROM cliente
INNER JOIN aluguel
ON cliente.id = aluguel.id_cliente, filme.id = aluguel.id_filme;






















    
    
    
    