from flask_restful import Resource
from flask import request
from main.models import UsuarioModel
from .usuario import Usuarios
from .. import db

class SignIn(Resource):
    def post(self, id):
        usuario = db.session.query(UsuarioModel).get(id)
        if usuario:
            return 'El usuario ya existe', 404
        else:
            Usuarios.post()