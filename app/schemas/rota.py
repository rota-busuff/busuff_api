from app.extensions.ma import ma
from app.models.rota import RotaModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class RotaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RotaModel
        load_instance = True
        include_fk = True