from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from ma import ma
from db import db
from server.instance import server
from routes.usuario import usuario_ns
from routes.historico import historico_ns
from routes.rota import rota_ns

api = server.api
app = server.app

ma.init_app(app)
migrate = Migrate(app, db)

api.add_namespace(usuario_ns, path='/usuarios')
api.add_namespace(historico_ns, path='/historico')
api.add_namespace(rota_ns, path='/rotas')

if __name__ == '__main__':
    app.run(debug=True)