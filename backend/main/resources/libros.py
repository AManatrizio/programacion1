from flask_restful import Resource
from flask import request

LIBROS = {
    1:{'nombre': 'Harry Potter y la Piedra Filosofal',
       'autor': 'JK',
       'genero': 'Fantasia',
       'estado': 'En prestamo'
       },
    2:{'nombre': 'Harry Potter y el Cáliz de Fuego',
       'autor': 'JK',
       'genero': 'Fantasia',
       'estado': 'Disponible'
       }
}

class Libro(Resource):
    def get(self, id):
        if int(id) in LIBROS:
            return LIBROS[int(id)]
        return 'No existe el id', 404
    
    def delete(self, id):
        if int(id) in LIBROS:
            del LIBROS[int(id)]
            return '', 204
        return 'No existe el id', 404
    
    def put(self, id):
        if int(id) in LIBROS:
            libro = LIBROS[int(id)]
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
        LIBROS[int(id)] = libro
        return 'Libro: ', LIBROS[int(id)], 'creado.', 201
