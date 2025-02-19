from app.extensions.ma import ma
from app.models.parada import ParadaModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class ParadaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ParadaModel
        load_instance = True
        include_fk = True