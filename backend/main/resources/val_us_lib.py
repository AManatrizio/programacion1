from flask_restful import Resource
from flask import request, jsonify
from main.models import ValUsLibModel
from .. import db


class ValUsLib(Resource):
    def get(self):
        valoraciones = db.session.query(ValUsLibModel).all()
        valoraciones_json = [valoracion.to_json() for valoracion in valoraciones]
        return jsonify(valoraciones_json)
