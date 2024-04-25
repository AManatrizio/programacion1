# from flask_restful import Resource
# from flask import request, jsonify
# from .. import db
# from main.models import AutoriaModel

# #Recurso Proyecto
# class Autoria(Resource):
#     #Insertar recurso
#     def post(self):
#         # Obtener objeto con id_animal y id_exhibicion
#         id_libro = request.get_json().get('id_libro')
#         id_autor = request.get_json().get('id_autor')

#         # Verificar si los objetos existen
#         if id_libro is None:
#             print("Animal no encontrado")
#             # Manejo de error o salida temprana si el animal no existe
#         if id_autor is None:
#             print("Exhibición no encontrada")
#             # Manejo de error o salida temprana si la exhibición no existe

#         # Insertar una nueva entrada en la tabla secundaria para asociar el animal con la exhibición
#         query = AutoriaModel.insert().values(id_animal=id_libro, id_exhibicion=id_autor)
#         try:
#             # Ejecutar la consulta
#             db.session.execute(query)
#             db.session.commit()
#         except:
#             return 'Formato no correcto', 400
#         return 'Creado con exito', 201