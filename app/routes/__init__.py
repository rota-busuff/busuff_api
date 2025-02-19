from app.routes.usuario import usuario_ns
from app.routes.rota import rota_ns
from app.routes.parada import parada_ns
from app.routes.horario import horario_ns
from app.routes.historico import historico_ns
from app.routes.rota_parada import rota_parada_ns
from app.routes.viagem import viagem_ns

def register_routes(api):
    namespaces = [
        usuario_ns,
        rota_ns,
        parada_ns,
        horario_ns,
        historico_ns,
        rota_parada_ns,
        viagem_ns
    ]

    for ns in namespaces:
        api.add_namespace(ns)
