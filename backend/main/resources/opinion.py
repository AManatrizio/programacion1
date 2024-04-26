from flask_restful import Resource, abort
from flask import request, jsonify
from main.models import OpinionModel
from .. import db
class IdEnUso(Exception):
    ...

class LibroNoDisponible(Exception):
    ...


class Opinion(Resource):
    def get(self, id):
        try:
            opinion = db.session.query(OpinionModel).get_or_404(id)
            return opinion.to_json()
        except Exception:
            abort(500, message=str("Error 404: el id de la opinion no existe"))
    
    def delete(self, id):
        try:
            opinion = db.session.query(OpinionModel).get_or_404(id)
            db.session.delete(opinion)
            db.session.commit()
            return 'La opinion fue borrada de manera satisfactoria', 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=str("404 Not Found: No se encuentra la opinion para eliminar. El ID no existe"))
    
    
    def put(self, id):
        try:
            opinion = db.session.query(OpinionModel).get_or_404(id)
            data = request.get_json().items()
            for key , value in data:
                setattr(opinion, key, value)
            db.session.add(opinion)
            db.session.commit()
            return opinion.to_json(), 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=str("Error 404 Not Found: No se encuentra la opinion para modificar"))
  


class Opiniones(Resource):
    def get(self):
        opiniones = db.session.query(OpinionModel).all()
        opiniones_json = [(opinion.to_json()) for opinion in opiniones]
        return jsonify(opiniones_json)

    def post(self):
        opinion = OpinionModel.from_json(request.get_json())
        db.session.add(opinion)
        db.session.commit()
        return opinion.to_json(), 201
    
    
    
        