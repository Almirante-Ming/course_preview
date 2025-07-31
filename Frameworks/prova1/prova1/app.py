from flask import Flask, render_template, request
from prova1.config import db, migrate


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)


@app.route('/', methods=['GET'])
def root():    
    return render_template('index.html')