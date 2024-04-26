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

        # Verificar si el usuario ya existe en la base de datos
        usuario_existente = db.session.query(UsuarioModel).filter_by(id=usuario_id).first()
        if usuario_existente:
            return 'El id de usuario ya existe', 404
        else:
            # Si el usuario no existe, crea el usuario y lo agrega a la tabla de usuarios
            nuevo_usuario = UsuarioModel.from_json(data)
            db.session.add(nuevo_usuario)
            db.session.commit()
            return nuevo_usuario.to_json(), 201

#Asi era con el id en la URL
    # def post(self,id):
    #     usuario = db.session.query(UsuarioModel).get(id)
    #     if usuario: #SI el id del usuario ya existe:
    #         return 'El id de usuario ya existe', 404
    #     else: #Crea el usuario y lo agrega a la tabla usuarios
    #         Usuarios.post(Usuarios())