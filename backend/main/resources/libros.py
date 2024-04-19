from flask_restful import Resource
from flask import request
from main.models import UsuarioModel
from .. import db


#--------------------Libros-------------------------
LIBROS = {
    1: {"nombre": "El principito", "autor": "Antoine De Saint Exupery", "valoracion":"5"},
    2: {"nombre": "Narnia", "autor": "C.S. Lewis", "valoracion":"4"}
}


class Libro(Resource):
    #Obtiene lista de todos los libros
    def get(self,id):
        if int(id) in LIBROS:
            return LIBROS[int(id)]
        else:
            return "Not found", 404
    #Elimina un libro
    def delete(self,id):
        if int(id) in  LIBROS:
            del LIBROS[int(id)]
            return "", 204

        return "Not found", 404
    #Edita un libro
    def put(self,id):
        if int(id) in  LIBROS:
            libros = LIBROS[int(id)]
            data = request.get_json()
            libros.update(data)
            return "", 201

        return "Not found", 404
    
class Libros(Resource):
    def get(self):
        return LIBROS
        
    def post(self):
        libro = request.get_json()
        id = int(max(LIBROS.keys())) + 1
        LIBROS[id] = libro
        return LIBROS[id], 201
    

    