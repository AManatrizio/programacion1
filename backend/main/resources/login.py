from flask_restful import Resource
from flask import request
from usuario import USUARIOS

class LogIn(Resource):
    def post(self, id):
        if id in USUARIOS:
            return 'Sesion Iniciada', 200
            
        return 'El id', USUARIOS, 'no existe.', 404
