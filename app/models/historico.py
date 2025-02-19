from app.extensions.db import db
from datetime import datetime
import pytz

class HistoricoModel(db.Model):
    __tablename__ = "historico"
    
    id = db.Column(db.Integer, primary_key=True)
    id_rota = db.Column(db.Integer, db.ForeignKey("rota.id"), nullable=False)
    data_registro = db.Column(db.DateTime, nullable=False, default=datetime.now())
    posicao = db.Column(db.Integer, db.ForeignKey("parada.id"), nullable=False)
    mensagem = db.Column(db.String(15))
    
    def json(self):
        return {
            'id_rota': self.id_rota,
            'data_registro': self.data_registro,
            'posicao': self.posicao,
            'mensagem': self.mensagem
        }