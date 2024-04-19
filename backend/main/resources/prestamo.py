from flask_restful import Resource
from flask import request
from main.models import UsuarioModel
from .. import db

#------------Prestamos----------------
    
PRESTAMOS = {
    1:{"usuario":"Coca", "tiempo":"2 semanas", "libro":"El principito"}

}

class Prestamo(Resource):

    def get(self,id):
        if int(id) in PRESTAMOS:
            return PRESTAMOS[int(id)]
        else:
            return "Not found", 404

class Prestamos(Resource):

    def get(self):
        return PRESTAMOS
        
    def post(self):
        prestamo = request.get_json()
        id = int(max(PRESTAMOS.keys())) + 1
        PRESTAMOS[id] = prestamo
        return PRESTAMOS[id], 201

    # def post(self, id_usuario):
    #     if int(id) in USUARIOS:
    #         usuario_id = int(id_usuario)
    #         usuario_nombre = USUARIOS[usuario_id]["nombre"] #Pedir el id de usuario?
    #         prestamo = request.get_json()
    #         prestamo["usuario"] = usuario_nombre  # Agregar el nombre del usuario al préstamo
    #         prestamo_id = int(max(PRESTAMOS.keys())) + 1 #Pide que tenga la misma estructura
    #         PRESTAMOS[prestamo_id] = prestamo
    #         return PRESTAMOS[prestamo_id], 201
    #     else:
    #         return "Usuario no encontrado", 404

