from flask import request, jsonify
from app import app, db
from app.models.parada import Parada
from flask_jwt_extended import jwt_required

@app.route('/paradas', methods=['POST'])
@jwt_required()
def criar_parada():
    data = request.get_json()

    try:
        nova_parada = Parada(
            nome=data['nome'],
            endereco=data['endereco'],
            latitude=data['latitude'],
            longitude=data['longitude']
        )
        
        db.session.add(nova_parada)
        db.session.commit()

        return jsonify({"message": "Parada criada com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
