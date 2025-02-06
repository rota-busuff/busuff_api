from flask_restx import Namespace
from controllers.rota_parada import RotaParada, RotaParadaList, rota_parada_ns

rota_parada_ns.add_resource(RotaParada, '/<int:id>')
rota_parada_ns.add_resource(RotaParadaList, '')
