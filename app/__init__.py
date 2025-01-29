from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Inicializando o Flask, banco de dados e JWT
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@<host>/<database>'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'jwt_secret_key'  # Chave secreta para JWT

# Inicializando extensões
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Importando todos os controllers
from app.controllers import usuario_controller, motorista_controller, parada_controller, rota_controller, historico_controller, viagem_controller, itinerario_controller

if __name__ == '__main__':
    app.run(debug=True)
