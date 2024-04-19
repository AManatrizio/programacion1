from flask_restful import Resource
from flask import request
from main.models import ComentarioModel
from .. import db

#------------Comentario--------------



class Comentario(Resource):
    def get(self, id):
        comentario = db.session.query(ComentarioModel).get_or_404(id)
        return comentario.to_json()
    
    def delete(self, id):
        comentario = db.session.query(ComentarioModel).get_or_404(id)
        db.session.delete(comentario)
        db.session.commit()
        return '', 201


class Comentarios(Resource):
    def get(self):
        comentarios = db.session.query(ComentarioModel).all()
        comentarios_json = [(comentario.to_json) for comentario in comentarios]
        return comentarios_json

    def post(self):
        comentario = ComentarioModel.from_json(request.get_json())
        db.session.add(comentario)
        db.session.commit()
        return comentario.to_json(), 201




# COMENT = {
#     1:{"nombre_usuario":"Luna", "comentario":"me gusto"},
#     2:{"nombre_usuario":"Martes", "comentario":"es interesante"},
#     3:{"nombre_usuario":"Vivian", "comentario":"poco entretenido"}
# }


# class Comentario(Resource):
#     def get(self,id):
#         if int(id) in COMENT:
#             return COMENT[int(id)]
#         else:
#             return "Not found", 404

    
# class Comentarios(Resource):
#     def get(self):
#         return COMENT
          
#     def post(self):
#         comen = request.get_json()
#         id = int(max(COMENT.keys())) + 1
#         COMENT[id] = comen
#         return COMENT[id], 201
