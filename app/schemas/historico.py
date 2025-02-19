from app.extensions.ma import ma
from app.models.historico import HistoricoModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class HistoricoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = HistoricoModel
        load_instance = True
        include_fk = True