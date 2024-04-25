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
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201
    
    # def post(self):
    #     libro_ids = request.get_json().get('libro')
    #     autor = AutorModel.from_json(request.get_json())
        
    #     if libro_ids:
    #         # Obtener las instancias de Exhibicion basadas en las ids recibidas
    #         libro = LibroModel.query.filter(LibroModel.id.in_(libro_ids)).all()
    #         # Agregar las instancias de Exhibicion a la lista de libro del autor
    #         autor.libro.extend(libro)
            
    #     db.session.add(autor)
    #     db.session.commit()
    #     return autor.to_json(), 201       