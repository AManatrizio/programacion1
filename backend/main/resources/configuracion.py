from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ConfiguracionModel

class Configuraciones(Resource):
    def get(self):
        configuraciones = db.session.query(ConfiguracionModel).all()
        configuraciones_json = [configuracion.to_json() for configuracion in configuraciones]
        return jsonify(configuraciones_json)
