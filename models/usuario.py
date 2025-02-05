# from db import db
from db import db

class UsuarioModel(db.Model):
    __tablename__ = "usuario"
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), nullable=False, unique=True)
    senha = db.Column(db.String(32), nullable=False)
    perfil = db.Column(db.String(20), nullable=False)
    online = db.Column(db.Integer)
    
    def __init__(self, login, senha, perfil, online):
        self.login = login
        self.senha = senha
        self.perfil = perfil
        self.online = online
        
    def __repr__(self):
        return f"UsuarioModel(login={self.login}, senha={self.senha}, perfil={self.perfil}, online={self.online})"
    
    def json(self):
        return {
            'login': self.login,
            'senha': self.senha,
            'perfil': self.perfil,
            'online': self.online
        }
        
    # Buscar por login
    @classmethod
    def find_by_login(cls, login):
        return cls.query.filter_by(login=login).first()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def add_to_db(self):
        db.session.add(self)
        print("adicionando", self)
        db.session.commit()
        print("commitando", self)
        
    def delete_from_db(self):
        db.session.delete(self)
        print("deletando", self)
        db.session.commit()
        print("commitando", self)
    