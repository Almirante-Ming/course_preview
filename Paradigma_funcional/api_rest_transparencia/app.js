const express = require('express');
const port = 3101
const app = express();

app.get('/api/cpf/:cpf', async (req, res) => {

    const { cpf } = req.params;
    const apiUrl = `http://3.85.29.215:3000/api/cpf/${cpf}`;
    
    try {
        const response = await fetch(apiUrl, { method: 'GET' });

        if (!response.ok) {
            return res.status(response.status).json({
                error: `Erro na API externa: ${response.statusText}`,
            });
        }

        const data = await response.json();
        return res.status(200).json(data);
    } catch (error) {
        console.error('Erro ao buscar dados:', error.message);
        return res.status(500).json({ error: 'Erro interno do servidor' });
    }

});

app.get('/itens', async (req, res) => {
    const api_url = `http://3.85.29.215:3000/itens`

    try {
        const data = await fetch(api_url, {method: 'GET'});

        if (!data.ok) {
            return res.status(data.status).json({
                error: `Erro na api externa: ${data.mensage}`,
            })
        }
    } catch (error)
});

app.listen(port, ()=>{
    console.log(`servidor iniciado na porta ${port}`)
})