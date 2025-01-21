const db = require('../db_conector'); 
const { DataTypes } = require('sequelize');

const Pessoa = db.define('pessoa', {
    nome: { 
        type: DataTypes.STRING,
        allowNull: false
    },
    idade: {
        type: DataTypes.INTEGER,
    },
    profissao: {
        type: DataTypes.STRING,
        allowNull: false
    }
});

module.exports = Pessoa;
