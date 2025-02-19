from app.extensions.db import db

class RotaModel(db.Model):
    __tablename__ = "rota"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(10), nullable=False)
    
    def json(self):
        return {
            'id': self.id,
            'nome': self.nome
        }