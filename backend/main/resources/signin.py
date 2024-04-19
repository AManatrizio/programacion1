from flask_restful import Resource
from flask import request
from .. import db


#-------------Sing In---------------- No seria lo mismo que un POST en Usuario? Crear un Usuario?

SINGIN = {
    1:{"nombre":"marta", "contrasena":"!23", "email":"marta@yahoo.com"}

}

class SingIn(Resource):
    def get(self):
        return SINGIN
        
    def post(self): #Crear un Usuario
        singin = request.get_json()
        id = int(max(SINGIN.keys())) + 1
        SINGIN[id] = singin
        return SINGIN[id], 201