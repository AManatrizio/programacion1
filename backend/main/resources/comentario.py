from flask_restful import Resource
from flask import request
from .libros import LIBROS, Libro, Libros

COMENTARIOS = {
    1:{'comentario': 'comentario'}
}

class Comentario(Resource):
    def get(self, id):
        if id in COMENTARIOS:
            return COMENTARIOS(id)
        return 'No existe el comentario', 404
    
    def delete(self, id):
        if id in COMENTARIOS:
            del COMENTARIOS[id]
            return '', 204
        return 'No existe el comentario', 404

class Comentarios(Resource):
    def post(self, id_libro):
        comentario = request.get_json()
        id = int(max(COMENTARIOS.keys())) + 1
        COMENTARIOS[id] = comentario
        LIBROS[id_libro][2] = comentario
        return 'Comentario: ', COMENTARIOS[id], 'agregado.', 201