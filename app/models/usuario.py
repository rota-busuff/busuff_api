from app.extensions.db import db

class UsuarioModel(db.Model):
    __tablename__ = "usuario"
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Integer, db.ForeignKey("rota.id"), nullable=False)
    senha = db.Column(db.String(32), nullable=False)
    perfil = db.Column(db.String(20), nullable=False)
    online = db.Column(db.Integer, default=0)
    
    def json(self):
        return {
            'id': self.id,
            'login': self.login,
            'senha': self.senha,
            'perfil': self.perfil,
            'online': self.online
        }