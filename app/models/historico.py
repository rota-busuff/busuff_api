from app import db
from .motorista import Motorista
from .rota import Rota

class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    data_hora = db.Column(db.DateTime, nullable=False)
    
    motorista_id = db.Column(db.Integer, db.ForeignKey('motorista.id'), nullable=False)
    
    rota_id = db.Column(db.Integer, db.ForeignKey('rota.id'), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    
    latitude = db.Column(db.Float, nullable=False)
    
    longitude = db.Column(db.Float, nullable=False)

    motorista = db.relationship('Motorista', backref=db.backref('historico', lazy=True))
    
    rota = db.relationship('Rota', backref=db.backref('historico', lazy=True))

    def __repr__(self):
        return f"<Historico {self.id}>"
