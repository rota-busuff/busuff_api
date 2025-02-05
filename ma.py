from flask_marshmallow import Marshmallow
from server.instance import server

ma = Marshmallow(server.app)