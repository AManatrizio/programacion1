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
    1: {"nombre": "El principito", "autor": "Antoine De Saint Exupery", "valoracion":"5"},
    2: {"nombre": "Narnia", "autor": "C.S. Lewis", "valoracion":"4"}
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
            libros = LIBROS[int(id)]
            data = request.get_json()
            libros.update(data)
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
    
#------------Prestamos----------------
    
PRESTAMOS = {
    1:{"usuario":"Coca", "tiempo":"2 semanas", "libro":"El principito"}

}

class Prestamo(Resource):

    def get(self,id):
        if int(id) in PRESTAMOS:
            return PRESTAMOS[int(id)]
        else:
            return "Not found", 404

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


        
#-------------Sing In---------------- No seria lo mismo que un POST en Usuario? Crear un Usuario?

SINGIN = {
    1:{"nombre":"marta", "contrasena":"!23", "email":"marta@yahoo.com"}

}

class SingIn(Resource):
    def get(self):
        return SINGIN
        
    def post(self): #Crear un Usuario
        singin = request.get_json()
        id = int(max(SINGIN.keys())) + 1
        SINGIN[id] = singin
        return SINGIN[id], 201
    
#-------------Log In------------------
    
LOGIN = {
    1:{"nombre_usuario":"Marta", "contrasena":"Marta123"},
    2:{"nombre_usuario":"JosefaRamirez", "contrasena":"lajose"}
}
class Login(Resource):

    def get(self):
        return LOGIN

    def post(self):
        login = request.get_json()
        id = int(max(LOGIN.keys()))+1
        LOGIN[id] = login
        return LOGIN[id], 201
        
#-------------Notificacion----------------------
NOTIFICACIONES = {
    1:{"mensaje":"su prestamo vence en 2 dias","hora notificacion":"2:30"},
    2:{"mensaje":"vea nuestros nuevos libros", "hora notificacion":"5:00"}
}

class Notificaciones(Resource):
    def get(self):
        return NOTIFICACIONES
    
    def post(self):
        notificacion = request.get_json()
        id = int(max(NOTIFICACIONES.keys())) + 1
        NOTIFICACIONES[id] = notificacion
        return NOTIFICACIONES[id], 201
    
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
#--------------Valoracion----------------
    
VALORACION = { #
    1:{"libro":"El Principito","valoracion":"5"},
    2:{"libro":"Narnia", "valoracion":"4"}
}

class Valoraciones(Resource):
    def get(self):
        return VALORACION
        
    def post(self):
        valo = request.get_json()
        id = int(max(VALORACION.keys())) + 1
        VALORACION[id] = valo
        return VALORACION[id], 201
    
    # def post(self,id):
    #     if int(id) in LIBROS:
    #         valoracion = request.get_json()
    #         LIBROS[int(id)]["valoracion"].update(int(valoracion))
    #         return "La valoracion del libro", id, "es", valoracion, 201
    #     return "El id no existe", 400
        
class Valoracion(Resource):
    def get(self, id):
        if int(id) in LIBROS:
            return "la valoracion del libro", id, "es", LIBROS[int(id)]["valoracion"]


    
        

#------------Comentario--------------

COMENT = {
    1:{"nombre_usuario":"Luna", "comentario":"me gusto"},
    2:{"nombre_usuario":"Martes", "comentario":"es interesante"},
    3:{"nombre_usuario":"Vivian", "comentario":"poco entretenido"}
}


class Comentario(Resource):
    def get(self,id):
        if int(id) in COMENT:
            return COMENT[int(id)]
        else:
            return "Not found", 404

    
class Comentarios(Resource):
    def get(self):
        return COMENT
          
    def post(self):
        comen = request.get_json()
        id = int(max(COMENT.keys())) + 1
        COMENT[id] = comen
        return COMENT[id], 201


