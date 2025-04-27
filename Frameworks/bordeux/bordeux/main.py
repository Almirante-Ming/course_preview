from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pessoas.db"
app.config["SECRETS_KEY"] = "senha"
db = SQLAlchemy(app)

class Endereco (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cep = db.Column(db.String(100), nullable = False)
    bairro = db.Column(db.String(100), nullable = False)
    logradouro = db.Column(db.String(150), nullable = False)
    numero = db.Column(db.String(100), nullable = False)
    complemento = db.Column(db.String(100), nullable = False)

    pessoas = db.relationship('Pessoa', backref=db.backref('endereco'))

class Pessoa (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), nullable = False)
    sobrenome = db.Column(db.String(150), nullable = False)
    cpf = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    telefone = db.Column(db.String(100), nullable = False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('endereco.id'), nullable=False)

with app.app_context():
    db.create_all()

# para fazer, session & commit
