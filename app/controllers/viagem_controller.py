from flask import request, jsonify
from app import app, db
from app.models.viagem import Viagem
from flask_jwt_extended import jwt_required

@app.route('/iniciar_viagem', methods=['POST'])
@jwt_required()
def iniciar_viagem():
    data = request.get_json()

    try:
        nova_viagem = Viagem(
            motorista_id=data['motorista_id'],
            rota_nome=data['rota_nome'],
            data_inicio=data['data_inicio'],
            mensagem_status="Em andamento"
        )
        
        db.session.add(nova_viagem)
        db.session.commit()

        return jsonify({"message": "Viagem iniciada com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/encerrar_viagem', methods=['POST'])
@jwt_required()
def encerrar_viagem():
    data = request.get_json()

    try:
        viagem = Viagem.query.filter_by(id=data['viagem_id']).first()

        if viagem:
            viagem.data_fim = data['data_fim']
            viagem.mensagem_status = "Concluída"
            db.session.commit()

            return jsonify({"message": "Viagem encerrada com sucesso!"}), 200
        else:
            return jsonify({"message": "Viagem não encontrada!"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
