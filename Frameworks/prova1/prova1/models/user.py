from prova1.config import db

class Beneficiario(db.Model):
    __tablename__ = 'beneficiarios'
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(17), unique=True, nullable=False)
    tipo_plano = db.Column(db.String(50), nullable=False)
    data_nasc = db.Column(db.String, nullable=False)
    pagamento = db.Column(db.String(20), nullable=False)

    # Relacionamento com Dependentes
    dependentes = db.relationship('Dependente', backref='beneficiario', lazy=True)

class Dependente(db.Model):
    __tablename__ = 'dependentes'
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String, nullable=False)
    titular = db.Column(db.Integer, db.ForeignKey('beneficiarios.id'), nullable=False)
