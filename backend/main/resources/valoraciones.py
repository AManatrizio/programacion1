from flask_restful import Resource
from flask import request, jsonify
from main.models import ValoracionModel
from .. import db

class Valoracion(Resource):
    def get(self, id):
        valoracion = db.session.query(ValoracionModel).get_or_404(id)
        return valoracion.to_json()
    
    def delete(self, id):
        valoracion = db.session.query(ValoracionModel).get_or_404(id)
        db.session.delete(valoracion)
        db.session.commit()
        return '', 201


class Valoraciones(Resource):
    def get(self):
        valoraciones = db.session.query(ValoracionModel).all()
        valoraciones_json = [(valoracion.to_json()) for valoracion in valoraciones]
        return jsonify(valoraciones_json)

    def post(self):
        valoracion = ValoracionModel.from_json(request.get_json())
        db.session.add(valoracion)
        db.session.commit()
        return valoracion.to_json(), 201



