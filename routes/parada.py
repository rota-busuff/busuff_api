from flask_restx import Namespace
from controllers.parada import Parada, ParadaList, parada_ns

parada_ns.add_resource(Parada, '/<int:id>')
parada_ns.add_resource(ParadaList, '')
