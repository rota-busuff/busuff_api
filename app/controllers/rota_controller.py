from flask import request, jsonify
from app import app, db
from app.models.rota import Rota
from flask_jwt_extended import jwt_required

@app.route('/rotas', methods=['POST'])
@jwt_required()
def criar_rota():
    data = request.get_json()

    try:
        nova_rota = Rota(
            nome=data['nome'],
            inicio_end=data['inicio_end'],
            destino_end=data['destino_end']
        )
        
        db.session.add(nova_rota)
        db.session.commit()

        return jsonify({"message": "Rota criada com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
