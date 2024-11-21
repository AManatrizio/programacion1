from flask_restful import Resource, abort
from flask import request, jsonify
from main.models import OpinionModel, PrestamoModel
from .exception import IdEnUso
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required


class Opinion(Resource):
    @jwt_required(optional=True)
    def get(self, prestamo_id):
        try:
            print(f"Solicitando opinión para préstamo ID: {prestamo_id}")
            opinion = db.session.query(OpinionModel).filter_by(
                prestamo_id=prestamo_id).first_or_404()
            return opinion.to_json()
        except Exception as e:
            print(f"Error al obtener la opinión: {str(e)}")
            abort(
                500, message="Error 404: No se encontró la opinión asociada al préstamo.")

    @role_required(["admin"])
    def delete(self, id):
        try:
            opinion = db.session.query(OpinionModel).get_or_404(id)
            current_identity = get_jwt_identity()
            if current_identity == id:
                db.session.delete(opinion)
                db.session.commit()
                return 'La opinion fue borrada de manera satisfactoria', 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(
                "404 Not Found: No se encuentra la opinion para eliminar. El ID no existe"))

    @role_required(['user'])
    def put(self, prestamo_id):
        try:
            opinion = db.session.query(OpinionModel).filter_by(
                prestamo_id=prestamo_id).first_or_404()
            data = request.get_json()
            print(f"Datos recibidos: {data}")

            if 'comentario' in data:
                opinion.comentario = data['comentario']
            if 'valoracion' in data:
                opinion.valoracion = int(data['valoracion'])

            db.session.add(opinion)
            db.session.commit()
            return opinion.to_json(), 201

        except Exception as e:
            db.session.rollback()
            print(f"Error al procesar PUT: {str(e)}")
            abort(500, message="Error interno del servidor")


class Opiniones(Resource):
    @jwt_required(optional=True)
    def get(self):
        page = 1
        per_page = 5
        opiniones = db.session.query(OpinionModel)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        if request.args.get('valoracion'):
            cant_ast = int(request.args.get('valoracion'))
            valoracion_a_buscar = '*' * cant_ast
            opiniones = opiniones.filter(
                OpinionModel.valoracion == valoracion_a_buscar)

        opiniones = opiniones.paginate(
            page=page, per_page=per_page, error_out=True)

        return jsonify({'opiniones': [opinion.to_json() for opinion in opiniones],
                        'total': opiniones.total,
                        'pages': opiniones.pages,
                        'page': page
                        })

    @role_required(['user'])
    def post(self, prestamo_id):
        data = request.get_json()

        if 'comentario' not in data or 'valoracion' not in data:
            return {'error': 'Faltan campos obligatorios (comentario, valoracion).'}, 400

        usuario_id = get_jwt_identity()

        prestamo = PrestamoModel.query.get_or_404(prestamo_id)

        if prestamo.usuario_id != usuario_id:
            return {'error': 'No puedes emitir una opinión sobre un préstamo que no te pertenece.'}, 403

        if prestamo.opinion:
            return {'message': 'Este préstamo ya tiene una opinión asociada.'}, 400

        opinion = OpinionModel.from_json(data)
        opinion.prestamo_id = prestamo_id
        db.session.add(opinion)
        db.session.commit()

        return opinion.to_json(), 201
