from flask_restful import Resource
from flask import request

CONFIGURACIONES = {
    
}

class Configuraciones(Resource):
    def get(self):
        return CONFIGURACIONES

    def put(self):
        ...