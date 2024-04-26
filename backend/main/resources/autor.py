from flask_restful import Resource, abort
from flask import request, jsonify
from main.models import AutorModel
from main.models import LibroModel
from .. import db

class Autor(Resource):
    def get(self, id):
        try:
            autor = db.session.query(AutorModel).get_or_404(id)
            return autor.to_json()
        except Exception as e:
            abort(404, message=str("Error 404 Not Found: No se encuentra el ID del autor."))
    
    
    def delete(self, id):
        try:
            autor = db.session.query(AutorModel).get_or_404(id)
            db.session.delete(autor)
            db.session.commit()
            return 'El autor fue borrado satisfactoriamente', 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str("404 Not Found: No se encuentra el autor para eliminar. El ID no existe"))
    
      
    
    def put(self, id):
        try:
            autor = db.session.query(AutorModel).get_or_404(id)
            data = request.get_json().items()
            for key , value in data:
                setattr(autor, key, value)
            db.session.add(autor)
            db.session.commit()
            return autor.to_json(), 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str("Error 404 Not Found: No se encuentra el autor para modificar"))
   


class Autores(Resource):
    def get(self):
        autores = db.session.query(AutorModel).all()
        autores_json = [(autor.to_json()) for autor in autores]
        return jsonify(autores_json)
    
    
    def post(self):
        id_libro = request.get_json().get('libro')
        autor = AutorModel.from_json(request.get_json())
        
        if id_libro:
            libro = LibroModel.query.filter(LibroModel.id.in_(id_libro)).all()
            autor.libro.extend(libro)
            
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201
    
    
