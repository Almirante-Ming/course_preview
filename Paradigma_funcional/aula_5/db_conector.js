const { Sequelize } = require('sequelize');
const db = new Sequelize('tads', 'postgres', 'masterkey', { 
    host: 'localhost',
    dialect: 'postgres'
});

module.exports = db;
