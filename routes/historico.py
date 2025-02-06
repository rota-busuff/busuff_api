from flask_restx import Namespace
from controllers.historico import Historico, HistoricoList, historico_ns

historico_ns.add_resource(Historico, '/<int:id>')
historico_ns.add_resource(HistoricoList, '')
