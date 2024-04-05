from flask_restful import Resource
from flask import request

USUARIOS = {
    1:{'nombre_completo': 'Ana', 
       'contraseña': '123456789',
       'telefono': '2612345678',
       'email': 'ana@gmail.com',
       'estado': 'activo' },
    2:{'nombre_completo': 'Susana', 
       'contraseña': '123456789',
       'telefono': '2612345679',
       'email': 'susana@gmail.com',
       'estado': 'inactivo' },
}

class Usuario(Resource):
    def get(self, id):
        if id in USUARIOS:
            return USUARIOS[id]
        return 'No existe el id', 404
    
    def delete(self, id):
        if id in USUARIOS:
            del USUARIOS[id]
            return '', 204
        return 'No existe el id', 404
    
    def put(self, id):
        if id in USUARIOS:
            usuario = USUARIOS[id]
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
