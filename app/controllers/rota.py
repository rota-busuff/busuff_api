from flask import request, jsonify
from app.models.rota import RotaModel
from app.schemas.rota import RotaSchema
from app.extensions.db import db

rota_schema = RotaSchema()
rota_list_schema = RotaSchema(many=True)

def get_rota(id):
    rota_data = RotaModel.query.get(id)
    if rota_data:
        return rota_schema.dump(rota_data), 200
    
    return jsonify({'message': 'Rota não encontrada'}), 404

def create_rota():
    rota_json = request.get_json()
    
    rota_model = RotaModel(
        nome=rota_json['nome']
    )
    
    db.session.add(rota_model)
    db.session.commit()
    
    return rota_schema.dump(rota_model), 201

def update_rota(id):
    rota_data = RotaModel.query.get(id)
    
    if not rota_data:
        return jsonify({'message': 'Rota não encontrada'}), 404

    rota_json = request.get_json()
    
    rota_data.nome = rota_json.get("nome", rota_data.nome)

    db.session.commit()
    
    return rota_schema.dump(rota_data), 200

def delete_rota(id):
    rota_data = RotaModel.query.get(id)
    if not rota_data:
        return jsonify({'message': 'Rota não encontrada'}), 404
    
    db.session.delete(rota_data)
    db.session.commit()
    return '', 204

def get_rotas():
    return rota_list_schema.dump(RotaModel.query.all()), 200
