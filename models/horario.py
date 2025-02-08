from db import db

class HorarioModel(db.Model):
    __tablename__ = "horario"
    
    id = db.Column(db.Integer, primary_key=True)
    id_rota = db.Column(db.Integer, db.ForeignKey("rota.id"), nullable=False)
    horario = db.Column(db.String(5), nullable=False)
    
    def __init__(self, id_rota, horario):
        self.id_rota = id_rota
        self.horario = horario
        
    def __repr__(self):
        return f"HorarioModel(id_rota={self.id_rota}, horario={self.horario})"
    
    def json(self):
        return {
            'id_rota': self.id_rota,
            'horario': self.horario
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
    