from flask import request
from flask_restx import Resource, Namespace, fields

from models.parada import ParadaModel
from schemas.parada import ParadaSchema

parada_ns = Namespace('paradas', description='Operações relacionadas a usuários')

parada_schema = ParadaSchema()
parada_list_schema = ParadaSchema(many=True)

item = parada_ns.model('Parada', {
    'nome': fields.String(description="nome da parada"),
    'latitude': fields.Float(description="latitude da parada"),
    'longitude': fields.Float(description="longitude da parada")
})

@parada_ns.route('/<int:id>')
class Parada(Resource):
    def get(self, id):
        parada_data = ParadaModel.find_by_id(id)
        if parada_data:
            return parada_schema.dump(parada_data), 200
        
        return {'message': 'Parada não encontrada'}, 404
    
    @parada_ns.expect(item)
    def put(self, id):
        parada_data = ParadaModel.find_by_id(id)
        
        if not parada_data:
            return {'message': 'Parada não encontrada'}, 404

        parada_json = request.get_json()
        
        parada_data.nome = parada_json.get("nome", parada_data.nome)
        parada_data.latitude = parada_json.get("latitude", parada_data.latitude)
        parada_data.longitude = parada_json.get("longitude", parada_data.longitude)

        parada_data.add_to_db()
        
        return parada_schema.dump(parada_data), 200
    
    def delete(self, id):
        parada_data = ParadaModel.find_by_id(id)
        if not parada_data:
            return {'message': 'Parada não encontrada'}, 404
        
        parada_data.delete_from_db()
        return '', 204

@parada_ns.route('')
class ParadaList(Resource):
    def get(self):
        return parada_list_schema.dump(ParadaModel.find_all()), 200
    
    @parada_ns.expect(item)
    @parada_ns.doc('Criar uma parada')
    def post(self):
        parada_json = request.get_json()
        
        parada_model = ParadaModel(
            nome=parada_json['nome'],
            latitude=parada_json['latitude'],
            longitude=parada_json['longitude'],
        )
        
        parada_model.add_to_db()
        
        return parada_schema.dump(parada_model), 200
