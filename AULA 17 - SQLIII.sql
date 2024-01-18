CREATE DATABASE cadastro;
USE cadastro;

CREATE TABLE usuario(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    cidade VARCHAR(255),
    idade INT
);


INSERT INTO usuario (nome, cidade, idade) VALUES
("João", "Fortaleza", 35),
("Maria", "Recife", 21),
("José", "São Paulo", 40),
("Ana", "Fortaleza", 19),
("Pedro", "Rio de Janeiro", 27),
("Patricia", "Fortaleza", 35),
("Carlos", "Pará", 14),
("Rebeca", "Florianopolis", 54);

CREATE TABLE dependente(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    cidade VARCHAR(255),
    idade INT,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id)
);


INSERT INTO dependente (nome, cidade, idade, id_usuario) VALUES
("Romario", "Recife", 35, 1),
("Jessica", "Recife", 21, 1),
("Diego", "Rio de Janeiro", 40, 4),
("Roberta", "Fortaleza", 19, 6),
("William", "Rio de Janeiro", 27, 2),
("Denise", "São Paulo", 35, 3),
("Wagner", "São Paulo", 14, 3),
("Aline", "São Paulo", 54, 1);

SELECT nome AS nome_cliente, cidade AS cidade_cliente FROM usuario WHERE cidade = "Fortaleza";

SELECT cidade, SUM(idade) AS Soma_das_idades FROM usuario GROUP BY cidade;

SELECT * FROM usuario ORDER BY idade ASC;

SELECT * FROM usuario ORDER BY idade DESC;

SELECT * FROM dependente;

SELECT usuario.nome, dependente.nome 
FROM usuario 
INNER JOIN dependente 
ON usuario.id = dependente.id_usuario
ORDER BY usuario.id;

SELECT 
usuario.nome AS nome_do_usuario,
usuario.cidade AS cidade_usuario,
dependente.nome AS nome_do_dependente,
dependente.cidade AS cidade_dependente 
FROM usuario
INNER JOIN dependente
ON usuario.id = dependente.id_usuario
ORDER BY usuario.id;

SELECT 
usuario.nome AS nome_do_usuario,
usuario.cidade AS cidade_usuario,
dependente.nome AS nome_do_dependente,
dependente.cidade AS cidade_dependente 
FROM usuario
LEFT JOIN dependente
ON usuario.id = dependente.id_usuario
ORDER BY usuario.id ASC;









 
