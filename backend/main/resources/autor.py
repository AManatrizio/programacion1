from flask_restful import Resource
from flask import request
from main.models import AutorModel
from .. import db
from flask import jsonify

class Autor(Resource):
    def get(self, id):
        autor = db.session.query(AutorModel).get_or_404(id)
        return autor.to_json()
    
    def delete(self, id):
        autor = db.session.query(AutorModel).get_or_404(id)
        db.session.delete(autor)
        db.session.commit()
        return '', 201
    
    def put(self, id):
        autor = db.session.query(AutorModel).get_or_404(id)
        data = request.get_json().items()
        for key , value in data:
            setattr(autor, key, value)
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201

class Autores(Resource):
    def get(self):
        autores = db.session.query(AutorModel).all()
        autores_json = [autor.to_json() for autor in autores]
        return jsonify(autores_json)
        
    def post(self):
        autor = AutorModel.from_json(request.get_json())
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201