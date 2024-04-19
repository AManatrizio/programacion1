from flask_restful import Resource
from flask import request
from main.models import UsuarioModel
from .. import db

class LogIn(Resource):
    def post(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        return 'Sesion iniciada', 201
