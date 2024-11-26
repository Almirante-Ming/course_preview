-- mostre o nome dos professores que ministram aula de matematica

select distinct p.nome from turma t join professor p on t.cod_professor = p.cod join disciplina d on t.cod_disciplina =d.cod where d.nome like'%Matemática%'; 