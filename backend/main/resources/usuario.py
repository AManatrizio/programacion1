from flask_jwt_extended import jwt_required, get_jwt_identity
from main.mail.functions import sendMail
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from .. import jwt
from sqlalchemy import func, desc
from main.auth.decorators import role_required
from flask_restful import Resource, abort
from flask import Blueprint, request
from main.models import UsuarioModel
from .. import db
from flask import jsonify


class IdEnUso(Exception):
    ...


class Usuario(Resource):
    @jwt_required()
    @role_required(roles=["librarian", "admin"])
    def get(self, id):
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            id_usuario = usuario.id
            current_identity = get_jwt_identity()

            claims = get_jwt()
            user_roles = claims.get('rol', [])

            if current_identity == id_usuario or "admin" in user_roles or "librarian" in user_roles:
                return jsonify(usuario.to_json_complete())
            else:
                return "No se puede visualizar el usuario solicitado", 404
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @role_required(roles=["librarian", "admin"])
    def delete(self, id):
        self.id = id
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            current_identity = get_jwt_identity()
            claims = get_jwt()
            if claims["rol"] == "admin" or claims["rol"] == "librarian":
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

    @role_required(roles=["librarian", "admin"])
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

        current_identity = get_jwt_identity()
        user_rol = get_jwt()['rol']

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        if request.args.get('id'):
            usuario_id = request.args.get('id')
            usuarios = usuarios.filter(UsuarioModel.id == usuario_id)

        if request.args.get('nombre'):
            usuarios = usuarios.filter(UsuarioModel.nombre.like(
                "%"+request.args.get('nombre')+"%"))

        if request.args.get('rol'):
            usuarios = usuarios.filter(UsuarioModel.rol.like(
                "%"+request.args.get('rol')+"%"))

        if request.args.get('all') == 'true':
            usuarios = usuarios.all()
            return jsonify({
                'usuarios': [usuario.to_json() for usuario in usuarios],
                'total': len(usuarios)
            })
        else:
            usuarios = usuarios.paginate(
                page=page, per_page=per_page, error_out=False)

            return jsonify({
                'usuarios': [usuario.to_json() for usuario in usuarios.items],
                'total': usuarios.total,
                'pages': usuarios.pages,
                'page': page
            })


class UsuarioProfile(Resource):
    @jwt_required()
    def get(self, id=None):
        if id is None:
            current_identity = get_jwt_identity()
            usuario = db.session.query(
                UsuarioModel).get_or_404(current_identity)
            return usuario.to_json(), 200

        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            current_identity = get_jwt_identity()

            if current_identity == id:
                return usuario.to_json_complete()
            else:
                return usuario.to_json_short()
        except Exception:
            abort(404, message=str("Error 404: el id del usuario no existe"))
