from flask_restful import Resource
from flask import request
from .usuario import USUARIOS, Usuario

NOTIFICACIONES = {
    1:{'notificacion'}
}

class Notificaciones(Resource):
    def post(self, id_usuario):
        notificacion = request.get_json()
        id = int(max(NOTIFICACIONES.keys())) + 1
        NOTIFICACIONES[id] = notificacion
        USUARIOS[id_usuario][2] = notificacion
        return 'Notificacion: ', NOTIFICACIONES[id], 'enviada.', 201
    
    def get(self):
        return NOTIFICACIONES
