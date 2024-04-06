from flask_restful import Resource
from flask import request
from .libros import LIBROS, Libro, Libros
from .usuario import USUARIOS

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
    def get(self, id_user):
        id_user = int(id_user)
        user_com = {}
        lista = list(USUARIOS.keys())
        if id_user not in lista:
            return "El id no existe", 404
        for i in VALORACIONES:
            if id_user == VALORACIONES[i]['usuario']:
                valoracion = VALORACIONES[i]
                user_com[i] = valoracion
        if user_com == {}:
            return "El usuario no tiene valoraciones"
        else:
            return "Valoracion/es del usuario: {}".format(user_com)

class Valoraciones(Resource):
    def get(self):
        return VALORACIONES
    
    def post(self, id_libro):
        valoracion = request.get_json()
        id = int(max(VALORACIONES.keys())) + 1
        VALORACIONES[id] = valoracion
        LIBROS[id_libro][2] = valoracion
        return 'Valoracion: ', VALORACIONES[id], 'agregada.', 201



