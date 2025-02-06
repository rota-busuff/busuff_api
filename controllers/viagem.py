from flask import request
from flask_restx import Resource, Namespace, fields

from models.viagem import ViagemModel
from schemas.viagem import ViagemSchema

viagem_ns = Namespace('viagens', description='Operações relacionadas a viagens')

viagem_schema = ViagemSchema()
viagem_list_schema = ViagemSchema(many=True)

item = viagem_ns.model('Viagem', {
    'id_rota': fields.Integer(description="id da rota"),
    'data_inicio': fields.DateTime(description="data do inicio da viagem"),
    'data_fim': fields.DateTime(description="data do fim da viagem")
})

@viagem_ns.route('/<int:id>')
class Viagem(Resource):
    def get(self, id):
        viagem_data = ViagemModel.find_by_id(id)
        if viagem_data:
            return viagem_schema.dump(viagem_data), 200
        
        return {'message': 'Viagem não encontrada'}, 404
    
    @viagem_ns.expect(item)
    def put(self, id):
        viagem_data = ViagemModel.find_by_id(id)
        
        if not viagem_data:
            return {'message': 'Viagem não encontrada'}, 404

        viagem_json = request.get_json()
        
        viagem_data.id_rota = viagem_json.get("id_rota", viagem_data.id_rota)
        viagem_data.data_inicio = viagem_json.get("data_inicio", viagem_data.data_inicio)
        viagem_data.data_fim = viagem_json.get("data_fim", viagem_data.data_fim)

        viagem_data.add_to_db()
        
        return viagem_schema.dump(viagem_data), 200
    
    def delete(self, id):
        viagem_data = ViagemModel.find_by_id(id)
        if not viagem_data:
            return {'message': 'Viagem não encontrada'}, 404
        
        viagem_data.delete_from_db()
        return '', 204

@viagem_ns.route('')
class ViagemList(Resource):
    def get(self):
        return viagem_list_schema.dump(ViagemModel.find_all()), 200
    
    @viagem_ns.expect(item)
    @viagem_ns.doc('Criar uma viagem')
    def post(self):
        viagem_json = request.get_json()
        
        viagem_model = ViagemModel(
            id_rota=viagem_json['id_rota'],
            data_inicio=viagem_json['data_inicio'],
            data_fim=viagem_json['data_fim'],
        )
        
        viagem_model.add_to_db()
        
        return viagem_schema.dump(viagem_model), 200
