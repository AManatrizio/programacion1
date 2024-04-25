from flask_restful import Resource
from flask import request, jsonify
from main.models import LibroModel, AutorModel
from .. import db

class Libro(Resource):
    def get(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        return libro.to_json()
    
    def delete(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return 'El libro fue borrado satisfactoriamente', 201
    
    def put(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        data = request.get_json().items()
        for key , value in data:
            setattr(libro, key, value)
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201

class Libros(Resource):
    def get(self):
        libros = db.session.query(LibroModel).all()
        libros_json = [(libro.to_json()) for libro in libros]
        return jsonify(libros_json)
        
    def post(self):
        id_autores = request.get_json().get('autor')
        libro = LibroModel.from_json(request.get_json())
        
        if id_autores:
            autor = AutorModel.query.filter(AutorModel.id.in_(id_autores)).all()
            libro.autor.extend(autor)
            
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201
    
