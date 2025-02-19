from flask import request, jsonify
from app.models.parada import ParadaModel
from app.schemas.parada import ParadaSchema
from app.extensions.db import db

parada_schema = ParadaSchema()
parada_list_schema = ParadaSchema(many=True)

def get_parada(id):
    parada_data = ParadaModel.query.get(id)
    if parada_data:
        return parada_schema.dump(parada_data), 200
    
    return jsonify({'message': 'Parada não encontrada'}), 404

def create_parada():
    parada_json = request.get_json()
    
    parada_model = ParadaModel(
        nome=parada_json['nome'],
        latitude=parada_json['latitude'],
        longitude=parada_json['longitude'],
    )
    
    db.session.add(parada_model)
    db.session.commit()
    
    return parada_schema.dump(parada_model), 201

def update_parada(id):
    parada_data = ParadaModel.query.get(id)
    
    if not parada_data:
        return jsonify({'message': 'Parada não encontrada'}), 404

    parada_json = request.get_json()
    
    parada_data.nome = parada_json.get("nome", parada_data.nome)
    parada_data.latitude = parada_json.get("latitude", parada_data.latitude)
    parada_data.longitude = parada_json.get("longitude", parada_data.longitude)

    db.session.commit()
    
    return parada_schema.dump(parada_data), 200

def delete_parada(id):
    parada_data = ParadaModel.query.get(id)
    if not parada_data:
        return jsonify({'message': 'Parada não encontrada'}), 404
    
    db.session.delete(parada_data)
    db.session.commit()
    return '', 204

def get_paradas():
    return parada_list_schema.dump(ParadaModel.query.all()), 200
