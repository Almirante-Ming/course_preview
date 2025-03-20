-- mostre o nome e o salario dos professores que sao da especialidade de matematica

SELECT p.nome, p.salario FROM professor p join especialidade e on p.cod_especialidade = e.cod where e.nome='Matemática';