from flask import request
from flask_restx import Resource, Namespace, fields

from models.historico import HistoricoModel 
from schemas.historico import HistoricoSchema

historico_ns = Namespace('historico', description='Operações relacionadas ao histórico')

historico_schema = HistoricoSchema()
historico_list_schema = HistoricoSchema(many=True)

item = historico_ns.model('Historico', {
    'id_rota': fields.Integer(description="id da rota"),
    'data_registro': fields.DateTime(description="Data e hora do registro"),
    'posicao': fields.Integer(description="chave estrangeira da parada"),
    'mensagem': fields.String(description="previsao de chegada no proximo ponto")
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
        
        historico_data.id_rota = historico_json.get("id_rota", historico_data.id_rota)
        historico_data.data_registro = historico_json.get("data_registro", historico_data.data_registro)
        historico_data.posicao = historico_json.get("posicao", historico_data.posicao)
        historico_data.mensagem = historico_json.get("mensagem", historico_data.mensagem)

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
            id_rota=historico_json['id_rota'],
            data_registro=historico_json['data_registro'],
            posicao=historico_json['posicao'],
            mensagem=historico_json['mensagem'],
        )
        
        historico_model.add_to_db()
        
        return historico_schema.dump(historico_model), 200
