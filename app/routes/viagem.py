from flask_restx import Namespace, Resource, fields
from app.models.viagem import ViagemModel
from app.schemas.viagem import ViagemSchema
from app.extensions.db import db

viagem_ns = Namespace('viagem', description='Operações relacionadas a viagems')

viagem_schema = ViagemSchema()
viagem_list_schema = ViagemSchema(many=True)

item = viagem_ns.model('Viagem', {
    'id_rota': fields.Integer(description="ID da Rota"),
    'data_inicio': fields.DateTime(description="DataHora de início da viagem"),
    'data_fim': fields.DateTime(description="DataHora do fim da viagem")
})

@viagem_ns.route('/')
class ViagemList(Resource):
    @viagem_ns.doc('listar_viagens')
    def get(self):
        """Lista todos os viagens"""
        return viagem_list_schema.dump(ViagemModel.query.all()), 200

    @viagem_ns.expect(item)
    @viagem_ns.doc('criar_viagem')
    def post(self):
        """Cria uma nova viagem"""
        viagem_json = viagem_ns.payload
        
        viagem_model = ViagemModel(
            id_rota=viagem_json['id_rota'],
            data_inicio=viagem_json['data_inicio'],
            data_fim=viagem_json['data_fim']
        )
        
        db.session.add(viagem_model)
        db.session.commit()
        
        return viagem_schema.dump(viagem_model), 201

@viagem_ns.route('/<int:id>')
@viagem_ns.param('id', 'O identificador da viagem')
class Viagem(Resource):
    @viagem_ns.doc('obter_viagem')
    def get(self, id):
        """Obtém uma viagem pelo ID"""
        viagem_data = ViagemModel.query.get(id)
        if viagem_data:
            return viagem_schema.dump(viagem_data), 200
        
        return {'message': 'Viagem não encontrada'}, 404

    @viagem_ns.expect(item)
    @viagem_ns.doc('atualizar_viagem')
    def put(self, id):
        """Atualiza uma viagem pelo ID"""
        viagem_data = ViagemModel.query.get(id)
        
        if not viagem_data:
            return {'message': 'Viagem não encontrada'}, 404

        viagem_json = viagem_ns.payload
        
        viagem_data.id_rota = viagem_json.get("id_rota", viagem_data.id_rota)
        viagem_data.data_inicio = viagem_json.get("data_inicio", viagem_data.data_inicio)
        viagem_data.data_fim = viagem_json.get("data_fim", viagem_data.data_fim)

        db.session.commit()
        
        return viagem_schema.dump(viagem_data), 200

    @viagem_ns.doc('deletar_viagem')
    def delete(self, id):
        """Deleta uma viagem pelo ID"""
        viagem_data = ViagemModel.query.get(id)
        if not viagem_data:
            return {'message': 'Viagem não encontrada'}, 404
        
        db.session.delete(viagem_data)
        db.session.commit()
        return '', 204
