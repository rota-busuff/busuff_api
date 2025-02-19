from flask_restx import Namespace, Resource, fields
from app.models.parada import ParadaModel
from app.schemas.parada import ParadaSchema
from app.extensions.db import db

parada_ns = Namespace('parada', description='Operações relacionadas a paradas')

parada_schema = ParadaSchema()
parada_list_schema = ParadaSchema(many=True)

item = parada_ns.model('Parada', {
    'nome': fields.String(description="Nome da parada"),
    'latitude': fields.Float(description="Latitude da parada"),
    'longitude': fields.Float(description="Longitude da parada"),
})

@parada_ns.route('/')
class ParadaList(Resource):
    @parada_ns.doc('listar_paradas')
    def get(self):
        """Lista todas as paradas"""
        return parada_list_schema.dump(ParadaModel.query.all()), 200

    @parada_ns.expect(item)
    @parada_ns.doc('criar_parada')
    def post(self):
        """Cria uma nova parada"""
        parada_json = parada_ns.payload
        
        parada_model = ParadaModel(
            nome=parada_json['nome'],
            latitude=parada_json['latitude'],
            longitude=parada_json['longitude'],
        )
        
        db.session.add(parada_model)
        db.session.commit()
        
        return parada_schema.dump(parada_model), 201

@parada_ns.route('/<int:id>')
@parada_ns.param('id', 'O identificador da parada')
class Parada(Resource):
    @parada_ns.doc('obter_parada')
    def get(self, id):
        """Obtém uma parada pelo ID"""
        parada_data = ParadaModel.query.get(id)
        if parada_data:
            return parada_schema.dump(parada_data), 200
        
        return {'message': 'Parada não encontrada'}, 404

    @parada_ns.expect(item)
    @parada_ns.doc('atualizar_parada')
    def put(self, id):
        """Atualiza uma parada pelo ID"""
        parada_data = ParadaModel.query.get(id)
        
        if not parada_data:
            return {'message': 'Parada não encontrada'}, 404

        parada_json = parada_ns.payload
        
        parada_data.nome = parada_json.get("nome", parada_data.nome)
        parada_data.latitude = parada_json.get("latitude", parada_data.latitude)
        parada_data.longitude = parada_json.get("longitude", parada_data.longitude)

        db.session.commit()
        
        return parada_schema.dump(parada_data), 200

    @parada_ns.doc('deletar_parada')
    def delete(self, id):
        """Deleta uma parada pelo ID"""
        parada_data = ParadaModel.query.get(id)
        if not parada_data:
            return {'message': 'Parada não encontrada'}, 404
        
        db.session.delete(parada_data)
        db.session.commit()
        return '', 204
