from db import db
from datetime import datetime
import pytz

class HistoricoModel(db.Model):
    __tablename__ = "historico"
    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=False, default=datetime.now())
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    rota = db.Column(db.String(10), nullable=False)
    
    def __init__(self, data, latitude, longitude, rota):
        self.data = data
        self.latitude = latitude
        self.longitude = longitude
        self.rota = rota
        
    def __repr__(self):
        return f"UsuarioModel(data={self.data}, latitude={self.latitude}, longitude={self.longitude}, rota={self.rota})"
    
    def json(self):
        return {
            'data': self.data,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'rota': self.rota
        }
        
    # Buscar por data
    @classmethod
    def find_by_data(cls, data):
        return cls.query.filter_by(data=data).first()
    
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
    