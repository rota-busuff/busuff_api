from ma import ma
from models.viagem import ViagemModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ViagemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ViagemModel
        load_instance = True