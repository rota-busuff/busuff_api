from flask import request, jsonify
from app import app, db
from app.models.motorista import Motorista
from flask_jwt_extended import jwt_required

@app.route('/motoristas', methods=['POST'])
@jwt_required()
def criar_motorista():
    data = request.get_json()

    try:
        novo_motorista = Motorista(
            nome=data['nome'],
            usuario_id=data['usuario_id']
        )
        
        db.session.add(novo_motorista)
        db.session.commit()

        return jsonify({"message": "Motorista criado com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
