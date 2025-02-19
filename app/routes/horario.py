from flask_restx import Namespace, Resource, fields
from app.models.horario import HorarioModel
from app.schemas.horario import HorarioSchema
from app.extensions.db import db

horario_ns = Namespace('horario', description='Operações relacionadas a horários')

horario_schema = HorarioSchema()
horario_list_schema = HorarioSchema(many=True)

item = horario_ns.model('Horario', {
    'id_rota': fields.Integer(description="Nome de horário"),
    'horario': fields.String(description="Senha do horário")
})

@horario_ns.route('/')
class HorarioList(Resource):
    @horario_ns.doc('listar_horarios')
    def get(self):
        """Lista todos os horários"""
        return horario_list_schema.dump(HorarioModel.query.all()), 200

    @horario_ns.expect(item)
    @horario_ns.doc('criar_horario')
    def post(self):
        """Cria um novo horário"""
        horario_json = horario_ns.payload
        
        horario_model = HorarioModel(
            id_rota=horario_json['id_rota'],
            horario=horario_json['horario']
        )
        
        db.session.add(horario_model)
        db.session.commit()
        
        return horario_schema.dump(horario_model), 201

@horario_ns.route('/<int:id>')
@horario_ns.param('id', 'O identificador do horário')
class Horario(Resource):
    @horario_ns.doc('obter_horario')
    def get(self, id):
        """Obtém um horário pelo ID"""
        horario_data = HorarioModel.query.get(id)
        if horario_data:
            return horario_schema.dump(horario_data), 200
        
        return {'message': 'Horário não encontrado'}, 404

    @horario_ns.expect(item)
    @horario_ns.doc('atualizar_horario')
    def put(self, id):
        """Atualiza um horário pelo ID"""
        horario_data = HorarioModel.query.get(id)
        
        if not horario_data:
            return {'message': 'Horário não encontrado'}, 404

        horario_json = horario_ns.payload
        
        horario_data.id_rota = horario_json.get("id_rota", horario_data.id_rota)
        horario_data.horario = horario_json.get("horario", horario_data.horario)

        db.session.commit()
        
        return horario_schema.dump(horario_data), 200

    @horario_ns.doc('deletar_horario')
    def delete(self, id):
        """Deleta um horário pelo ID"""
        horario_data = HorarioModel.query.get(id)
        if not horario_data:
            return {'message': 'Horário não encontrado'}, 404
        
        db.session.delete(horario_data)
        db.session.commit()
        return '', 204
