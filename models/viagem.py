from db import db

class ViagemModel(db.Model):
    __tablename__ = "viagem"

    id = db.Column(db.Integer, primary_key=True)
    id_rota = db.Column(db.Integer, db.ForeignKey("rota.id"), nullable=False)
    data_inicio = db.Column(db.DateTime, nullable=False)
    data_fim = db.Column(db.DateTime)

    rota = db.relationship("RotaModel")

    
    def __init__(self, id_rota, data_inicio, data_fim):
        self.id_rota = id_rota
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        
    def __repr__(self):
        return f"ViagemModel(id_rota={self.id_rota}, data_inicio={self.data_inicio}, data_fim={self.data_fim})"
    
    def json(self):
        return {
            'id_rota': self.id_rota,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
        }
        
    # Buscar por id_rota
    @classmethod
    def find_by_id_rota(cls, id_rota):
        return cls.query.filter_by(id_rota=id_rota).first()
    
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
    