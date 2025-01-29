from flask_sqlalchemy import SQLAlchemy

# Instanciando o objeto SQLAlchemy
db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
