from flask_restful import Resource
from flask import request
from libros import LIBROS, Libro, Libros

VALORACIONES = {
    1:{"valoracion"}
}

class Valoraciones(Resource):
    def post(self, id_libro):
        valoracion = request.get_json()
        id = int(max(VALORACIONES.keys())) + 1
        VALORACIONES[id] = valoracion
        LIBROS[id_libro][2] = valoracion
        return 'Valoracion: ', VALORACIONES[id], 'agregada.', 201