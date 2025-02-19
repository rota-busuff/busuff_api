from flask_restx import Namespace, Resource, fields
from app.models.rota_parada import RotaParadaModel
from app.schemas.rota_parada import RotaParadaSchema
from app.extensions.db import db

rota_parada_ns = Namespace('rota_parada', description='Operações relacionadas a Rota Paradas')

rota_parada_schema = RotaParadaSchema()
rota_parada_list_schema = RotaParadaSchema(many=True)

item = rota_parada_ns.model('RotaParada', {
    'id_rota': fields.Integer(description="ID da Rota Rota"),
    'id_parada': fields.Integer(description="ID da Parada"),
    'ordem': fields.Integer(description="Ordem da Parada na Rota")
})

@rota_parada_ns.route('/')
class RotaParadaList(Resource):
    @rota_parada_ns.doc('listar_rota_paradas')
    def get(self):
        """Lista todos os Rota Paradas"""
        return rota_parada_list_schema.dump(RotaParadaModel.query.all()), 200

    @rota_parada_ns.expect(item)
    @rota_parada_ns.doc('criar_rota_parada')
    def post(self):
        """Cria um novo Rota Parada"""
        rota_parada_json = rota_parada_ns.payload
        
        rota_parada_model = RotaParadaModel(
            id_rota=rota_parada_json['id_rota'],
            id_parada=rota_parada_json['id_parada'],
            ordem=rota_parada_json['ordem']
        )
        
        db.session.add(rota_parada_model)
        db.session.commit()
        
        return rota_parada_schema.dump(rota_parada_model), 201

@rota_parada_ns.route('/<int:id>')
@rota_parada_ns.param('id', 'O identificador do Rota Parada')
class RotaParada(Resource):
    @rota_parada_ns.doc('obter_rota_parada')
    def get(self, id):
        """Obtém um Rota Parada pelo ID"""
        rota_parada_data = RotaParadaModel.query.get(id)
        if rota_parada_data:
            return rota_parada_schema.dump(rota_parada_data), 200
        
        return {'message': 'Rota Parada não encontrada'}, 404

    @rota_parada_ns.expect(item)
    @rota_parada_ns.doc('atualizar_rota_parada')
    def put(self, id):
        """Atualiza uma Rota Parada pelo ID"""
        rota_parada_data = RotaParadaModel.query.get(id)
        
        if not rota_parada_data:
            return {'message': 'Rota Parada não encontrada'}, 404

        rota_parada_json = rota_parada_ns.payload
        
        rota_parada_data.id_rota = rota_parada_json.get("id_rota", rota_parada_data.id_rota)
        rota_parada_data.id_parada = rota_parada_json.get("id_parada", rota_parada_data.id_parada)
        rota_parada_data.ordem = rota_parada_json.get("ordem", rota_parada_data.ordem)

        db.session.commit()
        
        return rota_parada_schema.dump(rota_parada_data), 200

    @rota_parada_ns.doc('deletar_rota_parada')
    def delete(self, id):
        """Deleta uma Rota Parada pelo ID"""
        rota_parada_data = RotaParadaModel.query.get(id)
        if not rota_parada_data:
            return {'message': 'Rota Parada não encontrada'}, 404
        
        db.session.delete(rota_parada_data)
        db.session.commit()
        return '', 204
