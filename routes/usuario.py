from flask_restx import Namespace
from controllers.usuario import Usuario, UsuarioList, usuario_ns

usuario_ns.add_resource(Usuario, '/<int:id>')
usuario_ns.add_resource(UsuarioList, '')
