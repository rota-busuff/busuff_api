from flask import Flask
from flask_restx import Api, Resource

from server.instance import server

db_users = []

app, api = server.app, server.api

@api.route('/usuarios')
class Usuario(Resource):
    def get(self,):
        return db_users, 200
    
    def post(self,):
        response = api.payload
        print(response)
        db_users.append(response)
        return response, 200