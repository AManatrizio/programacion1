from flask_restful import Resource
from flask import request, jsonify
from main.models import PrestamoModel
from .. import db

class IdEnUso(Exception):
    ...

class LibroNoDisponible(Exception):
    ...

class Prestamo(Resource):
    def get(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        return prestamo.to_json()
    
    def delete(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        db.session.delete(prestamo)
        db.session.commit()
        return '', 201
    
    def put(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        data = request.get_json().items()
        for key , value in data:
            setattr(prestamo, key, value)
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201

class Prestamos(Resource):
    def get(self):
        prestamos = db.session.query(PrestamoModel).all()
        prestamos_json = [(prestamo.to_json()) for prestamo in prestamos]
        return jsonify(prestamos_json)
        
    def post(self):
        data = request.get_json()
        if isinstance(data, dict):
            data = [data]
        prestamos = []
        for prestamo_data in data:
            prestamo = PrestamoModel.from_json(prestamo_data)
            try:
                tabla = PrestamoModel.query.all()
                self.verificacion(prestamo_data, tabla)
            except Exception as e:
                return {'error': str(e)}, 403
            db.session.add(prestamo)
            prestamos.append(prestamo)
        db.session.commit()
        prestamos_json = [prestamo.to_json() for prestamo in prestamos]
        return prestamos_json, 201

    def verificacion(self, prestamo, tabla):
        for i in tabla:
            id = i.id
            id_nuevo = prestamo['id']
            id_libro = i.libro_id
            id_libro_nuevo = prestamo['libro_id']
            if id_libro == id_libro_nuevo:
                raise LibroNoDisponible('El libro no esta disponible')
            elif id == id_nuevo:
                raise IdEnUso('El ID esta en uso')
            else:
                return None