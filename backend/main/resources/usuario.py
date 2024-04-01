from flask_restful import Resource
from flask import request

USUARIOS = {
    1:['nombre', 'prestamos', 'notificaciones']
}

class Usuario(Resource):
    def get(self, id):
        if id in USUARIOS:
            return USUARIOS(id)
        return 'No existe el id', 404
    
    def delete(self, id):
        if id in USUARIOS:
            del USUARIOS[id]
            return '', 204
        return 'No existe el id', 404
    
    def put(self, id):
        if id in USUARIOS:
            usuario = USUARIOS(id)
            data = request.get_json()
            usuario.update(data)
            return '', 201
        return 'No existe el id', 404

class Usuarios(Resource):
    def get(self):
        return USUARIOS
    
    def post(self):
        usuario = request.get_json()
        id = int(max(USUARIOS.keys())) + 1
        USUARIOS[id] = usuario
        return 'Usuario: ', USUARIOS[id], 'creado.', 201
