from flask_restful import Resource, abort
from flask import request, jsonify
from main.models import LibroModel, AutorModel
from .. import db
from .exception import IdEnUso
from flask_jwt_extended import jwt_required
from main.auth.decorators import role_required
from sqlalchemy import func
from flask import request, jsonify, Blueprint
from .. import db


auth = Blueprint('/libros', __name__, url_prefix='/libros')


class Libro(Resource):
    @role_required(roles=['admin', 'user', "librarian"])
    def get(self, id):
        try:
            libro = db.session.query(LibroModel).get_or_404(id)
            return libro.to_json()
        except Exception as e:
            abort(404, message=str(
                "Error 404 Not Found: No se encuentra el ID del libro."))

    @role_required(roles=['admin', "librarian"])
    def delete(self, id):
        try:
            libro = db.session.query(LibroModel).get_or_404(id)
            db.session.delete(libro)
            db.session.commit()
            return 'El libro fue borrado satisfactoriamente', 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str(
                "404 Not Found: No se encuentra el libro para eliminar. El ID no existe"))

    @role_required(roles=['admin', "librarian"])
    def put(self, id):
        try:
            libro = db.session.query(LibroModel).get_or_404(id)
            data = request.get_json().items()
            for key, value in data:
                setattr(libro, key, value)
            db.session.add(libro)
            db.session.commit()
            return libro.to_json(), 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str(
                "Error 404 Not Found: No se encuentra el libro para modificar"))


class Libros(Resource):
    @jwt_required(optional=True)
    def get(self):
        page = 1
        per_page = 5
        libros = db.session.query(LibroModel)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        if request.args.get('genero'):
            libros = libros.filter(LibroModel.genero.like(
                "%"+request.args.get('genero')+"%"))

        if request.args.get('nombre'):
            libros = libros.filter(LibroModel.nombre.like(
                "%"+request.args.get('nombre')+"%"))

        if request.args.get('sortby_autor'):
            libros = libros.join(LibroModel.autores).\
                group_by(LibroModel.id).\
                order_by(func.group_concat(AutorModel.autor).desc())

        if request.args.get('autores'):
            autor_id = request.args.get('autores')
            libros = libros.filter(
                LibroModel.autores.any(AutorModel.id == autor_id))

        libros = libros.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'libros': [libro.to_json() for libro in libros],
                        'total': libros.total,
                        'pages': libros.pages,
                        'page': page
                        })

    @auth.route('/addbooks', methods=['POST'])
    @role_required(roles=["librarian", "admin"])
    def post(self):
        data = request.get_json()
        libros_list = []

        if isinstance(data, dict):
            data = [data]

        for libro_data in data:
            libros = LibroModel.from_json(libro_data)
            try:
                tabla = LibroModel.query.all()
            except Exception as e:
                return {'error': str(e)}, 403

            db.session.add(libros)
            libros_list.append(libros)

        db.session.commit()
        libros_json = [libro.to_json() for libro in libros_list]
        return libros_json, 201
