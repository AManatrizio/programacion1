from flask_restful import Resource, abort
from flask import request, jsonify
from main.models import AutorModel
from main.models import LibroModel
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required


class Autor(Resource):
    @jwt_required(optional=True)
    def get(self, id):
        try:
            autor = db.session.query(AutorModel).get_or_404(id)
            return autor.to_json()
        except Exception as e:
            abort(404, message=str("Error 404 Not Found: No se encuentra el ID del autor."))
    
    @role_required(['admin'])        
    def delete(self, id):
        try:
            autor = db.session.query(AutorModel).get_or_404(id)
            db.session.delete(autor)
            db.session.commit()
            return 'El autor fue borrado satisfactoriamente', 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str("404 Not Found: No se encuentra el autor para eliminar. El ID no existe"))    
    
    @role_required(['admin'])        
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
    @jwt_required(optional=True)
    def get(self):
        page = 1
        per_page = 10
        autores = db.session.query(AutorModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        autores = autores.paginate(page=page, per_page=per_page, error_out=True)
        return jsonify({'autores': [autor.to_json() for autor in autores],
                  'total': autores.total,
                  'pages': autores.pages,
                  'page': page
                })
    
    @role_required(['admin'])        
    def post(self):
        id_libro = request.get_json().get('libro')
        autor = AutorModel.from_json(request.get_json())
        
        if id_libro:
            libro = LibroModel.query.filter(LibroModel.id.in_(id_libro)).all()
            autor.libro.extend(libro)
            
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201
    