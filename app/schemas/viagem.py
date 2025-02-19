from app.extensions.ma import ma
from app.models.viagem import ViagemModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ViagemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ViagemModel
        load_instance = True
        include_fk = True