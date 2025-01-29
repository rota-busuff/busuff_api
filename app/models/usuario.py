from app import db

class Usuario(db.model):
    id = db.Column(db.Integer, primary_key=True)
    
    CPF = db.Column(db.String(14), unique=True, nullable=False)
    
    nome = db.Column(db.String(100), nullable=False)
    
    nomeusuario = db.Column(db.String(50), unique=True, nullable=False)
    
    senha = db.Column(db.String, nullable=False)
    
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    tipo_usuario = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f"<Usuario {self.nome}>"