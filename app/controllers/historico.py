from flask import request, jsonify
from app.models.historico import HistoricoModel
from app.schemas.historico import HistoricoSchema
from app.extensions.db import db

historico_schema = HistoricoSchema()
historico_list_schema = HistoricoSchema(many=True)

def get_historico(id):
    historico_data = HistoricoModel.query.get(id)
    if historico_data:
        return historico_schema.dump(historico_data), 200
    
    return jsonify({'message': 'Histórico não encontrado'}), 404

def create_historico():
    historico_json = request.get_json()
    
    historico_model = HistoricoModel(
        id_rota=historico_json['id_rota'],
        data_registro=historico_json['data_registro'],
        posicao=historico_json['posicao'],
        mensagem=historico_json['mensagem']
    )
    
    db.session.add(historico_model)
    db.session.commit()
    
    return historico_schema.dump(historico_model), 201

def update_historico(id):
    historico_data = HistoricoModel.query.get(id)
    
    if not historico_data:
        return jsonify({'message': 'Histórico não encontrado'}), 404

    historico_json = request.get_json()
    
    historico_data.id_rota = historico_json.get("id_rota", historico_data.id_rota)
    historico_data.data_registro = historico_json.get("data_registro", historico_data.data_registro)
    historico_data.posicao = historico_json.get("posicao", historico_data.posicao)
    historico_data.mensagem = historico_json.get("mensagem", historico_data.mensagem)

    db.session.commit()
    
    return historico_schema.dump(historico_data), 200

def delete_historico(id):
    historico_data = HistoricoModel.query.get(id)
    if not historico_data:
        return jsonify({'message': 'Histórico não encontrado'}), 404
    
    db.session.delete(historico_data)
    db.session.commit()
    return '', 204

def get_historicos():
    return historico_list_schema.dump(HistoricoModel.query.all()), 200
