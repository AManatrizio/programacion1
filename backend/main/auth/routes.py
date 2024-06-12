from flask import request, jsonify, Blueprint
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from main.mail.functions import sendMail


#Blueprint para acceder a los métodos de autenticación
auth = Blueprint('auth', __name__, url_prefix='/auth')

#Método de logueo
@auth.route('/login', methods=['POST'])
def login():
    #Buscar el usuario en la db por su mail, para cortar si no existe
    usuario = db.session.query(UsuarioModel).filter(UsuarioModel.email == request.get_json().get("email")).first_or_404()
    #Valida la contraseña
    if usuario.validate_pass(request.get_json().get("password")):
        
        access_token = create_access_token(identity=usuario)#Genera un nuevo token y a usuario lo pasa como identidad

        #Crear variable con datos de logueo para mostrarlos
        data = {
            'id': str(usuario.id),
            'email': usuario.email,
            'access_token': access_token
        }
                    #Mail de bienvenida TO,       SUBJECT     TEMPLATE    ARGUMENTO
        send = sendMail([usuario.email], "Inicio de sesion", "sesion", usuario=usuario)
        return data, 200
    else:
        return 'La contraseña ingresada es incorrecta', 401

#Método de registro
@auth.route('/register', methods=['POST'])
def register():
    #Obtener el usuario
    usuario = UsuarioModel.from_json(request.get_json())
    
    #Verificar si el mail ya existe en la db, scalar() para saber la cantidad de veces que aparece ese email
    exists = db.session.query(UsuarioModel).filter(UsuarioModel.email == usuario.email).scalar() is not None
    if exists:
        return 'El mail ingresado, ya existe', 409
    else:
        try:
            #Agregar Usuario a las tablas de DB
            db.session.add(usuario)
            db.session.commit()
            #Mail de bienvenida TO,             SUBJECT     TEMPLATE    ARGUMENTO
            send = sendMail([usuario.email], "Mensaje de bienvenida", "register", usuario=usuario)
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return usuario.to_json() , 201