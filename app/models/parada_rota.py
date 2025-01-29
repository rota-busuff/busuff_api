from app import db
from .rota import Rota
from .parada import Parada

class ParadaRota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    rota_id = db.Column(db.Integer, db.ForeignKey('rota.id'), nullable=False)
    
    parada_id = db.Column(db.Integer, db.ForeignKey('parada.id'), nullable=False)
    
    ordem = db.Column(db.Integer, nullable=False)

    rota = db.relationship('Rota', backref=db.backref('paradas', lazy=True))
    
    parada = db.relationship('Parada', backref=db.backref('rotas', lazy=True))

    def __repr__(self):
        return f"<ParadaRota {self.rota_id} - {self.parada_id}>"
