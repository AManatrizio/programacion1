from flask_restful import Resource
from flask import request
from .libros import LIBROS, Libro, Libros

VALORACIONES = {
    1:{'valoracion': '***',
       'usuario': 1,
       'libro': '2'
       },
    2:{'valoracion': '**',
       'usuario': 1,
       'libro': '1'
       },
    3:{'valoracion': '***',
       'usuario': 2,
       'libro': '2'
       },
    4:{'valoracion': '**',
       'usuario': 4,
       'libro': '1'
       }
}

class Valoracion(Resource):
    def get(self):
        if id in VALORACIONES:
            return VALORACIONES(id)
        return 'No existe', 404

class Valoraciones(Resource):
    def get(self):
        return VALORACIONES
    
    def post(self):
        valoracion = request.get_json()
        id = int(max(VALORACIONES.keys())) + 1
        VALORACIONES[id] = valoracion
        return 'Valoracion: ', VALORACIONES[id], 'agregada.', 201



