from flask_sqlalchemy import Column, Integer, String, ForeignKey

from bordeux.utils.database import db


class User(db.Model):

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50), nullable=False)
    surname = db.Column(String(50), nullable=False)
    cpf = db.Column(String(11), unique=True, nullable=False)
    email = db.Column(String(50), unique=True, nullable=False)
    phone = db.Column(String(15), nullable=False)
    address = db.Column(db.Integer, db.ForeignKey('addres.id'), nullable=False)
    
    address = db.relationship('Address', backref='user', lazy=True)
    
    
