CREATE DATABASE aula16;
USE aula16;

CREATE TABLE alunos(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    idade INT
    );

INSERT INTO 
	alunos (nome, idade) 
	VALUES 
	("JOÃO", 25), 
    ("MARIA", 30),
    ("RENAN", 40);


    
SELECT nome FROM alunos WHERE idade > 30;


    
    
    
