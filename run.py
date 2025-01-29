from flask import Flask
from app.config import Config
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicialize o JWTManager
    jwt = JWTManager(app)

    return app
