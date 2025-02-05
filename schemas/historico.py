from ma import ma
from models.historico import HistoricoModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class HistoricoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = HistoricoModel
        load_instance = True