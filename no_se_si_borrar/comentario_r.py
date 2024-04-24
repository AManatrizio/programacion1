from flask_restful import Resource
from flask import request, jsonify
from main.models import ComentarioModel
from ..backend.main import db

class Comentario(Resource):
    def get(self, id):
        comentario = db.session.query(ComentarioModel).get_or_404(id)
        return comentario.to_json()
    
    def delete(self, id):
        comentario = db.session.query(ComentarioModel).get_or_404(id)
        db.session.delete(comentario)
        db.session.commit()
        return '', 201

    def put(self, id):
        comentario = db.session.query(ComentarioModel).get_or_404(id)
        data = request.get_json().items()
        for key , value in data:
            setattr(comentario, key, value)
        db.session.add(comentario)
        db.session.commit()
        return comentario.to_json(), 201


class Comentarios(Resource):
    def get(self):
        comentarios = db.session.query(ComentarioModel).all()
        comentarios_json = [(comentario.to_json()) for comentario in comentarios]
        return jsonify(comentarios_json)

    def post(self):
        comentario = ComentarioModel.from_json(request.get_json())
        db.session.add(comentario)
        db.session.commit()
        return comentario.to_json(), 201

