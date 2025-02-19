from flask import request, jsonify
from app.models.rota_parada import RotaParadaModel
from app.schemas.rota_parada import RotaParadaSchema
from app.extensions.db import db

rota_parada_schema = RotaParadaSchema()
rota_parada_list_schema = RotaParadaSchema(many=True)

def get_rota_parada(id):
    rota_parada_data = RotaParadaModel.query.get(id)
    if rota_parada_data:
        return rota_parada_schema.dump(rota_parada_data), 200
    
    return jsonify({'message': 'RotaParada não encontrada'}), 404

def create_rota_parada():
    rota_parada_json = request.get_json()
    
    rota_parada_model = RotaParadaModel(
        id_rota=rota_parada_json['id_rota'],
        id_parada=rota_parada_json['id_parada'],
        ordem=rota_parada_json['ordem'],
    )
    
    db.session.add(rota_parada_model)
    db.session.commit()
    
    return rota_parada_schema.dump(rota_parada_model), 201

def update_rota_parada(id):
    rota_parada_data = RotaParadaModel.query.get(id)
    
    if not rota_parada_data:
        return jsonify({'message': 'RotaParada não encontrada'}), 404

    rota_parada_json = request.get_json()
    
    rota_parada_data.id_rota = rota_parada_json.get("id_rota", rota_parada_data.id_rota)
    rota_parada_data.id_parada = rota_parada_json.get("id_parada", rota_parada_data.id_parada)
    rota_parada_data.ordem = rota_parada_json.get("ordem", rota_parada_data.ordem)

    db.session.commit()
    
    return rota_parada_schema.dump(rota_parada_data), 200

def delete_rota_parada(id):
    rota_parada_data = RotaParadaModel.query.get(id)
    if not rota_parada_data:
        return jsonify({'message': 'RotaParada não encontrada'}), 404
    
    db.session.delete(rota_parada_data)
    db.session.commit()
    return '', 204

def get_rota_paradas():
    return rota_parada_list_schema.dump(RotaParadaModel.query.all()), 200
