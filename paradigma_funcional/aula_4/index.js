//Criar um arquivo arquivo.js numa pasta. Instalar no local da pasta o packge.json com npm init -y

//Instalar o servidor Express no local da pasta, npm install express.

//criar a API simples, primeiro importa a biblioteca do express, depois define um variavel app de express, e por ultimo definir a porta.

const express = require('express');
const app = express();
const port = 3101;


app.get('/api/cpf/:cpf', async (req, res) =>{
  const {cpf} = req.params;
  const api_url = `https://api.portaldatransparencia.gov.br/pessoa-fisica?cpf=${cpf}`;

  try {
    const response = await fetch(api_url, {
      method: 'GET'
    });
  

    if (!response.ok) {
      return res.status(response.status).json({
        error: `Erro na Api Externa: ${express.response.statusText}`,});
    }

    const data =await response.json();
    return res.status(200).json(data);
  } catch(error) {
    console.error('erro ao buscar dados: ', error.mensage);
    return res.status(500).json({error: 'erro interno do servidor'});
  }
});

app.listen(port, () => {console.log('Servidor OK');});