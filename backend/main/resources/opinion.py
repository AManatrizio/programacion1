from flask_restful import Resource, abort
from flask import request, jsonify
from main.models import OpinionModel, PrestamoModel
from .exception import IdEnUso
from .. import db
class IdEnUso(Exception):
    ...

class LibroNoDisponible(Exception):
    ...


class Opinion(Resource):
    def get(self, id):
        try:
            opinion = db.session.query(OpinionModel).get_or_404(id)
            return opinion.to_json()
        except Exception:
            abort(500, message=str("Error 404: el ID de la opinion no existe"))
    
    def delete(self, id):
        try:
            opinion = db.session.query(OpinionModel).get_or_404(id)
            db.session.delete(opinion)
            db.session.commit()
            return 'La opinion fue borrada de manera satisfactoria', 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=str("404 Not Found: No se encuentra la opinion para eliminar. El ID no existe"))
    
    
    def put(self, id):
        try:
            opinion = db.session.query(OpinionModel).get_or_404(id)
            data = request.get_json().items()
            for key , value in data:
                setattr(opinion, key, value)
            db.session.add(opinion)
            db.session.commit()
            return opinion.to_json(), 201
        except Exception as e:
            db.session.rollback()
            abort(500, message=str("Error 404 Not Found: No se encuentra la opinion para modificar"))
  


class Opiniones(Resource):
    def get(self):
        page = 1
        per_page = 10
        opiniones = db.session.query(OpinionModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))   
        
        opiniones = opiniones.paginate(page=page, per_page=per_page, error_out=True)
        
        return jsonify({'opiniones': [opinion.to_json() for opinion in opiniones],
                  'total': opiniones.total,
                  'pages': opiniones.pages,
                  'page': page
                })

    def post(self):
        data = request.get_json()
        prestamo_id = data.get('prestamo_id')

        # Verificar si el prestamo_id existe en la base de datos de prestamos
        prestamo_existente = db.session.query(PrestamoModel).filter_by(id=prestamo_id).first()
        if not prestamo_existente:
            return {'error': 'No se puede crear la opinión, el prestamo con ese id no existe'}, 404

        opinion = OpinionModel.from_json(data)
        db.session.add(opinion)
        db.session.commit()
        return opinion.to_json(), 201
    
    
    
        