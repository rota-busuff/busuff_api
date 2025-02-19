from flask import Flask
from flask_restx import Api
from app.extensions.db import db
from app.extensions.ma import ma
from config import Config

api = Api(
    title='BusUFF API',
    version='1.0',
    description='API para BusUFF',
    doc='/docs'
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializando extensões
    db.init_app(app)
    ma.init_app(app)
    
    # Registrando rotas com Namespaces
    from app.routes import register_routes
    register_routes(api)

    # Registrando o api com o app
    api.init_app(app)
    
    return app
