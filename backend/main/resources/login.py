from flask_restful import Resource, abort
from flask import request
from main.models import UsuarioModel
from .. import db

class LogIn(Resource):
    def post(self, id):
        try:
            usuario = db.session.query(UsuarioModel).get_or_404(id)
            return 'Sesion iniciada', 201
        except Exception: 
            abort(500, message=str("Error 404: el id del usuario no existe, cree una cuenta"))