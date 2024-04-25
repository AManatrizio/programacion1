from flask_restful import Resource
from flask import request, jsonify
from main.models import AutorModel
from main.models import LibroModel
from .. import db

class Autor(Resource):
    def get(self, id):
        autor = db.session.query(AutorModel).get_or_404(id)
        return autor.to_json()
    
    def delete(self, id):
        autor = db.session.query(AutorModel).get_or_404(id)
        db.session.delete(autor)
        db.session.commit()
        return 'El autor fue borrado satisfactoriamente', 201
    
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
        autores_json = [(autor.to_json()) for autor in autores]
        return jsonify(autores_json)
        
    
    def post(self):
        autor = AutorModel.from_json(request.get_json())
        print(autor)
        try:
            db.session.add(autor)
            db.session.commit()
        except:
            return 'Formato no correcto', 400
        return autor.to_json(), 201   
    
    
    
