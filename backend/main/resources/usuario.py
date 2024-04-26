from flask_restful import Resource, abort
from flask import request
from main.models import UsuarioModel
from .. import db
from flask import jsonify

class Usuario(Resource):
    def get(self, id):
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            return usuario.to_json()
        except Exception:
            abort(500, message=str("Error 404: el id del usuario no existe"))


    def delete(self, id):
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            db.session.delete(usuario)
            db.session.commit()
            return '', 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=str(e))
    
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
            abort(500, message=str(e))

class Usuarios(Resource):
    def get(self):
        usuarios = db.session.query(UsuarioModel).all()
        usuarios_json = [usuario.to_json() for usuario in usuarios]
        return jsonify(usuarios_json)
        
    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201
        



