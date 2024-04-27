from flask_restful import Resource, abort
from flask import request
from main.models import UsuarioModel
from .. import db
from flask import jsonify
from .exception import IdEnUso

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
        usuarios = db.session.query(UsuarioModel).all()
        usuarios_json = [usuario.to_json() for usuario in usuarios]
        return jsonify(usuarios_json)
        

    def post(self):
        data = request.get_json()
        if isinstance(data, dict):
            data = [data]
        usuarios = []
        for usuario_data in data:
            usuario = UsuarioModel.from_json(usuario_data)
            try:
                tabla = UsuarioModel.query.all()
                self.verificacion(usuario_data, tabla)
            except Exception as e:
                return {'error': str(e)}, 403
            db.session.add(usuario)
            usuarios.append(usuario)
        db.session.commit()
        usuario_json = [usuario.to_json() for usuario in usuarios]
        return usuario_json, 201


    def verificacion(self, usuario, tabla):
        for i in tabla:
            id = i.id
            id_nuevo = usuario['id']
            if id == id_nuevo:
                raise IdEnUso('El ID esta en uso')
            else:
                return None
        