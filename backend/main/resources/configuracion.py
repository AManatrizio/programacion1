from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ConfiguracionModel

class Configuraciones(Resource):
    def get(self):
        page = 1
        per_page = 10
        configuraciones = db.session.query(ConfiguracionModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))   
        
        configuraciones = configuraciones.paginate(page=page, per_page=per_page, error_out=True)
        
        return jsonify({'configuraciones': [configuracion.to_json() for configuracion in configuraciones],
                  'total': configuraciones.total,
                  'pages': configuraciones.pages,
                  'page': page
                })