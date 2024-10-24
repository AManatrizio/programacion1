from flask_jwt_extended import jwt_required, get_jwt_identity
from main.mail.functions import sendMail
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from .. import jwt
from sqlalchemy import func, desc
from main.auth.decorators import role_required
from flask_restful import Resource, abort
from flask import request
from main.models import UsuarioModel
from .. import db
from flask import jsonify


class IdEnUso(Exception):
    ...


class Usuario(Resource):
    @jwt_required()
    def get(self, id=None):
        if id is None:
            # Si no se proporciona un ID, devolver el perfil del usuario actual
            current_identity = get_jwt_identity()
            usuario = db.session.query(
                UsuarioModel).get_or_404(current_identity)
            return usuario.to_json(), 200

        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            current_identity = get_jwt_identity()

            # Si el usuario autenticado es el mismo que el solicitado
            if current_identity == id:
                return usuario.to_json()
            else:
                return usuario.to_json_short()  # Si no es el mismo, mostrar solo info básica
        except Exception:
            abort(404, message=str("Error 404: el id del usuario no existe"))

    @role_required(roles=["users", "admin"])
    def delete(self, id):
        self.id = id
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            current_identity = get_jwt_identity()
            # Obtener claims de adentro del JWT
            claims = get_jwt()
            if claims["rol"] == "admin" or current_identity == id:
                db.session.delete(usuario)
                db.session.commit()
                send = sendMail([usuario.email], "Usuario borrado",
                                "usuario_borrado", usuario=usuario)
                return 'El usuario fue borrado de manera satisfactoria', 201

            else:
                return "Usted no posee la cuenta que quiere borrar", 404
        except Exception as e:
            db.session.rollback()
            abort(404, message=str(
                "404 Not Found: No se encuentra el usuario para eliminar. El ID no existe"))

    @jwt_required()
    def put(self, id):
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            data = request.get_json().items()
            for key, value in data:
                setattr(usuario, key, value)
            db.session.add(usuario)
            db.session.commit()
            return usuario.to_json(), 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str(
                "Error 404 NOt Found: No se encuentra el usuario para modificar"))


class Usuarios(Resource):
    @role_required(roles=["admin", "librarian"])
    def get(self):
        page = 1
        per_page = 5
        usuarios = db.session.query(UsuarioModel)

        # Obtener el ID del usuario autenticado y su rol
        current_identity = get_jwt_identity()
        user_rol = get_jwt()['rol']

        # Leer parámetros de paginado
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # Aplicar filtros (ID, email, teléfono)
        if request.args.get('id'):
            usuario_id = request.args.get('id')
            usuarios = usuarios.filter(UsuarioModel.id == usuario_id)

        if request.args.get('email'):
            email = request.args.get('email')
            usuarios = usuarios.filter(UsuarioModel.email.ilike(f"%{email}%"))

        if request.args.get('telefono'):
            telefono = request.args.get('telefono')
            usuarios = usuarios.filter(
                UsuarioModel.telefono.ilike(f"%{telefono}%"))

        # Check if there is a request to get all users
        if request.args.get('all') == 'true':
            # Return all users without pagination
            usuarios = usuarios.all()
            return jsonify({
                'usuarios': [usuario.to_json() for usuario in usuarios],
                'total': len(usuarios)
            })
        else:
            # Paginación después de aplicar los filtros
            usuarios = usuarios.paginate(
                page=page, per_page=per_page, error_out=False)

            return jsonify({
                'usuarios': [usuario.to_json() for usuario in usuarios.items],
                'total': usuarios.total,
                'pages': usuarios.pages,
                'page': page
            })
