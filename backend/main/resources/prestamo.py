from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity
from main.auth.decorators import role_required
from flask_restful import Resource, abort
from flask import request, jsonify, Blueprint
from main.models import PrestamoModel
from .. import db

auth = Blueprint('/prestamos', __name__, url_prefix='/prestamos')
auth1 = Blueprint('/prestamo', __name__, url_prefix='/prestamo')


class IdEnUso(Exception):
    ...


class LibroNoDisponible(Exception):
    ...


class Prestamo(Resource):
    # Ver los prestamos puede hacerlo administrador y los usuarios solo logueados pueden ver todos los prestamos, pero con info menos detallada
    @role_required(roles=["admin", "user"])
    def get(self, id):
        try:
            prestamo = db.session.query(PrestamoModel).get_or_404(id)
            # Aca agarro columna de id usuario en tabla prestamo
            id_usuario = prestamo.usuario_id
            # get_jwt_identity() es el id del token que sera el del usuario
            current_identity = get_jwt_identity()
            if current_identity == id_usuario:
                return prestamo.to_json()  # Si es el propio usuario muestra completa la info
            else:
                # Si no existe token, mostrar solo datos de usuario id y libro id
                return prestamo.to_json_short()
        except Exception:
            abort(500, message=str("Error 404: el id del prestamo no existe"))

    @role_required(['admin'])
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

    @auth1.route('/editloans', methods=['PUT'])
    @role_required(['admin'])
    def put(self, id):
        try:
            prestamo = db.session.query(PrestamoModel).get_or_404(id)
            data = request.get_json().items()
            for key, value in data:
                setattr(prestamo, key, value)
            db.session.add(prestamo)
            db.session.commit()
            return prestamo.to_json(), 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(
                "Error 404 Not Found: No se encuentra el prestamo para modificar"))


class Prestamos(Resource):
    @role_required(['admin', "user", "bibliotecary"])
    def get(self):
        page = 1
        per_page = 5
        prestamos = db.session.query(PrestamoModel)
        current_identity = get_jwt_identity()  # Obtener el ID del usuario autenticado
        user_rol = get_jwt()['rol']  # Obtener el rol desde el token JWT

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # Filtros opcionales que ya tenías
        if request.args.get('prestamo'):
            prestamo = request.args.get('prestamo')
            prestamos = prestamos.filter(PrestamoModel.prestamo == prestamo)

        # Si el usuario es admin, mostrar todos los préstamos
        if (user_rol == 'admin' or user_rol == 'bibliotecary'):
            prestamos = prestamos.paginate(
                page=page, per_page=per_page, error_out=True)
        else:
            # Si es usuario, filtrar los préstamos para que solo vea los suyos
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
                'usuario_nombre': prestamo.usuario.nombre,  # Nombre del usuario
                'libro_nombre': prestamo.libro.nombre  # Nombre del libro
            } for prestamo in prestamos.items],
            'total': prestamos.total,
            'pages': prestamos.pages,
            'page': page
        })

    @auth.route('/addbooks', methods=['POST'])
    @role_required(['admin'])
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
