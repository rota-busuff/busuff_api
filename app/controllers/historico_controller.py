from flask import request, jsonify
from app import app, db
from app.models.historico import Historico
from flask_jwt_extended import jwt_required

@app.route('/historico', methods=['POST'])
@jwt_required()
def registrar_historico():
    data = request.get_json()

    try:
        novo_historico = Historico(
            motorista_nome=data['motorista_nome'],
            rota_nome=data['rota_nome'],
            endereco=data['endereco'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            data_hora=data['data_hora']
        )
        
        db.session.add(novo_historico)
        db.session.commit()

        return jsonify({"message": "Histórico registrado com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
