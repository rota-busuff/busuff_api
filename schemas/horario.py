from ma import ma
from models.horario import HorarioModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class HorarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = HorarioModel
        load_instance = True
        include_fk = True