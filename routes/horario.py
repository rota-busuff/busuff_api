from flask_restx import Namespace
from controllers.horario import Horario, HorarioList, horario_ns

horario_ns.add_resource(Horario, '/<int:id>')
horario_ns.add_resource(HorarioList, '')
