create database teste;
drop database teste;

use teste;

CREATE TABLE dados(
id INT(4) AUTO_INCREMENT,
nome VARCHAR(30) NOT NULL,
idade VARCHAR(3) NOT NULL,
nome_mae VARCHAR(30) NOT NULL,
PRIMARY KEY(id)
);

SELECT * FROM dados;

INSERT INTO dados (nome,idade) VALUES ("pedro", "15", "Jakeline");
drop table dados;