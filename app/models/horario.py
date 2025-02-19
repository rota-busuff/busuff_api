from app.extensions.db import db

class HorarioModel(db.Model):
    __tablename__ = "horario"
    
    id = db.Column(db.Integer, primary_key=True)
    id_rota = db.Column(db.Integer, db.ForeignKey("rota.id"), nullable=False)
    horario = db.Column(db.String(5), nullable=False)
    
    def json(self):
        return {
            'id_rota': self.id_rota,
            'horario': self.horario
        }