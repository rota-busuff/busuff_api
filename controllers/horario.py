from flask import request
from flask_restx import Resource, Namespace, fields

from models.horario import HorarioModel
from schemas.horario import HorarioSchema

horario_ns = Namespace('horarios', description='Operações relacionadas a horarios')

horario_schema = HorarioSchema()
horario_list_schema = HorarioSchema(many=True)

item = horario_ns.model('Horario', {
    'id_rota': fields.Integer(description="id da rota"),
    'horario': fields.String(description="horario")
})

@horario_ns.route('/<int:id>')
class Horario(Resource):
    def get(self, id):
        horario_data = HorarioModel.find_by_id(id)
        if horario_data:
            return horario_schema.dump(horario_data), 200
        
        return {'message': 'Horario não encontrado'}, 404
    
    @horario_ns.expect(item)
    def put(self, id):
        horario_data = HorarioModel.find_by_id(id)
        
        if not horario_data:
            return {'message': 'Horario não encontrado'}, 404

        horario_json = request.get_json()
        
        horario_data.id_rota = horario_json.get("id_rota", horario_data.id_rota)
        horario_data.horario = horario_json.get("horario", horario_data.horario)

        horario_data.add_to_db()
        
        return horario_schema.dump(horario_data), 200
    
    def delete(self, id):
        horario_data = HorarioModel.find_by_id(id)
        if not horario_data:
            return {'message': 'Horario não encontrada'}, 404
        
        horario_data.delete_from_db()
        return '', 204

@horario_ns.route('')
class HorarioList(Resource):
    def get(self):
        return horario_list_schema.dump(HorarioModel.find_all()), 200
    
    @horario_ns.expect(item)
    @horario_ns.doc('Criar um horario')
    def post(self):
        horario_json = request.get_json()
        
        horario_model = HorarioModel(
            id_rota=horario_json['id_rota'],
            horario=horario_json['horario']
        )
        
        horario_model.add_to_db()
        
        return horario_schema.dump(horario_model), 200
