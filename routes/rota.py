from flask_restx import Namespace
from controllers.rota import Rota, RotaList, rota_ns

rota_ns.add_resource(Rota, '/<int:id>')
rota_ns.add_resource(RotaList, '')
