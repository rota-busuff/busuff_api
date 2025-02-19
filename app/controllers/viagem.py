from flask import request, jsonify
from app.models.viagem import ViagemModel
from app.schemas.viagem import ViagemSchema
from app.extensions.db import db

viagem_schema = ViagemSchema()
viagem_list_schema = ViagemSchema(many=True)

def get_viagem(id):
    viagem_data = ViagemModel.query.get(id)
    if viagem_data:
        return viagem_schema.dump(viagem_data), 200
    
    return jsonify({'message': 'Viagem não encontrada'}), 404

def create_viagem():
    viagem_json = request.get_json()
    
    viagem_model = ViagemModel(
        id_rota=viagem_json['id_rota'],
        data_inicio=viagem_json['data_inicio'],
        data_inicio=viagem_json['data_inicio'],
    )
    
    db.session.add(viagem_model)
    db.session.commit()
    
    return viagem_schema.dump(viagem_model), 201

def update_viagem(id):
    viagem_data = ViagemModel.query.get(id)
    
    if not viagem_data:
        return jsonify({'message': 'Viagem não encontrada'}), 404

    viagem_json = request.get_json()
    
    viagem_data.id_rota = viagem_json.get("id_rota", viagem_data.id_rota)
    viagem_data.data_inicio = viagem_json.get("data_inicio", viagem_data.data_inicio)
    viagem_data.data_inicio = viagem_json.get("data_inicio", viagem_data.data_inicio)

    db.session.commit()
    
    return viagem_schema.dump(viagem_data), 200

def delete_viagem(id):
    viagem_data = ViagemModel.query.get(id)
    if not viagem_data:
        return jsonify({'message': 'Viagem não encontrada'}), 404
    
    db.session.delete(viagem_data)
    db.session.commit()
    return '', 204

def get_viagems():
    return viagem_list_schema.dump(ViagemModel.query.all()), 200
