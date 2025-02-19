from flask import request, jsonify
from app.models.usuario import UsuarioModel
from app.schemas.usuario import UsuarioSchema
from app.extensions.db import db

usuario_schema = UsuarioSchema()
usuario_list_schema = UsuarioSchema(many=True)

def get_usuario(id):
    usuario_data = UsuarioModel.query.get(id)
    if usuario_data:
        return usuario_schema.dump(usuario_data), 200
    
    return jsonify({'message': 'Usuário não encontrado'}), 404

def create_usuario():
    usuario_json = request.get_json()
    
    usuario_model = UsuarioModel(
        login=usuario_json['login'],
        senha=usuario_json['senha'],
        perfil=usuario_json['perfil'],
        online=usuario_json.get('online', 0)
    )
    
    db.session.add(usuario_model)
    db.session.commit()
    
    return usuario_schema.dump(usuario_model), 201

def update_usuario(id):
    usuario_data = UsuarioModel.query.get(id)
    
    if not usuario_data:
        return jsonify({'message': 'Usuário não encontrado'}), 404

    usuario_json = request.get_json()
    
    usuario_data.login = usuario_json.get("login", usuario_data.login)
    usuario_data.senha = usuario_json.get("senha", usuario_data.senha)
    usuario_data.perfil = usuario_json.get("perfil", usuario_data.perfil)

    db.session.commit()
    
    return usuario_schema.dump(usuario_data), 200

def delete_usuario(id):
    usuario_data = UsuarioModel.query.get(id)
    if not usuario_data:
        return jsonify({'message': 'Usuário não encontrado'}), 404
    
    db.session.delete(usuario_data)
    db.session.commit()
    return '', 204

def get_usuarios():
    return usuario_list_schema.dump(UsuarioModel.query.all()), 200
