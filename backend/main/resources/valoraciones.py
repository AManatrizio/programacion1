from flask_restful import Resource
from flask import request
from main.models import UsuarioModel
from .. import db
from .libros import LIBROS


#--------------Valoracion----------------
    
VALORACION = { #Como puedo hacer que el libro sea el mismo libro de id 1 de LIBROS?
    1:{"libro":"El Principito","valoracion":"5"},
    2:{"libro":"Narnia", "valoracion":"4"}
}

class Valoraciones(Resource):
    def get(self):
        return VALORACION
        
    def post(self):
        valo = request.get_json()
        id = int(max(VALORACION.keys())) + 1
        VALORACION[id] = valo
        return VALORACION[id], 201
        
class Valoracion(Resource):
    def get(self, id):
        if int(id) in LIBROS:
            return "la valoracion del libro", id, "es", LIBROS[int(id)]["valoracion"]
    def post(self,id):
        if int(id) in LIBROS:
            valoracion = request.get_json()
            LIBROS[int(id)]["valoracion"].update(int(valoracion))
            return "La valoracion del libro", id, "es", valoracion, 201
        return "El id no existe", 400
