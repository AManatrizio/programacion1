from flask_restful import Resource
from flask import request
from .libros import LIBROS, Libro, Libros

COMENTARIOS = {
    1:{'comentario': 'comentario'}
}

class Comentario(Resource):
    def get(self, id):
        if int(id) in COMENTARIOS:
            return COMENTARIOS[int(id)]
        return 'No existe el comentario', 404
    
    def delete(self, id):
        if int(id) in COMENTARIOS:
            del COMENTARIOS[int(id)]
            return '', 204
        return 'No existe el comentario', 404

class Comentarios(Resource):
    def get(self):
        return COMENTARIOS
    
    def post(self):
        comentario = request.get_json()
        id = int(max(COMENTARIOS.keys())) + 1
        COMENTARIOS[int(id)] = comentario
        return 'Comentario: ', COMENTARIOS[int(id)], 'agregado.', 201
