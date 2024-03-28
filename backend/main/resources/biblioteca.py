from flask_restful import Resource
from flask import request

#--------------Usuarios-----------------

#Los numeros son los Id
USUARIOS = {
    1:{"nombre":"Josefina","rol":"Admin"},
    2:{"nombre":"Luna","rol":"Cliente"},
    3:{"nombre":"Marco","rol":"Bibliotecario"}
    }

class Usuario(Resource):
    def get(self,id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        else:
            return "Not found", 404
        
    def delete(self,id):
        if int(id) in  USUARIOS:
            del USUARIOS[int(id)]
            return "", 204

        return "Not found", 404
    
    def put(self,id):
        if int(id) in  USUARIOS:
            usuario = USUARIOS[int(id)]
            data = request.get_json()
            usuario.update(data)
            return "", 201

        return "Not found", 404

#Aca obtenemos TODOS los usuarios
class Usuarios(Resource):
    def get(self):
        return USUARIOS
    
    # En POST creo un usuario con su esctructura
    def post(self):
        usuario = request.get_json()
        id = int(max(USUARIOS.keys())) + 1
        USUARIOS[id] = usuario
        return USUARIOS[id], 201


#--------------------Libros-------------------------
LIBROS = {
    1: {"nombre": "El principito", "autor": "Antoine De Saint Exupery"},
    2: {"nombre": "Narnia", "autor": "C.S. Lewis"}
}


class Libro(Resource):
    #Obtiene lista de todos los libros
    def get(self,id):
        if int(id) in LIBROS:
            return LIBROS[int(id)]
        else:
            return "Not found", 404
    #Elimina un libro
    def delete(self,id):
        if int(id) in  LIBROS:
            del LIBROS[int(id)]
            return "", 204

        return "Not found", 404
    #Edita un libro
    def put(self,id):
        if int(id) in  LIBROS:
            libro = LIBROS[int(id)]
            data = request.get_json
            libro.update(data)
            return "", 201

        return "Not found", 404
    
class Libros(Resource):
    def get(self):
        return LIBROS
        
    def post(self):
        libro = request.get_json()
        id = int(max(LIBROS.keys())) + 1
        LIBROS[id] = libro
        return LIBROS[id], 201
    
#-------------Sing In---------------- No seria lo mismo que un POST en Usuario? Y login?

# class SingIn(Resource):
        
#     def post(self): #Crear un Usuario
#         usuario = request.get_json()
#         id = int(max(USUARIOS.keys())) + 1
#         USUARIOS[id] = usuario
#         return USUARIOS[id], 201
    
#------------Prestamos----------------
    
PRESTAMOS = {
    1:{"usuario":"Coca", "tiempo":"2 semanas", "libro":"El principito"}

}

class Prestamos(Resource):

    def get(self):
        return PRESTAMOS
        
    def post(self):
        prestamo = request.get_json()
        id = int(max(PRESTAMOS.keys())) + 1
        PRESTAMOS[id] = prestamo
        return PRESTAMOS[id], 201

    # def post(self, id_usuario):
    #     if int(id) in USUARIOS:
    #         usuario_id = int(id_usuario)
    #         usuario_nombre = USUARIOS[usuario_id]["nombre"] #Pedir el id de usuario?
    #         prestamo = request.get_json()
    #         prestamo["usuario"] = usuario_nombre  # Agregar el nombre del usuario al préstamo
    #         prestamo_id = int(max(PRESTAMOS.keys())) + 1 #Pide que tenga la misma estructura
    #         PRESTAMOS[prestamo_id] = prestamo
    #         return PRESTAMOS[prestamo_id], 201
    #     else:
    #         return "Usuario no encontrado", 404
    

class Prestamo(Resource):

    def get(self,id):
        if int(id) in PRESTAMOS:
            return PRESTAMOS[int(id)]
        else:
            return "Not found", 404
        
#-------------Notificacion----------------------
NOTIFICACIONES = {

}

class Notificaciones(Resource):
    def post(self):
        notificacion = notificacion.get_json()
        id = int(max(NOTIFICACIONES.keys())) + 1
        NOTIFICACIONES[id] = notificacion
        return NOTIFICACIONES[id], 201
        


