from ma import ma
from models.usuario import UsuarioModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UsuarioModel
        load_instance = True
        include_fk = True