from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources

#Iniciamos restful


api = Api()
#Este metodo create_app inicializa la app y todos los modulos
def create_app():
    app = Flask(__name__)
    load_dotenv()

    api.add_resource(resources.UsuarioResource, "/usuario/<id>")
    api.add_resource(resources.UsuariosResource, "/usuarios") #Hacerlo con minuscula

    api.add_resource(resources.LibroResource, "/libro/<id>")
    api.add_resource(resources.LibrosResource, "/libros") #Hacerlo con minuscula

    api.add_resource(resources.PrestamoResource, "/prestamo/<id>")
    api.add_resource(resources.PrestamosResource, "/prestamos")

    api.add_resource(resources.SignInResource, "/singin")

    api.add_resource(resources.LoginResource, "/login")

    api.add_resource(resources.NotificacionResource, "/notificaciones")  

    api.add_resource(resources.ConfiguracionResource, "/configuracion/<id>")  
    api.add_resource(resources.ConfiguracionesResource, "/configuraciones")  

    api.add_resource(resources.ValoracionResource, "/valoracion/<id>")  
    api.add_resource(resources.ValoracionesResource, "/valoraciones")  
    
    api.add_resource(resources.ComentarioResource, "/comentario/<id>")  
    api.add_resource(resources.ComentariosResource, "/comentarios")  


    api.init_app(app)

    return app