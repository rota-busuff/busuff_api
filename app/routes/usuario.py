from flask_restx import Namespace, Resource, fields
from app.models.usuario import UsuarioModel
from app.schemas.usuario import UsuarioSchema
from app.extensions.db import db

usuario_ns = Namespace('usuario', description='Operações relacionadas a usuários')

usuario_schema = UsuarioSchema()
usuario_list_schema = UsuarioSchema(many=True)

item = usuario_ns.model('Usuario', {
    'login': fields.Integer(description="ID de usuário (rota)"),
    'senha': fields.String(description="Senha do usuário"),
    'perfil': fields.String(description="Perfil do usuário"),
    'online': fields.Integer(default=0)
})

@usuario_ns.route('/')
class UsuarioList(Resource):
    @usuario_ns.doc('listar_usuarios')
    def get(self):
        """Lista todos os usuários"""
        return usuario_list_schema.dump(UsuarioModel.query.all()), 200

    @usuario_ns.expect(item)
    @usuario_ns.doc('criar_usuario')
    def post(self):
        """Cria um novo usuário"""
        usuario_json = usuario_ns.payload
        
        usuario_model = UsuarioModel(
            login=usuario_json['login'],
            senha=usuario_json['senha'],
            perfil=usuario_json['perfil'],
            online=usuario_json.get('online', 0)
        )
        
        db.session.add(usuario_model)
        db.session.commit()
        
        return usuario_schema.dump(usuario_model), 201

@usuario_ns.route('/<int:id>')
@usuario_ns.param('id', 'O identificador do usuário')
class Usuario(Resource):
    @usuario_ns.doc('obter_usuario')
    def get(self, id):
        """Obtém um usuário pelo ID"""
        usuario_data = UsuarioModel.query.get(id)
        if usuario_data:
            return usuario_schema.dump(usuario_data), 200
        
        return {'message': 'Usuário não encontrado'}, 404

    @usuario_ns.expect(item)
    @usuario_ns.doc('atualizar_usuario')
    def put(self, id):
        """Atualiza um usuário pelo ID"""
        usuario_data = UsuarioModel.query.get(id)
        
        if not usuario_data:
            return {'message': 'Usuário não encontrado'}, 404

        usuario_json = usuario_ns.payload
        
        usuario_data.login = usuario_json.get("login", usuario_data.login)
        usuario_data.senha = usuario_json.get("senha", usuario_data.senha)
        usuario_data.perfil = usuario_json.get("perfil", usuario_data.perfil)

        db.session.commit()
        
        return usuario_schema.dump(usuario_data), 200

    @usuario_ns.doc('deletar_usuario')
    def delete(self, id):
        """Deleta um usuário pelo ID"""
        usuario_data = UsuarioModel.query.get(id)
        if not usuario_data:
            return {'message': 'Usuário não encontrado'}, 404
        
        db.session.delete(usuario_data)
        db.session.commit()
        return '', 204
