from flask_restful import Resource
from flask import request

#Los numeros son los Id
USUARIOS = {
    1:{"nombre":"Josefina","rol":"Admin"},
    2:{"nombre":"Luna","rol":"Cliente"},
    3:{"nombre":"Marco","rol":"Bibliotecario"}
    }

class Usuario(Resource):
    def get(self,id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        else:
            return "Not found", 404
        
    def delete(self,id):
        if int(id) in  USUARIOS:
            del USUARIOS[int(id)]
            return "", 204

        return "Not found", 404
    
    def put(self,id):
        if int(id) in  USUARIOS:
            usuario = USUARIOS[int(id)]
            data = request.get_json()
            usuario.update(data)
            return "", 201

        return "Not found", 404

#Aca obtenemos TODOS los usuarios
class Usuarios(Resource):
    def get(self):
        return USUARIOS
    
    # En POST creo un usuario con su esctructura
    def post(self):
        usuario = request.get_json()
        id = int(max(USUARIOS.keys())) + 1
        USUARIOS[id] = usuario
        return USUARIOS[id], 201
    
LIBROS = {
    1: {"nombre": "El principito", "autor": "Antoine De Saint Exupery"},
    2: {"nombre": "Narnia", "autor": "C.S. Lewis"}
}

class Libros(Resource):
    def get(self,id):
        if int(id) in LIBROS:
            return LIBROS[int[id]]
        else:
            return "Not found", 404
        
    def delete(self,id):
        if int(id) in  LIBROS:
            del LIBROS[int[id]]
            return "", 204

        return "Not found", 404
    
class Libro(Resource):
    #Obtiene lista de todos los libros
    def get(self,id):
        if int(id) in LIBROS:
            return LIBROS[int[id]]
        else:
            return "Not found", 404
    #Elimina un libro
    def delete(self,id):
        if int(id) in  LIBROS:
            del LIBROS[int[id]]
            return "", 204

        return "Not found", 404
    #Edita un libro
    def put(self,id):
        if int(id) in  LIBROS:
            libro = LIBROS[int[id]]
            data = request.get_json
            libro.update(data)
            return "", 201

        return "Not found", 404

    

