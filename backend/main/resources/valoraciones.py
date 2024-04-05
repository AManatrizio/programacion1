from flask_restful import Resource
from flask import request
from .libros import LIBROS, Libro, Libros

VALORACIONES = {
    1:{'valoracion': '***',
       'usuario': '1',
       'libro': '2'
       },
    2:{'valoracion': '**',
       'usuario': '1',
       'libro': '1'
       }
}

class Valoraciones(Resource):
    def get(self):
        return VALORACIONES
    
    def post(self, id_libro):
        valoracion = request.get_json()
        id = int(max(VALORACIONES.keys())) + 1
        VALORACIONES[id] = valoracion
        LIBROS[id_libro][2] = valoracion
        return 'Valoracion: ', VALORACIONES[id], 'agregada.', 201