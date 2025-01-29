from flask import Flask
from .controllers import init_app as init_controllers
from .models import init_app as init_models
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Configuração do ambiente (banco, etc)

    init_models(app)  # Inicializa o banco de dados
    init_controllers(app)  # Inicializa os controladores

    return app
