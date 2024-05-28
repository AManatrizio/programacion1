from flask_restful import Resource
from flask import request
from main.models import UsuarioModel
from main.resources import UsuariosResource
from .usuario import Usuarios
from .. import db

class SignIn(Resource):
    def post(self):
        data = request.get_json()
        usuario_id = data.get('id')

        usuario_existente = db.session.query(UsuarioModel).filter_by(id=usuario_id).first()
        if usuario_existente:
            return 'El id de usuario ya existe', 404
        else:
            nuevo_usuario = UsuarioModel.from_json(data)
            db.session.add(nuevo_usuario)
            db.session.commit()
            return nuevo_usuario.to_json(), 201