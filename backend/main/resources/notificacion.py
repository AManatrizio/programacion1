from flask_restful import Resource
from flask import request
from main.models import UsuarioModel
from .. import db


#-------------Notificacion----------------------
NOTIFICACIONES = {
    1:{"mensaje":"su prestamo vence en 2 dias","hora notificacion":"2:30"},
    2:{"mensaje":"vea nuestros nuevos libros", "hora notificacion":"5:00"}
}

class Notificaciones(Resource):
    def get(self):
        return NOTIFICACIONES
    
    def post(self):
        notificacion = request.get_json()
        id = int(max(NOTIFICACIONES.keys())) + 1
        NOTIFICACIONES[id] = notificacion
        return NOTIFICACIONES[id], 201