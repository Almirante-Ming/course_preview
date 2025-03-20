const express = require('express');
const path = require('path');
const app = express();
const port = 3101;
const cors = require('cors');

const db = require('./db_conector');
const Pessoa = require('./models/pessoa');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

db.authenticate()
    .then(() => {
        console.log('Conexão com PostgreSQL estabelecida');
        return db.sync();
    })
    .catch(err => {
        console.log(`Não foi possível se conectar ao banco: ${err}`);
    });


app.get('/', (req, res) => {
    res.render('index');
});

app.get('/api/dados', (req, res) => {
    Pessoa.findAll()
        .then(pessoas => {
            res.send(pessoas);
        })
        .catch(err => {
            res.status(500).send(`Erro ao buscar pessoas: ${err.message}`);
        });
})

app.post('/api/cad', async (req, res) => {
    const dados = req.body;

    if (!dados.nome || !dados.idade || !dados.profissao) {
        return res.status(400).send('Todos os campos são obrigatórios: nome, idade e profissão');
    }

    try {
        await Pessoa.create({
            nome: dados.nome,
            idade: dados.idade,
            profissao: dados.profissao
        });

        res.status(201).send('Pessoa cadastrada com sucesso');
    } catch (err) {
        res.status(500).send(`Houve um erro durante a criação: ${err}`);
    }
});

app.listen(port, () => {
    console.log(`Servidor iniciado na porta ${port}`);
});
