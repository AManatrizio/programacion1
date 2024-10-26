from flask import request, jsonify, Blueprint
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from main.mail.functions import sendMail


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login():
    usuario = db.session.query(UsuarioModel).filter(
        UsuarioModel.email == request.get_json().get("email")).first_or_404()
    if usuario.validate_pass(request.get_json().get("password")):

        access_token = create_access_token(identity=usuario)

        data = {
            'id': str(usuario.id),
            'email': usuario.email,
            'access_token': access_token
        }
        send = sendMail([usuario.email], "Inicio de sesion",
                        "sesion", usuario=usuario)
        return data, 200
    else:
        return 'La contraseña ingresada es incorrecta', 401


@auth.route('/register', methods=['POST'])
def register():
    usuario = UsuarioModel.from_json(request.get_json())

    exists = db.session.query(UsuarioModel).filter(
        UsuarioModel.email == usuario.email).scalar() is not None

    if exists:
        return 'El mail ingresado, ya existe', 409
    else:
        try:

            db.session.add(usuario)
            db.session.commit()

            sendMail(
                [usuario.email], "Mensaje de bienvenida", "register", usuario=usuario)

        except Exception as error:
            db.session.rollback()
            return str(error), 409

        return usuario.to_json(), 201
