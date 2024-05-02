from flask_restful import Resource, abort
from flask import request, jsonify
from main.models import LibroModel, AutorModel
from .. import db
from .exception import IdEnUso
from sqlalchemy import func, desc, asc

class Libro(Resource):
    def get(self, id):
        try:
            libro = db.session.query(LibroModel).get_or_404(id)
            return libro.to_json()
        except Exception as e:
            abort(404, message=str("Error 404 Not Found: No se encuentra el ID del libro."))
    
    def delete(self, id):
        try:
            libro = db.session.query(LibroModel).get_or_404(id)
            db.session.delete(libro)
            db.session.commit()
            return 'El libro fue borrado satisfactoriamente', 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str("404 Not Found: No se encuentra el libro para eliminar. El ID no existe"))
      

    def put(self, id):
        try:
            libro = db.session.query(LibroModel).get_or_404(id)
            data = request.get_json().items()
            for key , value in data:
                setattr(libro, key, value)
            db.session.add(libro)
            db.session.commit()
            return libro.to_json(), 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str("Error 404 Not Found: No se encuentra el libro para modificar"))

class Libros(Resource):
    def get(self):
        page = 1
        per_page = 10
        libros = db.session.query(LibroModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
            

        
        libros = libros.paginate(page=page, per_page=per_page, error_out=True)
        
        return jsonify({'libros': [libro.to_json() for libro in libros],
                  'total': libros.total,
                  'pages': libros.pages,
                  'page': page
                })    
        
    def post(self):
        libro = LibroModel.from_json(request.get_json())
        print(libro)
        try:
            db.session.add(libro)
            db.session.commit()
        except:
            return 'Formato no correcto', 400
        return libro.to_json(), 201   

    # def post(self):
    #     data = request.get_json()
    #     if isinstance(data, dict):
    #         data = [data]
    #     libros = []
    #     for libro_data in data:
    #         libros = LibroModel.from_json(libro_data)
    #         try:
    #             tabla = LibroModel.query.all()
    #             self.verificacion(libro_data, tabla)
    #         except Exception as e:
    #             return {'error': str(e)}, 403
    #         db.session.add(libros)
    #         libros.append(libros)
    #     db.session.commit()
    #     libros_json = [libro.to_json() for libro in libros]
    #     return libros_json, 201

    # def verificacion(self, libro, tabla):
    #     for i in tabla:
    #         id_libro = i.id
    #         id_libro_nuevo = libro['id']
    #         if id_libro == id_libro_nuevo:
    #             raise IdEnUso('El ID esta en uso')