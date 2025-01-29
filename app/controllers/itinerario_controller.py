from flask import request, jsonify
from app import app, db
from app.models.itinerario import Itinerario
from flask_jwt_extended import jwt_required

@app.route('/itinerarios', methods=['POST'])
@jwt_required()
def criar_itinerario():
    data = request.get_json()

    try:
        novo_itinerario = Itinerario(
            rota_nome=data['rota_nome'],
            horario_de_partida=data['horario_de_partida']
        )
        
        db.session.add(novo_itinerario)
        db.session.commit()

        return jsonify({"message": "Itinerário criado com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
