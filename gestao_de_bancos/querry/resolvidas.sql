-- 1) Mostre todos os professores, sem repetição, que já deram aula de História 1
SELECT DISTINCT p.Nome
FROM professor AS p
INNER JOIN turma AS t ON p.Codigo = t.CodProfessor
INNER JOIN disciplina AS d ON d.Codigo = t.CodDisciplina
WHERE d.Nome = 'História 1';

-- 2) Mostre todas as especialidade ordenadas de Z a A

SELECT nome
FROM especialidade 
ORDER BY nome DESC;

-- 3) Mostre todas as disciplinas que a aluna Ana Carla Já fez

SELECT d.Nome AS Disciplina
FROM turma t
INNER JOIN aluno a ON t.CodAluno = a.RA
INNER JOIN disciplina d ON t.CodDisciplina = d.Codigo
WHERE a.Nome = 'Ana Carla Sella';

-- 4) Mostre todas as especialidades que estão sem professores
SELECT Nome AS Especialidade
FROM especialidade
WHERE Codigo NOT IN (SELECT CodEspecialidade FROM professor);

-- 5) Mostre todos os professores, sem repetição, que estão ministrando alguma disciplina
SELECT DISTINCT p.Nome AS Professor
FROM professor p
INNER JOIN turma t ON p.Codigo = t.CodProfessor;

-- 6) Mostre a média entre os salários de todos os professores

SELECT AVG(Salario) AS MediaSalario
FROM professor;

-- 7) Mostre a média dos salários dos professores por área de conhecimento (ex. Humanas)

SELECT AVG(p.Salario) AS MediaSalarioArea
FROM professor p
INNER JOIN especialidade e ON p.CodEspecialidade = e.Codigo
GROUP BY e.Humanas;

-- 8) Mostre a quantidade de especialidades cadastradas

SELECT COUNT(*) AS QuantidadeEspecialidade
FROM especialidade;

-- 9) Mostre a soma total dos salários
SELECT SUM(Salario) 
FROM professor;

-- 10) Mostre o nome e o salário dos professores que são da especialidade de Matemática
SELECT p.Nome, p.Salario
FROM professor p
INNER JOIN especialidade e ON p.CodEspecialidade = e.Codigo
WHERE e.nome = 'Matemática';

-- 11) Mostre o nome de todos os professores que 'dão' aula da disciplina de Matemática
SELECT p.Nome, d.Nome
FROM professor p
INNER JOIN turma t ON p.Codigo = t.CodProfessor
INNER JOIN disciplina d ON t.CodDisciplina = d.Codigo
WHERE d.Nome = 'Matemática 1'
GROUP BY p.Nome, d.Nome;

-- 12) Mostre o nome, sem repetição, de todos os professore que já deram aula de história 1
SELECT DISTINCT p.Nome
FROM professor AS p
INNER JOIN turma AS t ON p.Codigo = t.CodProfessor
INNER JOIN disciplina AS d ON d.Codigo = t.CodDisciplina
WHERE d.Nome = 'História 1';

-- 13) Liste o nome de todos os alunos que tiveram aula com professores de Humanas
SELECT DISTINCT a.nome
FROM aluno AS A
JOIN turma t ON a.RA = t.CodAluno
JOIN professor p ON t.CodProfessor = p.Codigo
JOIN especialidade e ON p.CodEspecialidade = e.Codigo
WHERE e.Humanas = 1;

-- 14) Mostre todas as disciplinas que nunca foram ministradas
SELECT d.nome 
FROM disciplina d
LEFT JOIN turma t ON d.Codigo = t.CodDisciplina
WHERE t.CodDisciplina IS NULL;

-- 15) Mostre a soma dos salários dos professores de humanas e dos que não são de humanas
SELECT e.Humanas AS Area,
    SUM(p.Salario) AS Salario
FROM professor p
JOIN especialidade e ON p.CodEspecialidade = e.Codigo 
GROUP BY e.Humanas;

-- 16) Mostre as disciplinas que têm carga horária superior a 60 horas e que são ministradas por professores cuja a especialidade é Matemática

SELECT DISTINCT d.Nome AS Disciplina
FROM disciplina d
JOIN turma t ON d.Codigo = t.CodDisciplina
JOIN professor p ON t.CodProfessor = p.Codigo
JOIN especialidade e ON p.CodEspecialidade = e.Codigo
WHERE d.CargaHoraria > 60
AND e.Nome = 'Matemática';

-- 17) Mostre todas as disciplinas e o nome do professor que é responsável por cada disciplina. O resultado deve ser ordenado pelo nome da disciplina. Não é permitido repetições

SELECT DISTINCT d.nome AS disciplina, p.Nome AS professor
FROM disciplina d
JOIN turma t ON d.Codigo = t.CodDisciplina
JOIN professor p ON t.CodProfessor = p.Codigo
ORDER BY d.Nome;

-- 18) Faça uma view que mostre todos os professores que também já foram alunos

CREATE VIEW professores_foram_alunos AS
SELECT DISTINCT p.Nome AS Nome_Professor, p.Codigo AS CodigoProfessor
FROM professor p
JOIN aluno a ON p.Nome = a.Nome;

-- 19) Faça uma view que selecione todos os alunos que fazem as disciplinas de Inglês 1 e Inglês 2

CREATE VIEW alunos_ingles AS
SELECT a.Nome AS Aluno, 

-- 20) Crie uma view materializada dentro do contexto do DER Escola


-- 22) Faça uma procedure que retorne a carga horária de um determinado professor

CREATE OR REPLACE PROCEDURE carga_horaria_professor(IN professor_nome varchar(50))
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT SUM(CargaHoraria) FROM disciplina d
    JOIN turma t ON d.Codigo = t.CodDisciplina
    JOIN professor p ON t.CodProfessor = p.Codigo 
    WHERE p.nome = professor_nome; --group by t.cod_profesor;
END;
$$;

CALL carga_horaria_professor('kleber Fonseca');