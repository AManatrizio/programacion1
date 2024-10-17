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
    # USUARIO ACCEDE AL GET, ADMINISTRADOR TAMBIEN PERO INFO MAS REDUCIDA. Pero opcional porque no logueado tambien puede ver
    @jwt_required(optional=True)
    def get(self, id):
        self.id = id
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            # get_jwt_identity() es el id del token que sera el del usuario
            current_identity = get_jwt_identity()

            # Comparo el id que se pide con el id perteneciente al token
            if current_identity == id:
                return usuario.to_json()
            else:
                return usuario.to_json_short()  # Si no existe token, mostrar solo datos relevantes
        except Exception:
            abort(404, message=str("Error 404: el id del usuario no existe"))

    # En token viene un rol que debe ser alguno de los dos, para poder borrar
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
    @role_required(roles=["admin"])
    def get(self):
        page = 1
        per_page = 6
        usuarios = db.session.query(UsuarioModel)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # Filtrar por ID
        if request.args.get('id'):
            usuario_id = request.args.get('id')
            usuarios = usuarios.filter(UsuarioModel.id == usuario_id)

        # Filtrar por email
        if request.args.get('email'):
            email = request.args.get('email')
            usuarios = usuarios.filter(UsuarioModel.email == email)

        # Filtrar por teléfono
        if request.args.get('telefono'):
            telefono = request.args.get('telefono')
            usuarios = usuarios.filter(UsuarioModel.telefono == telefono)

        usuarios = usuarios.paginate(
            page=page, per_page=per_page, error_out=True)

        return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios],
                        'total': usuarios.total,
                        'pages': usuarios.pages,
                        'page': page
                        })
