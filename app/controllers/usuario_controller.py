from flask import request, jsonify
from app import app, db
from app.models.usuario import Usuario
from flask_jwt_extended import jwt_required

@app.route('/usuarios', methods=['POST'])
@jwt_required()
def criar_usuario():
    data = request.get_json()

    try:
        novo_usuario = Usuario(
            CPF=data['CPF'],
            nome=data['nome'],
            nomeusuario=data['nomeusuario'],
            senha=data['senha'],
            email=data['email']
        )
        
        db.session.add(novo_usuario)
        db.session.commit()

        return jsonify({"message": "Usuário criado com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
