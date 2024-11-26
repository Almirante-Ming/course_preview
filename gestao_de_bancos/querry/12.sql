-- mostre o nome, sem repeticao, de todos os professores que ja deram aula de historia 1

select distinct p.nome from turma t join professor p on t.cod_professor = p.cod join disciplina d on t.cod_disciplina = d.cod where d.nome='História 1';