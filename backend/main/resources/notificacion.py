from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import NotificacionModel

class Notificaciones(Resource):
    def get(self):
        notificaciones = db.session.query(NotificacionModel).all()
        notificaciones_json = [(notificacion.to_json()) for notificacion in notificaciones]
        return jsonify(notificaciones_json)
        
    def post(self):
        notificacion = NotificacionModel.from_json(request.get_json())
        db.session.add(notificacion)
        db.session.commit()
        return notificacion.to_json(), 201
