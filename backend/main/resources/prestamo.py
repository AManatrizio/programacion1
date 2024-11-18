from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity
from main.auth.decorators import role_required
from flask_restful import Resource, abort
from flask import request, jsonify, Blueprint
from main.models import PrestamoModel, LibroModel, UsuarioModel, StockModel
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

            if current_identity == id_usuario or "admin" in user_roles or "librarian" in user_roles:
                return jsonify(prestamo.to_json())
            else:
                return jsonify(prestamo.to_json_short())
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @role_required(roles=["librarian", "admin"])
    def delete(self, id):
        try:
            prestamo = db.session.query(PrestamoModel).get_or_404(id)

            # Recuperar el stock del libro asociado y aumentar la cantidad
            stock = db.session.query(StockModel).filter_by(
                libro_id=prestamo.libro_id).first()
            if stock:
                stock.cantidad += 1

            db.session.delete(prestamo)
            db.session.commit()
            return 'El préstamo fue borrado de manera satisfactoria', 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=str("Error al eliminar el préstamo: " + str(e)))

    @role_required(roles=['admin', "librarian"])
    def put(self, id):
        try:
            prestamo = db.session.query(PrestamoModel).get_or_404(id)
            estado_anterior = prestamo.estado
            data = request.get_json()
            nuevo_estado = data.get('estado')

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

            if estado_anterior == "En uso" and nuevo_estado == "Finalizado":
                stock = db.session.query(StockModel).filter_by(
                    libro_id=prestamo.libro_id).first()
                if stock:
                    stock.cantidad = stock.cantidad + 1
                    db.session.add(stock)

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
        per_page = 4
        prestamos = db.session.query(PrestamoModel)
        current_identity = get_jwt_identity()
        user_rol = get_jwt()['rol']

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        if request.args.get('estado'):
            prestamos = prestamos.filter(PrestamoModel.estado.like(
                "%"+request.args.get('estado')+"%"))

        if request.args.get('id'):
            prestamo_id = request.args.get('id')
            prestamos = prestamos.filter(PrestamoModel.id == prestamo_id)

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
                'estado': prestamo.estado,
                'fecha_inicio': prestamo.fecha_inicio,
                'fecha_vencimiento': prestamo.fecha_vencimiento,
                'usuario_nombre_completo': prestamo.usuario.nombre_completo,
                'libro_nombre': prestamo.libro.nombre
            } for prestamo in prestamos.items],
            'total': prestamos.total,
            'pages': prestamos.pages,
            'page': page
        })

    @role_required(['admin', "user", "librarian"])
    def post(self):
        try:
            data = request.get_json()
            libro_id = data.get('libro_id')
            if not db.session.query(LibroModel).get(libro_id):
                abort(404, message="El libro con el ID proporcionado no existe")

            # Verificar si hay stock disponible
            stock = db.session.query(StockModel).filter_by(
                libro_id=libro_id).first()
            if not stock or stock.cantidad <= 0:
                raise LibroNoDisponible(
                    "No hay stock disponible para el libro solicitado")

            # Crear el préstamo
            nuevo_prestamo = PrestamoModel.from_json(data)
            db.session.add(nuevo_prestamo)

            # Reducir el stock en 1
            stock.cantidad -= 1
            db.session.commit()

            return nuevo_prestamo.to_json(), 201
        except LibroNoDisponible as e:
            return {'message': str(e)}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
