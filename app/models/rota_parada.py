from app.extensions.db import db

class RotaParadaModel(db.Model):
    __tablename__ = "rota_parada"

    id = db.Column(db.Integer, primary_key=True)
    id_rota = db.Column(db.Integer, db.ForeignKey("rota.id"))
    id_parada = db.Column(db.Integer, db.ForeignKey("parada.id"))
    ordem = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id_rota': self.id_rota,
            'id_parada': self.id_parada,
            'ordem': self.ordem,
        }