from flask_restful import Resource
from flask import request

PRESTAMOS = {
    1:{'prestamo': 'prestamo',
       'libro': '1',
       'usuario': '2'
       }
}

class Prestamo(Resource):
    def get(self, id):
        if id in Prestamo:
            return PRESTAMOS(id)
        return 'No existe el id', 404
    
    def delete(self, id):
        if id in PRESTAMOS:
            del PRESTAMOS[id]
            return '', 204
        return 'No existe el id', 404
    
    def put(self, id):
        if id in PRESTAMOS:
            prestamo = PRESTAMOS(id)
            data = request.get_json()
            prestamo.update(data)
            return '', 201
        return 'No existe el id', 404

class Prestamos(Resource):
    def get(self):
        return PRESTAMOS
    
    def post(self):
        prestamo = request.get_json()
        id = int(max(PRESTAMOS.keys())) + 1
        PRESTAMOS[id] = prestamo
        return 'Prestamo: ', PRESTAMOS[id], 'creado.', 201