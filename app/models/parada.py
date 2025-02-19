from app.extensions.db import db

class ParadaModel(db.Model):
    __tablename__ = "parada"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False, unique=True)
    latitude = db.Column(db.Float, nullable=False) 
    longitude = db.Column(db.Float, nullable=False)
    
    def json(self):
        return {
            'nome': self.nome,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }