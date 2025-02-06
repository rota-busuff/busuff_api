from db import db

class RotaModel(db.Model):
    __tablename__ = "rota"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(10), nullable=False)
    
    def __init__(self, nome):
        self.nome = nome
        
    def __repr__(self):
        return f"RotaModel(nome={self.nome})"
    
    def json(self):
        return {
            'nome': self.nome
        }
        
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
    