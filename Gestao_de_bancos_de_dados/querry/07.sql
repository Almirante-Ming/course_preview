--  mostre a media dos salarios dos professores por area de conhecimento

select avg(p.salario) from professor p join especialidade e on p.cod_especialidade = e.cod group by e.humanas;