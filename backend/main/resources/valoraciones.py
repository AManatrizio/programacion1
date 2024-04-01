from flask_restful import Resource
from flask import request
from libros import LIBROS, Libro, Libros

VALORACIONES = {}

class Valoraciones(Resource):
    def post(self):
        libro = input("ID del libro a valorar")
        valoracion = request.get_json()
        id = int(max(VALORACIONES.keys())) + 1
        VALORACIONES[id] = valoracion
        LIBROS[libro][2] = valoracion
        return 'Valoracion: ', VALORACIONES[id], 'agregada.', 201