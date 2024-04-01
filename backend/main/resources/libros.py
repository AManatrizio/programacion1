from flask_restful import Resource
from flask import request

LIBROS = {
    1:['nombre', 'valoracion']
}

class Libro(Resource):
    def get(self, id):
        if id in LIBROS:
            return LIBROS(id)
        return 'No existe el id', 404
    
    def delete(self, id):
        if id in LIBROS:
            del LIBROS[id]
            return '', 204
        return 'No existe el id', 404
    
    def put(self, id):
        if id in LIBROS:
            libro = LIBROS(id)
            data = request.get_json()
            libro.update(data)
            return '', 201
        return 'No existe el id', 404

class Libros(Resource):
    def get(self):
        return LIBROS
    
    def post(self):
        libro = request.get_json()
        id = int(max(LIBROS.keys())) + 1
        LIBROS[id] = libro
        return 'Libro: ', LIBROS[id], 'creado.', 201
