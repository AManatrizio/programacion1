from flask_restful import Resource
from flask import request

USUARIOS = {
    1: {
        "id": 1,
        "nombre": "Juan",
        "apellido": "Perez",
        "edad": 30
    },
    2: {
        "id": 2,
        "nombre": "María",
        "apellido": "González",
        "edad": 25
    },
    3: {
        "id": 3,
        "nombre": "Carlos",
        "apellido": "López",
        "edad": 35
    }
}

class Usuario(Resource):
    # Método para manejar solicitudes GET para un usuario específico
    def get(self, id):
        if id in USUARIOS:
            return USUARIOS[id]
        #si no existe
        return 'No existe el id', 404
    
    # Método para manejar solicitudes DELETE para un usuario específico
    def delete(self, id):
        if id in USUARIOS:
            del USUARIOS[id]
            return '', 204
        #si no existe
        return 'No existe el id', 404
    
    # Método para manejar solicitudes PUT para actualizar un usuario específico
    def put(self, id):
        if id in USUARIOS:
            usuario = USUARIOS[id]
            data = request.get_json()
            usuario.update(data)
            return '', 201
        #si no existe
        return 'No existe el id', 404

class Usuarios(Resource):
    # Método para manejar solicitudes GET para obtener todos los usuarios
    def get(self):
        return USUARIOS
    
    # Método para manejar solicitudes POST para agregar un nuevo usuario
    def post(self):
        usuario = request.get_json()
        id = int(max(USUARIOS.keys(), default=0)) + 1
        usuario["id"] = id
        USUARIOS[id] = usuario
        return USUARIOS[id], 201