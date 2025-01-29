from app import db

class Rota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    nome = db.Column(db.String(100), nullable=False)
    
    inicio_end = db.Column(db.String(200), nullable=False)
    
    destino_end = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<Rota {self.nome}>"
