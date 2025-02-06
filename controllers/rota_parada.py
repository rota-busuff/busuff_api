from flask import request
from flask_restx import Resource, Namespace, fields

from models.rota_parada import RotaParadaModel
from schemas.rota_parada import RotaParadaSchema

rota_parada_ns = Namespace('rota_paradas', description='Operações relacionadas a rota_paradas')

rota_parada_schema = RotaParadaSchema()
rota_parada_list_schema = RotaParadaSchema(many=True)

item = rota_parada_ns.model('RotaParada', {
    'id_rota': fields.Integer(description="id da rota"),
    'id_parada': fields.Integer(description="id da parada"),
    'ordem': fields.Integer(description="ordem da parada")
})

@rota_parada_ns.route('/<int:id>')
class RotaParada(Resource):
    def get(self, id):
        rota_parada_data = RotaParadaModel.find_by_id(id)
        if rota_parada_data:
            return rota_parada_schema.dump(rota_parada_data), 200
        
        return {'message': 'rota_parada não encontrada'}, 404
    
    @rota_parada_ns.expect(item)
    def put(self, id):
        rota_parada_data = RotaParadaModel.find_by_id(id)
        
        if not rota_parada_data:
            return {'message': 'rota_parada não encontrada'}, 404

        rota_parada_json = request.get_json()
        
        rota_parada_data.id_rota = rota_parada_json.get("id_rota", rota_parada_data.id_rota)
        rota_parada_data.id_parada = rota_parada_json.get("id_parada", rota_parada_data.id_parada)
        rota_parada_data.ordem = rota_parada_json.get("ordem", rota_parada_data.ordem)

        rota_parada_data.add_to_db()
        
        return rota_parada_schema.dump(rota_parada_data), 200
    
    def delete(self, id):
        rota_parada_data = RotaParadaModel.find_by_id(id)
        if not rota_parada_data:
            return {'message': 'rota_parada não encontrada'}, 404
        
        rota_parada_data.delete_from_db()
        return '', 204

@rota_parada_ns.route('')
class RotaParadaList(Resource):
    def get(self):
        return rota_parada_list_schema.dump(RotaParadaModel.find_all()), 200
    
    @rota_parada_ns.expect(item)
    @rota_parada_ns.doc('Criar uma relação entre rota e parada')
    def post(self):
        rota_parada_json = request.get_json()
        
        rota_parada_model = RotaParadaModel(
            id_rota=rota_parada_json['id_rota'],
            id_parada=rota_parada_json['id_parada'],
            ordem=rota_parada_json['ordem'],
        )
        
        rota_parada_model.add_to_db()
        
        return rota_parada_schema.dump(rota_parada_model), 200
