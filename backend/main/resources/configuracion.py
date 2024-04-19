from flask_restful import Resource
from flask import request
from main.models import UsuarioModel
from .. import db

#-------------Configuracion--------------

CONFI = {
    1:{"tipo":"historia", "color":"rojo", "old":"5 anos"},
    2:{"tipo":"fantasia", "color":"violeta", "old":"6 meses"}
}
    
class Configuracion(Resource):
    def get(self,id):
        if int(id) in CONFI:
            return CONFI[int(id)]
        else:
            return "Not found", 404
        
    def put(self,id):
        if int(id) in  CONFI:
            confi = CONFI[int(id)]
            data = request.get_json()
            confi.update(data)
            return "", 201

        return "Not found", 404
    
class Configuraciones(Resource):

    def get(self):
        return CONFI
        
    def post(self):
        confi = request.get_json()
        id = int(max(CONFI.keys())) + 1
        CONFI[id] = confi
        return CONFI[id], 201