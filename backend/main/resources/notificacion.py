from flask_restful import Resource, abort
from flask import request, jsonify
from .. import db
from main.models import NotificacionModel

class Notificaciones(Resource):
    def get(self):
            page = 1
            per_page = 10
            notificaciones = db.session.query(NotificacionModel)
            
            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))   
            
            notificaciones = notificaciones.paginate(page=page, per_page=per_page, error_out=True)
            
            return jsonify({'notificaciones': [notificacion.to_json() for notificacion in notificaciones],
                    'total': notificaciones.total,
                    'pages': notificaciones.pages,
                    'page': page
                    })

                
                
    def post(self):
        notificacion = NotificacionModel.from_json(request.get_json())
        db.session.add(notificacion)
        db.session.commit()
        return notificacion.to_json(), 201