from flask import Blueprint

from app.controllers.motorista_controller import cadastrar_motorista

# Definindo o Blueprint para a API
api_bp = Blueprint('api', __name__)

@api_bp.route('/home', methods=['GET'])
def home():
    return "home", 200