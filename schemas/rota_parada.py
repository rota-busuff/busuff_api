from ma import ma
from models.rota_parada import RotaParadaModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class RotaParadaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RotaParadaModel
        load_instance = True
        include_fk = True