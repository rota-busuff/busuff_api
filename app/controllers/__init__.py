from flask import Blueprint
from .usuario_controller import user_bp
from .motorista_controller import motorista_bp
from .parada_controller import parada_bp
from .rota_controller import rota_bp
from .historico_controller import historico_bp
from .viagem_controller import viagem_bp
from .itinerario_controller import itinerario_bp

# Inicializando o blueprint para registrar todos os controladores
def init_app(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(motorista_bp)
    app.register_blueprint(parada_bp)
    app.register_blueprint(rota_bp)
    app.register_blueprint(historico_bp)
    app.register_blueprint(viagem_bp)
    app.register_blueprint(itinerario_bp)
