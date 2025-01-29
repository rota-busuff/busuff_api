from app import db

class Parada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    nome = db.Column(db.String(100), nullable=False)
    
    endereco = db.Column(db.String(200), nullable=False)
    
    latitude = db.Column(db.Float, nullable=False)
    
    longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Parada {self.nome}>"
