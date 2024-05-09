from flask_restful import Resource
from flask import request

LIBROS = {
        1: {
        "id": 1,
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "genero": "Realismo mágico",
        "anio_publicacion": 1967
    },
    2: {
        "id": 2,
        "titulo": "El Señor de los Anillos",
        "autor": "J.R.R. Tolkien",
        "genero": "Fantasía",
        "anio_publicacion": 1954
    },
    3: {
        "id": 3,
        "titulo": "Harry Potter y la piedra filosofal",
        "autor": "J.K. Rowling",
        "genero": "Fantasía",
        "anio_publicacion": 1997
    }
}

class Libro(Resource):
# Método para manejar solicitudes GET para un libro específico
    def get(self, id):
        if id in LIBROS:
            return LIBROS(id)
        #si no existe
        return 'No existe el id', 404
    
# Método para manejar solicitudes DELETE para un libro específico
    def delete(self, id):
        if id in LIBROS:
            del LIBROS[id]
            return '', 204
        #si no existe
        return 'No existe el id', 404
    
# Método para manejar solicitudes PUT para actualizar un libro específico 
    def put(self, id):
        if id in LIBROS:
            libro = LIBROS(id)
            data = request.get_json()
            libro.update(data)
            return '', 201
        #si no existe
        return 'No existe el id', 404

class Libros(Resource):
    # Método para manejar solicitudes GET para obtener todos los libros
    def get(self):
        return LIBROS
    
    # Método para manejar solicitudes POST para agregar un nuevo libro
    def post(self):
        libro = request.get_json()
        id = int(max(LIBROS.keys())) + 1
        LIBROS[id] = libro
        return LIBROS[id], 201