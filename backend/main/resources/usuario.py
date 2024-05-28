from flask_restful import Resource, abort
from flask import request
from main.models import UsuarioModel
from .. import db
from flask import jsonify
class IdEnUso(Exception):
    ...
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required
from sqlalchemy import func, desc

class Usuario(Resource):
    @jwt_required(optional=True) #USUARIO ACCEDE AL GET, ADMINISTRADOR TAMBIEN PERO INFO MAS REDUCIDA
    def get(self, id):
        try:          
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            current_identity = get_jwt_identity() #get_jwt_identity() es el id del token que sera el del usuario
           
            #Si el token existe, implica que el rol es usuario, asi que mostrar todos sus datos
            if current_identity:                    
                return usuario.to_json()
            else:
                return usuario.to_json_short() #Si no existe token, mostrar solo datos relevantes
        except Exception:
            abort(404, message=str("Error 404: el id del usuario no existe"))
    
    
    @role_required(roles = ["admin","users"]) #En token viene un rol que debe ser alguno de los dos, para poder borrar
    def delete(self, id):
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            db.session.delete(usuario)
            db.session.commit()
            return 'El usuario fue borrado de manera satisfactoria', 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str("404 Not Found: No se encuentra el usuario para eliminar. El ID no existe"))
    
    @jwt_required()    
    def put(self, id):
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            data = request.get_json().items()
            for key , value in data:
                setattr(usuario, key, value)
            db.session.add(usuario)
            db.session.commit()
            return usuario.to_json(), 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str("Error 404 NOt Found: No se encuentra el usuario para modificar"))



class Usuarios(Resource):
    
    @role_required(roles = ["admin"])    
    def get(self):
        page = 1
        per_page = 10
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
        
        usuarios = usuarios.paginate(page=page, per_page=per_page, error_out=True)
        
        return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios],
                  'total': usuarios.total,
                  'pages': usuarios.pages,
                  'page': page
                })