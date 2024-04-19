from flask_restful import Resource
from flask import request
from .. import db

#-------------Log In------------------
    
LOGIN = {
    1:{"nombre_usuario":"Marta", "contrasena":"Marta123"},
    2:{"nombre_usuario":"JosefaRamirez", "contrasena":"lajose"}
}
class Login(Resource):

    def get(self):
        return LOGIN

    def post(self):
        login = request.get_json()
        id = int(max(LOGIN.keys()))+1
        LOGIN[id] = login
        return LOGIN[id], 201
        