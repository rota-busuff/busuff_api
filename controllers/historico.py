from flask import request
from flask_restx import Resource, Namespace, fields

from models.historico import HistoricoModel 
from schemas.historico import HistoricoSchema

historico_ns = Namespace('historico', description='Operações relacionadas ao histórico')

historico_schema = HistoricoSchema()
historico_list_schema = HistoricoSchema(many=True)

item = historico_ns.model('Historico', {
    'data': fields.DateTime(description="Data e hora do registro"),
    'latitude': fields.Float(description="Latitude da localização"),
    'longitude': fields.Float(description="Longitude da localização"),
    'rota': fields.String(description="Rota identificadora"),
})


historico_ns.route('/<int:id>')
class Historico(Resource):
    def get(self, id):
        historico_data = HistoricoModel.find_by_id(id)
        if historico_data:
            return historico_schema.dump(historico_data), 200
        
        return {'message': 'Histórico não encontrado'}, 404
    
    @historico_ns.expect(item)
    def put(self, id):
        historico_data = HistoricoModel.find_by_id(id)
        
        if not historico_data:
            return {'message': 'Histórico não encontrado'}, 404

        historico_json = request.get_json()
        
        historico_data.data = historico_json.get("data", historico_data.data)
        historico_data.latitude = historico_json.get("latitude", historico_data.latitude)
        historico_data.longitude = historico_json.get("longitude", historico_data.longitude)
        historico_data.rota = historico_json.get("rota", historico_data.rota)

        historico_data.add_to_db()
        
        return historico_schema.dump(historico_data), 200
    
    def delete(self, id):
        historico_data = HistoricoModel.find_by_id(id)
        if not historico_data:
            return {'message': 'Histórico não encontrado'}, 404
        
        historico_data.delete_from_db()
        return '', 204

@historico_ns.route('')
class HistoricoList(Resource):
    def get(self):
        return historico_list_schema.dump(HistoricoModel.find_all()), 200
    
    @historico_ns.expect(item)
    @historico_ns.doc('Criar um histórico')
    def post(self):
        historico_json = request.get_json()
        
        historico_model = HistoricoModel(
            data=historico_json['data'],
            latitude=historico_json['latitude'],
            longitude=historico_json['longitude'],
            rota=historico_json['rota']
        )
        
        historico_model.add_to_db()
        
        return historico_schema.dump(historico_model), 200
