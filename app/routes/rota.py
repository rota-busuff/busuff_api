from flask_restx import Namespace, Resource, fields
from app.models.rota import RotaModel
from app.schemas.rota import RotaSchema
from app.extensions.db import db

rota_ns = Namespace('rota', description='Operações relacionadas a rotas')

rota_schema = RotaSchema()
rota_list_schema = RotaSchema(many=True)

item = rota_ns.model('Rota', {
    'nome': fields.String(description="Nome da rota"),
})

@rota_ns.route('/')
class RotaList(Resource):
    @rota_ns.doc('listar_rotas')
    def get(self):
        """Lista todos os rotas"""
        return rota_list_schema.dump(RotaModel.query.all()), 200

    @rota_ns.expect(item)
    @rota_ns.doc('criar_rota')
    def post(self):
        """Cria um novo rota"""
        rota_json = rota_ns.payload
        
        rota_model = RotaModel(
            nome=rota_json['nome']
        )
        
        db.session.add(rota_model)
        db.session.commit()
        
        return rota_schema.dump(rota_model), 201

@rota_ns.route('/<int:id>')
@rota_ns.param('id', 'O identificador da rota')
class Rota(Resource):
    @rota_ns.doc('obter_rota')
    def get(self, id):
        """Obtém um rota pelo ID"""
        rota_data = RotaModel.query.get(id)
        if rota_data:
            return rota_schema.dump(rota_data), 200
        
        return {'message': 'Rota não encontrada'}, 404

    @rota_ns.expect(item)
    @rota_ns.doc('atualizar_rota')
    def put(self, id):
        """Atualiza um rota pelo ID"""
        rota_data = RotaModel.query.get(id)
        
        if not rota_data:
            return {'message': 'Rota não encontrada'}, 404

        rota_json = rota_ns.payload
        
        rota_data.nome = rota_json.get("nome", rota_data.nome)

        db.session.commit()
        
        return rota_schema.dump(rota_data), 200

    @rota_ns.doc('deletar_rota')
    def delete(self, id):
        """Deleta um rota pelo ID"""
        rota_data = RotaModel.query.get(id)
        if not rota_data:
            return {'message': 'Rota não encontrado'}, 404
        
        db.session.delete(rota_data)
        db.session.commit()
        return '', 204
