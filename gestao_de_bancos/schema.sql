--criacao das tabelas

CREATE TABLE IF NOT EXISTS aluno (
    RA INTEGER NOT NULL UNIQUE,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE NOT NULL,
    PRIMARY KEY(RA)
);

CREATE TABLE IF NOT EXISTS especialidade (
    cod INTEGER NOT NULL UNIQUE,
    nome VARCHAR(255) NOT NULL,
    humanas INTEGER NOT NULL,
    PRIMARY KEY(cod)
);

CREATE TABLE IF NOT EXISTS professor (
    cod INTEGER NOT NULL UNIQUE,
    nome VARCHAR(255) NOT NULL,
    salario INTEGER NOT NULL,
    cod_especialidade INTEGER NOT NULL,
    data_formacao DATE NOT NULL,
    PRIMARY KEY(cod),
    FOREIGN KEY(cod_especialidade) REFERENCES especialidade(cod)
);

CREATE TABLE IF NOT EXISTS disciplina (
    cod INTEGER NOT NULL UNIQUE,
    nome VARCHAR(255) NOT NULL,
    carga INTEGER NOT NULL,
    PRIMARY KEY(cod)
);

CREATE TABLE IF NOT EXISTS turma (
    cod INTEGER NOT NULL UNIQUE,
    cod_aluno INTEGER NOT NULL,
    cod_professor INTEGER NOT NULL,
    cod_disciplina INTEGER NOT NULL,
    PRIMARY KEY(cod),
    FOREIGN KEY(cod_aluno) REFERENCES aluno(RA),
    FOREIGN KEY(cod_professor) REFERENCES professor(cod),
    FOREIGN KEY(cod_disciplina) REFERENCES disciplina(cod)
);

-- insersao de dados 

INSERT INTO aluno (RA, nome, data_nascimento)
VALUES
  (110, 'Ana Carla Sella', '1990-01-31'),
  (111, 'Carla Rodrigues', '1990-12-31'),
  (112, 'Pietro Henrique Sá', '1991-10-10'),
  (113, 'Janete Souza Neta', '1990-07-08'),
  (114, 'Júlio César Xavier', '1991-09-17'),
  (115, 'Fabrícia Lordani', '1990-03-11'),
  (116, 'Patrício Junqueira', '1991-11-08'),
  (117, 'Brian Pereira Silva', '1991-07-17'),
  (118, 'Cássia Martins', '1991-06-18'),
  (119, 'Cláudio Martins', '1991-06-18'),
  (120, 'Cristina Sanches', '1990-02-20');

INSERT INTO disciplina (cod, nome, carga)
VALUES
  (1, 'Matemática 1', 100),
  (2, 'Português 1', 120),
  (3, 'Inglês 1', 60),
  (4, 'Física 1', 60),
  (5, 'Biologia 1', 60),
  (6, 'Geografia 1', 60),
  (7, 'Química 1', 40),
  (8, 'Espanhol 1', 60),
  (9, 'História 1', 40),
  (10, 'Matemática 2', 100),
  (11, 'Português 2', 100),
  (12, 'Inglês 2', 40);

INSERT INTO especialidade (cod, nome, humanas)
VALUES
  (1, 'Matemática', 0),
  (2, 'Português', 1),
  (3, 'História Nacional', 1),
  (4, 'História Internacional', 1),
  (5, 'Inglês Instrumental', 1),
  (6, 'Inglês Avançado', 1),
  (7, 'Física', 0),
  (8, 'Biologia Animal', 0),
  (9, 'Biologia Vegetal', 0),
  (10, 'Espanhol', 1),
  (11, 'Química', 0),
  (12, 'Geografia', 1);

INSERT INTO professor (cod, nome, cod_especialidade, data_formacao, salario)
VALUES
  (1, 'Gilmar Santiago', 3, '2005-08-07', 1000),
  (2, 'Kleber Fonseca', 12, '2005-10-12', 2000),
  (3, 'Jeruza Maria Pereira', 9, '2006-08-07', 3000),
  (4, 'Thiago Santos Padilha', 11, '2008-08-15', 1000),
  (5, 'Michella Cristina Berner', 2, '2004-08-10', 1000),
  (6, 'Érica Junqueira Pereira', 5, '2010-07-05', 2000),
  (7, 'Angela Carreira', 3, '2003-08-05', 2000),
  (8, 'Elaine Clarice Correia', 1, '2003-08-05', 2000);

INSERT INTO turma (cod, cod_aluno, cod_disciplina, cod_professor)
VALUES
  (1, 120, 1, 8),
  (2, 120, 3, 6),
  (3, 120, 10, 8),
  (4, 120, 11, 5),
  (5, 120, 12, 6),
  (6, 110, 10, 4),
  (7, 110, 11, 5),
  (8, 110, 12, 6),
  (9, 111, 9, 1),
  (10, 112, 9, 1),
  (11, 113, 9, 1),
  (12, 113, 4, 7),
  (13, 118, 5, 3),
  (14, 118, 1, 8),
  (15, 118, 2, 5),
  (16, 118, 4, 7),
  (17, 119, 5, 4),
  (18, 119, 1, 8),
  (19, 119, 4, 7),
  (20, 119, 4, 7),
  (21, 117, 1, 8),
  (22, 117, 2, 5),
  (23, 117, 3, 6),
  (24, 117, 4, 7),
  (25, 117, 5, 4),
  (26, 117, 6, 2),
  (27, 117, 7, 4),
  (28, 117, 10, 8),
  (29, 117, 11, 5),
  (30, 117, 12, 6);