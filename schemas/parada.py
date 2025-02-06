from ma import ma
from models.parada import ParadaModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ParadaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ParadaModel
        load_instance = True