<<<<<<< HEAD
from flask_restful import Resource
from flask import request

USUARIOS = {
    1: {
        "id": 1,
        "nombre": "Juan",
        "apellido": "Perez",
        "edad": 30
    },
    2: {
        "id": 2,
        "nombre": "María",
        "apellido": "González",
        "edad": 25
    },
    3: {
        "id": 3,
        "nombre": "Carlos",
        "apellido": "López",
        "edad": 35
    }
}

class Usuario(Resource):
    # Método para manejar solicitudes GET para un usuario específico
    def get(self, id):
        if id in USUARIOS:
            return USUARIOS[id]
        #si no existe
        return 'No existe el id', 404
    
    # Método para manejar solicitudes DELETE para un usuario específico
    def delete(self, id):
        if id in USUARIOS:
            del USUARIOS[id]
            return '', 204
        #si no existe
        return 'No existe el id', 404
    
    # Método para manejar solicitudes PUT para actualizar un usuario específico
    def put(self, id):
        if id in USUARIOS:
            usuario = USUARIOS[id]
            data = request.get_json()
            usuario.update(data)
            return '', 201
        #si no existe
        return 'No existe el id', 404

class Usuarios(Resource):
    # Método para manejar solicitudes GET para obtener todos los usuarios
    def get(self):
        return USUARIOS
    
    # Método para manejar solicitudes POST para agregar un nuevo usuario
    def post(self):
        usuario = request.get_json()
        id = int(max(USUARIOS.keys(), default=0)) + 1
        usuario["id"] = id
        USUARIOS[id] = usuario
        return USUARIOS[id], 201
=======
from flask_restful import Resource, abort
from flask import request
from main.models import UsuarioModel
from .. import db
from flask import jsonify
class IdEnUso(Exception):
    ...

class Usuario(Resource):
    def get(self, id):
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            return usuario.to_json()
        except Exception:
            abort(404, message=str("Error 404: el id del usuario no existe"))


    def delete(self, id):
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            db.session.delete(usuario)
            db.session.commit()
            return 'El usuario fue borrado de manera satisfactoria', 201
        except Exception as e:
            db.session.rollback()
            abort(404, message=str("404 Not Found: No se encuentra el usuario para eliminar. El ID no existe"))
    
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
             

    def post(self):
        data = request.get_json()
        if isinstance(data, dict):
            data = [data]
        usuarios_list = []
        for usuario_data in data:
            usuarios = UsuarioModel.from_json(usuario_data)
            try:
                tabla = UsuarioModel.query.all()
                self.verificacion(usuario_data, tabla)
            except Exception as e:
                return {'error': str(e)}, 403
            db.session.add(usuarios)
            usuarios_list.append(usuarios)
        db.session.commit()
        usuario_json = [usuario.to_json() for usuario in usuarios_list]
        return usuario_json, 201


    def verificacion(self, usuario, tabla):
        for i in tabla:
            id = i.id
            id_nuevo = usuario['id']
            if id == id_nuevo:
                raise IdEnUso('El ID esta en uso')
            else:
                return None
>>>>>>> 104ad670bb82c21f0c81a6b10a0f683cbd7ea39b
