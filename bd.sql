
CREATE DATABASE bd;
USE bd;
CREATE TABLE aluno (
    id INT(4) AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    matricula VARCHAR(11),
    cpf VARCHAR(11),
    curso VARCHAR(20),
    PRIMARY KEY (id)
);
CREATE TABLE tecadm (
    id INT(4) AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(100),
    telefone VARCHAR(20),
    cpf VARCHAR(11),
	salario VARCHAR(11),
    PRIMARY KEY (id)
);
CREATE TABLE professor (
    id INT(4) AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(100),
    telefone VARCHAR(20),
    cpf VARCHAR(11),
	salario VARCHAR(11),
    titulacao VARCHAR(11),
    formacao VARCHAR(11),
    PRIMARY KEY (id)
);
CREATE TABLE curso (
    codigo VARCHAR(11),
    nome VARCHAR(50) NOT NULL,
    duracao VARCHAR(11),

    PRIMARY KEY (codigo)
);
CREATE TABLE disciplina (
    codigo VARCHAR(11),
    nome VARCHAR(50) NOT NULL,
    cargahoraria VARCHAR(11),

    PRIMARY KEY (codigo)
);




















