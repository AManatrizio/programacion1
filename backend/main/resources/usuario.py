from flask_restful import Resource
from flask import request
from main.models import UsuarioModel
from .. import db
from flask import jsonify

#--------------Usuarios-----------------

#Los numeros son los Id
USUARIOS = {
    1:{"nombre":"Josefina","rol":"Admin"},
    2:{"nombre":"Luna","rol":"Cliente"},
    3:{"nombre":"Marco","rol":"Bibliotecario"}
    }

class Usuario(Resource):
    def get(self,id):

        usuario = db.session.query(UsuarioModel).get_or_404(id)
        return usuario.to_json()
    
    def delete(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return '', 201
    
    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key , value in data:
            setattr(usuario, key, value)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201

#Aca obtenemos TODOS los usuarios
class Usuarios(Resource):

    def get(self):
        usuarios = db.session.query(UsuarioModel).all()
        usuarios_json = [usuario.to_json() for usuario in usuarios]
        return jsonify(usuarios_json)
        
    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201
    
    # def get(self):
    #     return USUARIOS
    
    # # En POST creo un usuario con su esctructura
    # def post(self):
    #     usuario = request.get_json()
    #     id = int(max(USUARIOS.keys())) + 1
    #     USUARIOS[id] = usuario
    #     return USUARIOS[id], 201

        
        



