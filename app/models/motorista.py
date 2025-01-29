from app import db
from .usuario import Usuario

class Motorista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    nome = db.Column(db.String(100), nullable=False)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    usuario = db.relationship('Usuario', backref=db.backref('motoristas', lazy=True))

    def __repr__(self):
        return f"<Motorista {self.nome}>"
