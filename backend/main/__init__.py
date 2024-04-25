from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


api = Api()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)
    migrate.init_app(app, db)

    import main.resources as resources
    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<int:id>')
    api.add_resource(resources.OpinionesResources, '/opiniones')
    api.add_resource(resources.OpinionResource, '/opinion/<int:id>')
    api.add_resource(resources.SignInResources, '/signin/<int:id>')
    api.add_resource(resources.PrestamosResource, '/prestamos')
    api.add_resource(resources.PrestamoResource, '/prestamo/<int:id>')
    api.add_resource(resources.NotificacionesResources, '/notificaciones')
    api.add_resource(resources.LogInResources, '/login/<int:id>')
    api.add_resource(resources.LibrosResources, '/libros')
    api.add_resource(resources.LibroResources, '/libro/<int:id>')
    api.add_resource(resources.ConfiguracionesResources, '/configuraciones')
    api.add_resource(resources.AutoresResource, '/autores')
    api.add_resource(resources.AutorResource, '/autor/<int:id>')

    api.init_app(app)
    return app