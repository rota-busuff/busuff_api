from db import db

class RotaParadaModel(db.Model):
    __tablename__ = "rota_parada"

    id_rota = db.Column(db.Integer, db.ForeignKey("rota.id"), primary_key=True)
    id_parada = db.Column(db.Integer, db.ForeignKey("parada.id"), primary_key=True)
    ordem = db.Column(db.Integer, nullable=False)
    
    def __init__(self, id_rota, id_parada, ordem):
        self.id_rota = id_rota
        self.id_parada = id_parada
        self.ordem = ordem
        
    def __repr__(self):
        return f"RotaParadaModel(id_rota={self.id_rota}, id_parada={self.id_parada}, ordem={self.ordem})"
    
    def json(self):
        return {
            'id_rota': self.id_rota,
            'id_parada': self.id_parada,
            'ordem': self.ordem,
        }
        
    # Buscar por id_rota
    @classmethod
    def find_by_id_rota(cls, id_rota):
        return cls.query.filter_by(id_rota=id_rota).first()
    
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
    