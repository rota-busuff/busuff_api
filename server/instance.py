from flask import Flask, Blueprint
from flask_restx import Api
from db import db

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.app,
            version='1.0',
            title='BusUFF API',
            description='API para BusUFF',
            doc='/docs')
        self.app.register_blueprint(self.blueprint)
        
        self.app.config["SQLALCHEMY_DATABASE_URI"] = ""
        self.app.config["PROPAGATE_EXCEPTIONS"] = True
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        
        db.init_app(self.app)
        
        self.usuario_ns = self.usuario_ns()
    
    def usuario_ns(self,):
            return self.api.namespace(name="Usuarios", description="usuarios cadastrados", path="/usuarios")
        
    def run(self,):
        self.app.run(
            debug=True
        )
        
server = Server()