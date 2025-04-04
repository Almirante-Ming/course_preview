const express = require('express');
const exphbs = require('express-handlebars');
const path = require('path');

const mgs = express();
const port = 7070;


mgs.engine('handlebars', exphbs.engine());
mgs.set('view engine', 'handlebars');
mgs.set('views', path.join(__dirname, 'views'));

mgs.use(express.static(path.join(__dirname, 'public')));

mgs.get('/', (req, res) => {
  res.render('home', {layout: false});
});

mgs.get('/jogo', (req, res) => {
  res.render('game',{layout: false});
});

mgs.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
