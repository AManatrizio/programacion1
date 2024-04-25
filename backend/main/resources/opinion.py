from flask_restful import Resource
from flask import request, jsonify
from main.models import OpinionModel
from .. import db

class Opinion(Resource):
    def get(self, id):
        opinion = db.session.query(OpinionModel).get_or_404(id)
        return opinion.to_json()
    
    def delete(self, id):
        opinion = db.session.query(OpinionModel).get_or_404(id)
        db.session.delete(opinion)
        db.session.commit()
        return '', 201

    def put(self, id):
        opinion = db.session.query(OpinionModel).get_or_404(id)
        data = request.get_json().items()
        for key , value in data:
            setattr(opinion, key, value)
        db.session.add(opinion)
        db.session.commit()
        return opinion.to_json(), 201


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