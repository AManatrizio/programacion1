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
       },
    3:{'valoracion': '***',
       'usuario': '2',
       'libro': '2'
       },
    4:{'valoracion': '**',
       'usuario': '4',
       'libro': '1'
       }
}

class Valoracion(Resource):
    def get(id_user):
        user_com = {}
        for i in VALORACIONES:
            if id_user == VALORACIONES[i]['usuario']:
                valoracion = VALORACIONES[i]
                user_com[i] = valoracion
        print(user_com)

class Valoraciones(Resource):
    def get(self):
        return VALORACIONES
    
    def post(self, id_libro):
        valoracion = request.get_json()
        id = int(max(VALORACIONES.keys())) + 1
        VALORACIONES[id] = valoracion
        LIBROS[id_libro][2] = valoracion
        return 'Valoracion: ', VALORACIONES[id], 'agregada.', 201



