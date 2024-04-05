from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources

api = Api()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')
    api.add_resource(resources.ValoracionesResources, '/valoraciones')
    api.add_resource(resources.ValoracionResources, '/valoracion/<id>')
    api.add_resource(resources.SignInResources, '/signin/<id>')
    api.add_resource(resources.PrestamosResource, '/prestamos')
    api.add_resource(resources.PrestamoResource, '/prestamo/<id>')
    api.add_resource(resources.NotificacionesResources, '/notificaciones')
    api.add_resource(resources.LogInResources, '/login/<id>')
    api.add_resource(resources.LibrosResources, '/libro')
    api.add_resource(resources.LibroResources, '/libros/<id>')
    api.add_resource(resources.ConfiguracionesResources, '/configuraciones')
    api.add_resource(resources.ComentariosResources, '/comentarios')
    api.add_resource(resources.ComentarioResources, '/comentario/<id>')
    api.init_app(app)
    return app