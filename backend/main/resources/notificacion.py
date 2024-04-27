from flask_restful import Resource, abort
from flask import request, jsonify
from .. import db
from main.models import NotificacionModel

class Notificaciones(Resource):
    def get(self):
        try:
            notificaciones = db.session.query(NotificacionModel).all()
            notificaciones_json = [(notificacion.to_json()) for notificacion in notificaciones]
            return jsonify(notificaciones_json)
        except Exception as e:
            abort(404, message=str("Error 404 Not Found: No se encuentra el ID de la notificacion."))
                
                
    def post(self):
        notificacion = NotificacionModel.from_json(request.get_json())
        db.session.add(notificacion)
        db.session.commit()
        return notificacion.to_json(), 201