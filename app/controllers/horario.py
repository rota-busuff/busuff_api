from flask import request, jsonify
from app.models.horario import HorarioModel
from app.schemas.horario import HorarioSchema
from app.extensions.db import db

horario_schema = HorarioSchema()
horario_list_schema = HorarioSchema(many=True)

def get_horario(id):
    horario_data = HorarioModel.query.get(id)
    if horario_data:
        return horario_schema.dump(horario_data), 200
    
    return jsonify({'message': 'Horário não encontrado'}), 404

def create_horario():
    horario_json = request.get_json()
    
    horario_model = HorarioModel(
        id_rota=horario_json['id_rota'],
        horario=horario_json['horario']
    )
    
    db.session.add(horario_model)
    db.session.commit()
    
    return horario_schema.dump(horario_model), 201

def update_horario(id):
    horario_data = HorarioModel.query.get(id)
    
    if not horario_data:
        return jsonify({'message': 'Horário não encontrado'}), 404

    horario_json = request.get_json()
    
    horario_data.id_rota = horario_json.get("id_rota", horario_data.id_rota)
    horario_data.horario = horario_json.get("horario", horario_data.horario)

    db.session.commit()
    
    return horario_schema.dump(horario_data), 200

def delete_horario(id):
    horario_data = HorarioModel.query.get(id)
    if not horario_data:
        return jsonify({'message': 'Horário não encontrado'}), 404
    
    db.session.delete(horario_data)
    db.session.commit()
    return '', 204

def get_horarios():
    return horario_list_schema.dump(HorarioModel.query.all()), 200
