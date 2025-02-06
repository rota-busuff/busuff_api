from flask import request
from flask_restx import Resource, Namespace, fields

from models.usuario import UsuarioModel
from schemas.usuario import UsuarioSchema

usuario_ns = Namespace('usuarios', description='Operações relacionadas a usuários')

usuario_schema = UsuarioSchema()
usuario_list_schema = UsuarioSchema(many=True)

item = usuario_ns.model('Usuario', {
    'login': fields.String(description="Nome de usuário"),
    'senha': fields.String(description="Senha do usuário"),
    'perfil': fields.String(description="Perfil do usuário"),
    'online': fields.Integer(default=0)
})

@usuario_ns.route('/<int:id>')
class Usuario(Resource):
    def get(self, id):
        usuario_data = UsuarioModel.find_by_id(id)
        if usuario_data:
            return usuario_schema.dump(usuario_data), 200
        
        return {'message': 'Usuário não encontrado'}, 404
    
    @usuario_ns.expect(item)
    def put(self, id):
        usuario_data = UsuarioModel.find_by_id(id)
        
        if not usuario_data:
            return {'message': 'Usuário não encontrado'}, 404

        usuario_json = request.get_json()
        
        usuario_data.login = usuario_json.get("login", usuario_data.login)
        usuario_data.senha = usuario_json.get("senha", usuario_data.senha)
        usuario_data.perfil = usuario_json.get("perfil", usuario_data.perfil)

        usuario_data.add_to_db()
        
        return usuario_schema.dump(usuario_data), 200
    
    def delete(self, id):
        usuario_data = UsuarioModel.find_by_id(id)
        if not usuario_data:
            return {'message': 'Usuário não encontrado'}, 404
        
        usuario_data.delete_from_db()
        return '', 204

@usuario_ns.route('')
class UsuarioList(Resource):
    def get(self):
        return usuario_list_schema.dump(UsuarioModel.find_all()), 200
    
    @usuario_ns.expect(item)
    @usuario_ns.doc('Criar um usuário')
    def post(self):
        usuario_json = request.get_json()
        
        usuario_model = UsuarioModel(
            login=usuario_json['login'],
            senha=usuario_json['senha'],
            perfil=usuario_json['perfil'],
            online=usuario_json.get('online', 0)
        )
        
        usuario_model.add_to_db()
        
        return usuario_schema.dump(usuario_model), 200
