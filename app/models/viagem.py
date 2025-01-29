from app import db
from .motorista import Motorista
from .rota import Rota

class Viagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    motorista_id = db.Column(db.Integer, db.ForeignKey('motorista.id'), nullable=False)
    
    rota_id = db.Column(db.Integer, db.ForeignKey('rota.id'), nullable=False)
    
    data_inicio = db.Column(db.DateTime, nullable=False)
    
    data_fim = db.Column(db.DateTime, nullable=True)
    
    mensagem_status = db.Column(db.String(200), nullable=True)

    motorista = db.relationship('Motorista', backref=db.backref('viagens', lazy=True))
    
    rota = db.relationship('Rota', backref=db.backref('viagens', lazy=True))

    def __repr__(self):
        return f"<Viagem {self.id}>"
