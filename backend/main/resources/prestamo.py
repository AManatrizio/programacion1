from flask_restful import Resource
from flask import request, jsonify
from main.models import PrestamoModel
from .. import db

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
        prestamos = []
        for prestamo_data in data:
            prestamo = PrestamoModel.from_json(prestamo_data)
            db.session.add(prestamo)
            prestamos.append(prestamo)
        db.session.commit()
        return [prestamo.to_json() for prestamo in prestamos], 201