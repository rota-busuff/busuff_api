from flask_restx import Namespace
from controllers.viagem import Viagem,ViagemList, viagem_ns

viagem_ns.add_resource(Viagem, '/<int:id>')
viagem_ns.add_resource(ViagemList, '')
