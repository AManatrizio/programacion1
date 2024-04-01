from flask_restful import Resource
from flask import request
from usuario import USUARIOS, Usuarios, Usuario

class SingIn(Resource):
    def post(self, id):
        if id in USUARIOS:
            return 'El id', USUARIOS, 'ya existe.', 404
        else:
            Usuarios.post()
