from app.extensions.db import db

class ViagemModel(db.Model):
    __tablename__ = "viagem"

    id = db.Column(db.Integer, primary_key=True)
    id_rota = db.Column(db.Integer, db.ForeignKey("rota.id"), nullable=False)
    data_inicio = db.Column(db.DateTime, nullable=False)
    data_fim = db.Column(db.DateTime)
    
    def json(self):
        return {
            'id_rota': self.id_rota,
            'data_inicio': self.data_inicio,
            'data_fim': self.data_fim,
        }