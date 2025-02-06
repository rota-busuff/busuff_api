from db import db

class ParadaModel(db.Model):
    __tablename__ = "parada"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False, unique=True)
    latitude = db.Column(db.Float, nullable=False) 
    longitude = db.Column(db.Float, nullable=False)

    
    def __init__(self, nome, latitude, longitude):
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        
    def __repr__(self):
        return f"ParadaModel(nome={self.nome}, latitude={self.latitude}, longitude={self.longitude})"
    
    def json(self):
        return {
            'nome': self.nome,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }
        
    # Buscar por nome
    @classmethod
    def find_by_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()
    
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
    