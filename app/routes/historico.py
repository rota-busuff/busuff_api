from flask_restx import Namespace, Resource, fields
from sqlalchemy.orm import aliased
from app.models.historico import HistoricoModel
from app.models.parada import ParadaModel
from app.models.rota import RotaModel
from app.models.usuario import UsuarioModel
from app.schemas.historico import HistoricoSchema
from app.extensions.db import db

historico_ns = Namespace('historico', description='Operações relacionadas a históricos')

historico_schema = HistoricoSchema()
historico_list_schema = HistoricoSchema(many=True)

item = historico_ns.model('Historico', {
    'id_rota': fields.Integer(description="ID da rota"),
    'data_registro': fields.DateTime(description="Data do registro"),
    'posicao': fields.Integer(description="Última parada registrada"),
    'mensagem': fields.String(description="Mensagem de aproximação")
})

@historico_ns.route('/')
class HistoricoList(Resource):
    @historico_ns.doc('listar_historicos')
    def get(self):
        """Lista todos os históricos"""
        return historico_list_schema.dump(HistoricoModel.query.all()), 200

    @historico_ns.expect(item)
    @historico_ns.doc('criar_historico')
    def post(self):
        """Cria um novo histórico"""
        historico_json = historico_ns.payload
        
        historico_model = HistoricoModel(
            id_rota=historico_json['id_rota'],
            data_registro=historico_json['data_registro'],
            posicao=historico_json['posicao'],
            mensagem=historico_json['mensagem']
        )
        
        db.session.add(historico_model)
        db.session.commit()
        
        return historico_schema.dump(historico_model), 201

@historico_ns.route('/<int:id>')
@historico_ns.param('id', 'O identificador do histórico')
class Historico(Resource):
    @historico_ns.doc('obter_historico')
    def get(self, id):
        """Obtém um histórico pelo ID"""
        historico_data = HistoricoModel.query.get(id)
        if historico_data:
            return historico_schema.dump(historico_data), 200
        
        return {'message': 'Histórico não encontrado'}, 404

    @historico_ns.expect(item)
    @historico_ns.doc('atualizar_historico')
    def put(self, id):
        """Atualiza um histórico pelo ID"""
        historico_data = HistoricoModel.query.get(id)
        
        if not historico_data:
            return {'message': 'Histórico não encontrado'}, 404

        historico_json = historico_ns.payload
        
        historico_data.id_rota = historico_json.get("id_rota", historico_data.id_rota)
        historico_data.data_registro = historico_json.get("data_registro", historico_data.data_registro)
        historico_data.posicao = historico_json.get("posicao", historico_data.posicao)
        historico_data.mensagem = historico_json.get("mensagem", historico_data.mensagem)

        db.session.commit()
        
        return historico_schema.dump(historico_data), 200

    @historico_ns.doc('deletar_historico')
    def delete(self, id):
        """Deleta um histórico pelo ID"""
        historico_data = HistoricoModel.query.get(id)
        if not historico_data:
            return {'message': 'Histórico não encontrado'}, 404
        
        db.session.delete(historico_data)
        db.session.commit()
        return '', 204

@historico_ns.route('/movimento')
class HistoricoMovimento(Resource):
    @historico_ns.doc('listar todos os históricos formatados')
    def get(self):
        """Obtém todos os históricos formatados"""
        
        rota = aliased(RotaModel)
        parada = aliased(ParadaModel)
        usuario = aliased(UsuarioModel)
        
        historico_data = db.session.query(
            HistoricoModel.id,
            rota.nome.label("rota_nome"),
            parada.nome.label("parada_nome"),
            HistoricoModel.mensagem,
            usuario.online
        ).join(rota, HistoricoModel.id_rota == rota.id
        ).join(parada, HistoricoModel.posicao == parada.id
        ).join(usuario, HistoricoModel.id_rota == usuario.login
        ).all()

        if historico_data:
            return [
                {
                    "id": item.id,
                    "rota": item.rota_nome,
                    "posicao": item.parada_nome,
                    "mensagem": item.mensagem,
                    "online": item.online
                } for item in historico_data
            ], 200
        
        return {'message': 'Nenhum histórico encontrado'}, 404
