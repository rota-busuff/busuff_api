from flask import request
from flask_restx import Resource, Namespace, fields

from models.rota import RotaModel
from schemas.rota import RotaSchema

rota_ns = Namespace('rotas', description='Operações relacionadas a rotas')

rota_schema = RotaSchema()
rota_list_schema = RotaSchema(many=True)

item = rota_ns.model('Rota', {
    'nome': fields.String(description="Nome da rota")
})

@rota_ns.route('/<int:id>')
class Rota(Resource):
    def get(self, id):
        rota_data = RotaModel.find_by_id(id)
        if rota_data:
            return rota_schema.dump(rota_data), 200
        
        return {'message': 'Rota não encontrada'}, 404
    
    @rota_ns.expect(item)
    def put(self, id):
        rota_data = RotaModel.find_by_id(id)
        
        if not rota_data:
            return {'message': 'Rota não encontrada'}, 404

        rota_json = request.get_json()
        
        rota_data.nome = rota_json.get("nome", rota_data.nome)

        rota_data.add_to_db()
        
        return rota_schema.dump(rota_data), 200
    
    def delete(self, id):
        rota_data = RotaModel.find_by_id(id)
        if not rota_data:
            return {'message': 'Rota não encontrada'}, 404
        
        rota_data.delete_from_db()
        return '', 204

@rota_ns.route('')
class RotaList(Resource):
    def get(self):
        return rota_list_schema.dump(RotaModel.find_all()), 200
    
    @rota_ns.expect(item)
    @rota_ns.doc('Criar uma rota')
    def post(self):
        rota_json = request.get_json()
        
        rota_model = RotaModel(
            nome=rota_json['nome'],
        )
        
        rota_model.add_to_db()
        
        return rota_schema.dump(rota_model), 200
