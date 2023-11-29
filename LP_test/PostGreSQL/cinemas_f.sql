DROP TABLE IF EXISTS Enderecos CASCADE;
DROP TABLE IF EXISTS Complexos CASCADE;
DROP TABLE IF EXISTS Exibidores CASCADE;
DROP TABLE IF EXISTS Salas CASCADE;
DROP TABLE IF EXISTS cinemas;
CREATE TABLE IF NOT EXISTS public.cinemas(
	nome_sala character varying(150) NOT NULL,
	registro_sala character varying(7) NOT NULL,
	cnpj_sala character varying(180) NOT NULL,
	situacao_sala character varying(23) NOT NULL,
	assento_sala smallint NOT NULL,
	assento_cadeirantes smallint NOT NULL, 
	assentos_mobilidade_reduzida smallint NOT NULL,
	assentos_obesidade smallint NOT NULL,
	acesso_acentos_com_rampa character varying(30) NOT NULL,
	acesso_sala_com_rampa character varying(30) NOT NULL,
	banheiros_acessiveis character varying(30) NOT NULL,
	nome_complexo character varying(150) NOT NULL,
	registro_completo character varying(70) NOT NULL,
	situacao_complexo character varying(100) NOT NULL,
	pagina_eletronica_complexo character varying(120) NOT NULL,
	endereco_complexo character varying(120) NOT NULL,
	numero_endereco_complexo character varying(60) NOT NULL,
	complemento_complexo character varying(160) NOT NULL,
	bairro_complexo character varying(120) NOT NULL,
	municipio_complexo character varying(50) NOT NULL,
	cep_complexo character varying(150) NOT NULL,
	uf_complexo character varying(100) NOT NULL,
	complexo_itinerante character varying(30) NOT NULL,
	operacao_usual character varying(70) NOT NULL,
	nome_exibidor character varying(150) NOT NULL,
	registro_exibidor character varying(100) NOT NULL,
	cnpj_exibidor character varying(50) NOT NULL,
	situacao_exibidor character varying(90) NOT NULL,
	nome_grupo_exibidor character varying(150) NOT NULL
);

COPY cinemas FROM '/home/amanda/Documentos/cinemas.csv' DELIMITER ',' CSV HEADER;

DROP FUNCTION IF EXISTS f_alterTipoRegistroSala();
DROP FUNCTION IF EXISTS f_chavePrimaria();
DROP FUNCTION IF EXISTS criar_tabelas_normalizadas();
DROP FUNCTION IF EXISTS inserir_dados_normalizados();
DROP FUNCTION IF EXISTS criar_visao_denormalizada();
DROP FUNCTION IF EXISTS cinemas_stored_procedure();

-- Criação da função para alterar o tipo do campo
CREATE OR REPLACE FUNCTION f_alterTipoRegistroSala()
RETURNS VOID
AS 
$$ 
BEGIN
    -- Alteração do tipo do campo para integer
    EXECUTE 'ALTER TABLE cinemas ALTER COLUMN registro_sala TYPE integer USING registro_sala::integer';
END;
$$
LANGUAGE plpgsql;

SELECT f_alterTipoRegistroSala();


-- Criação da função para alterar os numeros 0 existentes na tabela registro_sala
CREATE OR REPLACE FUNCTION f_chavePrimaria()
RETURNS VOID AS 
$$
DECLARE
    contador INTEGER := 4999968;
    reg_sala_atual INTEGER;
BEGIN
    -- Obtendo e atualizando cada registro_sala = 0 individualmente
    FOR reg_sala_atual IN SELECT registro_sala FROM cinemas WHERE registro_sala = 0 ORDER BY registro_sala
    LOOP
        -- Atualizando o primeiro registro encontrado com registro_sala = 0
        UPDATE cinemas SET registro_sala = contador WHERE registro_sala = reg_sala_atual AND registro_sala = 0
        AND ctid = (SELECT ctid FROM cinemas WHERE registro_sala = reg_sala_atual AND registro_sala = 0 LIMIT 1);
        
        contador := contador + 1;
    END LOOP;
END;
$$
LANGUAGE plpgsql;

SELECT f_chavePrimaria();


-- Criação da função para criar as tabelas normalizadas
CREATE OR REPLACE FUNCTION criar_tabelas_normalizadas() RETURNS void AS $$
BEGIN
    -- Criar tabela Enderecos
    CREATE TABLE IF NOT EXISTS Enderecos (
        endereco_id SERIAL PRIMARY KEY,
        endereco_complexo VARCHAR(120),
        numero_endereco_complexo VARCHAR(60),
        complemento_complexo VARCHAR(160),
        bairro_complexo VARCHAR(120),
        municipio_complexo VARCHAR(50),
        cep_complexo VARCHAR(150),
        uf_complexo VARCHAR(100)
    );

    -- Criar tabela Complexos
    CREATE TABLE IF NOT EXISTS Complexos (
        complexo_id SERIAL PRIMARY KEY,
        nome_complexo VARCHAR(150),
        registro_completo VARCHAR(70),
        situacao_complexo VARCHAR(100),
        pagina_eletronica_complexo VARCHAR(120),
        endereco_id INT REFERENCES Enderecos(endereco_id),
        complexo_itinerante VARCHAR(30),
        operacao_usual VARCHAR(70)
    );

    -- Criar tabela Exibidores
    CREATE TABLE IF NOT EXISTS Exibidores (
        exibidor_id SERIAL PRIMARY KEY,
        nome_exibidor VARCHAR(150),
        registro_exibidor VARCHAR(100),
        cnpj_exibidor VARCHAR(50),
        situacao_exibidor VARCHAR(90),
        nome_grupo_exibidor VARCHAR(150)
    );

    -- Criar tabela Salas
    CREATE TABLE IF NOT EXISTS Salas (
        registro_sala INTEGER PRIMARY KEY,
        nome_sala VARCHAR(150),
        cnpj_sala VARCHAR(180),
        situacao_sala VARCHAR(23),
        assento_sala SMALLINT,
        assento_cadeirantes SMALLINT,
        assentos_mobilidade_reduzida SMALLINT,
        assentos_obesidade SMALLINT,
        acesso_acentos_com_rampa VARCHAR(30),
        acesso_sala_com_rampa VARCHAR(30),
        banheiros_acessiveis VARCHAR(30),
        complexo_id INT REFERENCES Complexos(complexo_id)
    );
END;
$$ LANGUAGE plpgsql;

SELECT criar_tabelas_normalizadas();


-- Criar função para passar os dados da tabela public.cinemas para as tabelas normalizadas
CREATE OR REPLACE FUNCTION inserir_dados_normalizados() RETURNS void AS $$
BEGIN
    -- Inserir dados em Enderecos
    INSERT INTO Enderecos (endereco_complexo, numero_endereco_complexo, complemento_complexo, bairro_complexo, municipio_complexo, cep_complexo, uf_complexo)
    SELECT DISTINCT endereco_complexo, numero_endereco_complexo, complemento_complexo, bairro_complexo, municipio_complexo, cep_complexo, uf_complexo
    FROM public.cinemas;

    -- Inserir dados em Complexos
    INSERT INTO Complexos (nome_complexo, registro_completo, situacao_complexo, pagina_eletronica_complexo, endereco_id, complexo_itinerante, operacao_usual)
    SELECT DISTINCT nome_complexo, registro_completo, situacao_complexo, pagina_eletronica_complexo, 
           (SELECT endereco_id FROM Enderecos 
            WHERE Enderecos.endereco_complexo = cinemas.endereco_complexo 
            AND Enderecos.numero_endereco_complexo = cinemas.numero_endereco_complexo
            AND Enderecos.complemento_complexo = cinemas.complemento_complexo
            AND Enderecos.bairro_complexo = cinemas.bairro_complexo
            AND Enderecos.municipio_complexo = cinemas.municipio_complexo
            AND Enderecos.cep_complexo = cinemas.cep_complexo
            AND Enderecos.uf_complexo = cinemas.uf_complexo), 
           complexo_itinerante, operacao_usual
    FROM public.cinemas;

    -- Inserir dados em Exibidores
    INSERT INTO Exibidores (nome_exibidor, registro_exibidor, cnpj_exibidor, situacao_exibidor, nome_grupo_exibidor)
    SELECT DISTINCT nome_exibidor, registro_exibidor, cnpj_exibidor, situacao_exibidor, nome_grupo_exibidor
    FROM public.cinemas;

    -- Inserir dados em Salas
    INSERT INTO Salas (registro_sala, nome_sala, cnpj_sala, situacao_sala, assento_sala, assento_cadeirantes, assentos_mobilidade_reduzida, assentos_obesidade, acesso_acentos_com_rampa, acesso_sala_com_rampa, banheiros_acessiveis, complexo_id)
    SELECT registro_sala, nome_sala, cnpj_sala, situacao_sala, assento_sala, assento_cadeirantes, assentos_mobilidade_reduzida, assentos_obesidade, acesso_acentos_com_rampa, acesso_sala_com_rampa, banheiros_acessiveis,
           (SELECT complexo_id FROM Complexos 
 	    WHERE Complexos.nome_complexo = cinemas.nome_complexo 
 	    AND Complexos.registro_completo = cinemas.registro_completo
	    LIMIT 1)
    FROM public.cinemas;

END;
$$ LANGUAGE plpgsql;

SELECT inserir_dados_normalizados();


-- Criação da visão denormalizada
CREATE OR REPLACE FUNCTION criar_visao_denormalizada() RETURNS void AS $$
BEGIN
    EXECUTE 'DROP VIEW IF EXISTS visao_denormalizada';
    EXECUTE 'CREATE VIEW visao_denormalizada AS
             SELECT 
                 s.registro_sala,
                 s.nome_sala,
                 s.cnpj_sala,
                 s.situacao_sala,
                 s.assento_sala,
                 s.assento_cadeirantes,
                 s.assentos_mobilidade_reduzida,
                 s.assentos_obesidade,
                 s.acesso_acentos_com_rampa,
                 s.acesso_sala_com_rampa,
                 s.banheiros_acessiveis,
                 c.nome_complexo,
                 c.registro_completo,
                 c.situacao_complexo,
                 c.pagina_eletronica_complexo,
                 c.complexo_itinerante,
                 c.operacao_usual,
                 e.endereco_complexo,
                 e.numero_endereco_complexo,
                 e.complemento_complexo,
                 e.bairro_complexo,
                 e.municipio_complexo,
                 e.cep_complexo,
                 e.uf_complexo
             FROM 
                 Salas s
             JOIN 
                 Complexos c ON s.complexo_id = c.complexo_id
             JOIN 
                 Enderecos e ON c.endereco_id = e.endereco_id';
END;
$$ LANGUAGE plpgsql;

SELECT criar_visao_denormalizada();


-- FUNÇÃO STORED PROCEDURE
CREATE OR REPLACE FUNCTION cinemas_stored_procedure()
RETURNS TABLE(
    registro_sala INTEGER,
    nome_sala VARCHAR(150),
    cnpj_sala VARCHAR(180),
    situacao_sala VARCHAR(23),
    assento_sala SMALLINT,
    assento_cadeirantes SMALLINT,
    assentos_mobilidade_reduzida SMALLINT,
    assentos_obesidade SMALLINT,
    acesso_acentos_com_rampa VARCHAR(30),
    acesso_sala_com_rampa VARCHAR(30),
    banheiros_acessiveis VARCHAR(30),
    nome_complexo VARCHAR(150),
    registro_completo VARCHAR(70),
    situacao_complexo VARCHAR(100),
    pagina_eletronica_complexo VARCHAR(120),
    complexo_itinerante VARCHAR(30),
    operacao_usual VARCHAR(70),
    endereco_complexo VARCHAR(120),
    numero_endereco_complexo VARCHAR(60),
    complemento_complexo VARCHAR(160),
    bairro_complexo VARCHAR(120),
    municipio_complexo VARCHAR(50),
    cep_complexo VARCHAR(150),
    uf_complexo VARCHAR(100)
) AS $$
BEGIN

    -- Retornar os dados da visão denormalizada
    RETURN QUERY SELECT * FROM visao_denormalizada;
END;
$$ LANGUAGE plpgsql;

SELECT cinemas_stored_procedure();
