from flask_restful import Resource
from flask import request
from libros import LIBROS, Libro, Libros

COMENTARIOS = {}

class Comentarios(Resource):
    def post(self):
        libro = input("ID del libro a comentar")
        comentario = request.get_json()
        id = int(max(COMENTARIOS.keys())) + 1
        COMENTARIOS[id] = comentario
        LIBROS[libro][2] = comentario
        return 'Comentario: ', COMENTARIOS[id], 'agregado.', 201