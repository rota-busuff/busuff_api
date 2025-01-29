from app import db
from .rota import Rota

class Itinerario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    rota_id = db.Column(db.Integer, db.ForeignKey('rota.id'), nullable=False)
    
    horario_de_partida = db.Column(db.Time, nullable=False)

    rota = db.relationship('Rota', backref=db.backref('itinerarios', lazy=True))

    def __repr__(self):
        return f"<Itinerario {self.id}>"
