from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity
from main.auth.decorators import role_required
from flask_restful import Resource, abort
from flask import request, jsonify, Blueprint
from main.models import PrestamoModel, LibroModel, UsuarioModel
from .. import db


class IdEnUso(Exception):
    ...


class LibroNoDisponible(Exception):
    ...


class Prestamo(Resource):
    @role_required(roles=["librarian", "admin"])
    def get(self, id):
        try:
            prestamo = db.session.query(PrestamoModel).get_or_404(id)
            id_usuario = prestamo.usuario_id
            current_identity = get_jwt_identity()

            claims = get_jwt()
            user_roles = claims.get('rol', [])

            if current_identity == id_usuario or "admin" in user_roles:
                return jsonify(prestamo.to_json())
            else:
                return jsonify(prestamo.to_json_short())
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @role_required(roles=["librarian", "admin"])
    def delete(self, id):
        try:
            prestamo = db.session.query(PrestamoModel).get_or_404(id)
            db.session.delete(prestamo)
            db.session.commit()
            return 'El prestamo fue borrado de manera satisfactoria', 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(
                "404 Not Found: No se encuentra el prestamo para eliminar. El ID no existe"))

    @role_required(roles=['admin', "librarian"])
    def put(self, id):
        try:
            prestamo = db.session.query(PrestamoModel).get_or_404(id)

            data = request.get_json()

            libro_id = data.get('libro_id')
            if not db.session.query(LibroModel).get(libro_id):
                abort(
                    404, message="Error 404: El libro con el ID proporcionado no existe")

            usuario_id = data.get('usuario_id')
            if not db.session.query(UsuarioModel).get(usuario_id):
                abort(
                    404, message="Error 404: El usuario con el ID proporcionado no existe")

            for key, value in data.items():
                setattr(prestamo, key, value)

            db.session.add(prestamo)
            db.session.commit()

            return prestamo.to_json(), 201

        except Exception as e:
            db.session.rollback()
            abort(500, message=str(e))


class Prestamos(Resource):
    @role_required(['admin', "user", "librarian"])
    def get(self):
        page = 1
        per_page = 5
        prestamos = db.session.query(PrestamoModel)
        current_identity = get_jwt_identity()
        user_rol = get_jwt()['rol']

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # if request.args.get('prestamo'):
        #     prestamo = request.args.get('prestamo')
        #     prestamos = prestamos.filter(PrestamoModel.prestamo == prestamo)

        if request.args.get('prestamo'):
            prestamos = prestamos.filter(PrestamoModel.prestamo.like(
                "%"+request.args.get('prestamo')+"%"))

        # if request.args.get('id'):
        #     prestamos = prestamos.filter(PrestamoModel.prestamo.like(
        #         "%"+request.args.get('id')+"%"))

        if (user_rol == 'admin' or user_rol == 'librarian'):
            prestamos = prestamos.paginate(
                page=page, per_page=per_page, error_out=True)
        else:
            prestamos = prestamos.filter(
                PrestamoModel.usuario_id == current_identity)
            prestamos = prestamos.paginate(
                page=page, per_page=per_page, error_out=True)

        return jsonify({
            'prestamos': [{
                'id': prestamo.id,
                'prestamo': prestamo.prestamo,
                'fecha_inicio': prestamo.fecha_inicio,
                'fecha_vencimiento': prestamo.fecha_vencimiento,
                'usuario_nombre': prestamo.usuario.nombre,
                'libro_nombre': prestamo.libro.nombre
            } for prestamo in prestamos.items],
            'total': prestamos.total,
            'pages': prestamos.pages,
            'page': page
        })

    @role_required(roles=["librarian", "admin"])
    def post(self):
        data = request.get_json()
        if isinstance(data, dict):
            data = [data]
        prestamos_list = []
        for prestamo_data in data:
            prestamo = PrestamoModel.from_json(prestamo_data)
            try:
                tabla = PrestamoModel.query.all()
            except Exception as e:
                return {'error': str(e)}, 403
            db.session.add(prestamo)
            prestamos_list.append(prestamo)
        db.session.commit()
        prestamos_json = [prestamo.to_json() for prestamo in prestamos_list]
        return prestamos_json, 201
