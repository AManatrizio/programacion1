from flask_restful import Resource, abort
from flask import request, jsonify
from main.models import OpinionModel, PrestamoModel
from .exception import IdEnUso
from .. import db

class Opinion(Resource):
    def get(self, id):
        try: 
            opinion = db.session.query(OpinionModel).get_or_404(id)
            return opinion.to_json()
        except Exception:
            abort(404, message=str("Error 404: No existen opiniones de este libro"))
    
    def delete(self, id):
        try:
            opinion = db.session.query(OpinionModel).get_or_404(id)
            db.session.delete(opinion)
            db.session.commit()
            return '', 201
        except Exception:
            abort(404, message=str("404 Not Found: No puede eliminar una opinion que no existe"))

    def put(self, id):
        try:
            opinion = db.session.query(OpinionModel).get_or_404(id)
            data = request.get_json().items()
            for key , value in data:
                setattr(opinion, key, value)
            db.session.add(opinion)
            db.session.commit()
            return opinion.to_json(), 201
        except Exception:
            abort(404, message=str("404 Not Found: No puede modificar una opinion que no existe"))


class Opiniones(Resource):
    def get(self):
        try: 
            opiniones = db.session.query(OpinionModel).all()
            opiniones_json = [(opinion.to_json()) for opinion in opiniones]
            return jsonify(opiniones_json)
        except Exception:
            abort(404, message=str("404 Not Found: No se encuentran opiniones"))

class Opiniones(Resource):
    def post(self):
        data = request.get_json()
        prestamo_id = data.get('prestamo_id')

        # Verificar si el prestamo_id existe en la base de datos de prestamos
        prestamo_existente = db.session.query(PrestamoModel).filter_by(id=prestamo_id).first()
        if not prestamo_existente:
            return {'error': 'No se puede crear la opinión, el prestamo con ese id no existe'}, 404

        opinion = OpinionModel.from_json(data)
        db.session.add(opinion)
        db.session.commit()
        return opinion.to_json(), 201

