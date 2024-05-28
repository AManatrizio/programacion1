from flask_restful import Resource, abort
from flask import request, jsonify
from main.models import OpinionModel, PrestamoModel
from .exception import IdEnUso
from .. import db

class Opinion(Resource):
    def get(self, id):
        try:
            opinion = db.session.query(OpinionModel).get_or_404(id)
            return opinion.to_json()
        except Exception:
            abort(500, message=str("Error 404: el id de la opinion no existe"))
    
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
        per_page = 5
        opiniones = db.session.query(OpinionModel)
            
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        if request.args.get('valoracion'):
            cant_ast = int(request.args.get('valoracion'))
            valoracion_a_buscar = '*' * cant_ast
            opiniones = opiniones.filter(OpinionModel.valoracion == valoracion_a_buscar)
        
        opiniones = opiniones.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'opiniones': [opinion.to_json() for opinion in opiniones],
                  'total': opiniones.total,
                  'pages': opiniones.pages,
                  'page': page
                })
        

    def post(self):
        data = request.get_json()
        if isinstance(data, dict):
            data = [data]
        opinion_list = []
        for opinion_data in data:
            opinion = OpinionModel.from_json(opinion_data)
            try:
                tabla = OpinionModel.query.all()
                self.verificacion(opinion_data, tabla)
            except Exception as e:
                return {'error': str(e)}, 403
            db.session.add(opinion)
            opinion_list.append(opinion)
        db.session.commit()
        opinion_json = [opinion.to_json() for opinion in opinion_list]
        return opinion_json, 201


    def verificacion(self, opinion, tabla):
        for i in tabla:
            id = i.id
            id_nuevo = opinion['id']
            if id == id_nuevo:
                raise IdEnUso('El ID esta en uso')
            else:
                return None