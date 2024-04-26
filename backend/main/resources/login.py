from flask_restful import Resource, abort
from flask import request
from main.models import UsuarioModel
from .. import db

class LogIn(Resource):
    def post(self, id):
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            return 'Sesion iniciada', 201
        except Exception: #Si la URL tiene un id para iniciar sesion que no existe, entonces da error
            abort(500, message=str("Error 404: el id del usuario no existe, cree una cuenta"))