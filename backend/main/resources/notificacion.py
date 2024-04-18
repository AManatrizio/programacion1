from flask_restful import Resource
from flask import request
from .usuario import USUARIOS, Usuario

NOTIFICACIONES = {
    1:{'notificacion': 'Prestamo vencido',
       'usuario': '2'}
}

class Notificaciones(Resource):
    def post(self):
        notificacion = request.get_json()
        id = int(max(NOTIFICACIONES.keys())) + 1
        NOTIFICACIONES[int(id)] = notificacion
        return 'Notificacion: ', NOTIFICACIONES[int(id)], 'enviada.', 201
    
    def get(self):
        return NOTIFICACIONES
