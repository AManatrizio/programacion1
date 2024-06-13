
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#Importar Flask JWT
from flask_jwt_extended import JWTManager
from flask_mail import Mail

import os


api = Api()

db = SQLAlchemy()

#Inicializar Migrate
migrate = Migrate()

#Inicializar JWT
jwt = JWTManager()

mailsender = Mail()


def create_app():
    app = Flask(__name__)
    load_dotenv()

    #Si no existe el archivo de base de datos crearlo (solo válido si se utiliza SQLite)
    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))
    
    #Url de configuración de base de datos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)

    #Importar directorio de recursos
    import main.resources as resources
    
    #Recursos en API y su ruta
    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<int:id>')
    api.add_resource(resources.OpinionesResources, '/opiniones')
    api.add_resource(resources.OpinionResource, '/opinion/<int:id>')
    api.add_resource(resources.PrestamosResource, '/prestamos')
    api.add_resource(resources.PrestamoResource, '/prestamo/<int:id>')
    api.add_resource(resources.NotificacionesResources, '/notificaciones')
    api.add_resource(resources.LibrosResources, '/libros')
    api.add_resource(resources.LibroResources, '/libro/<int:id>')
    api.add_resource(resources.ConfiguracionesResources, '/configuraciones')
    api.add_resource(resources.AutoresResource, '/autores')
    api.add_resource(resources.AutorResource, '/autor/<int:id>')

    #Cargar la aplicacion en la API de Flask Restful
    #es para que la aplicacion de flask funcione como API
    api.init_app(app)
    
    #Cargar clave secreta
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    
    #Cargar tiempo de expiración de los tokens
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    jwt.init_app(app)

    from main.auth import routes
    
    #Importar blueprint, que va a independizar la autenticacion, el login y registro de todo el resto de la API 
    #para trabajarlo mejor por separado
    app.register_blueprint(routes.auth)
    
    #Configuración de mail
    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER'] = os.getenv('FLASKY_MAIL_SENDER')
    #Inicializar en app
    mailsender.init_app(app) 
    
    

    #Por ultimo retornamos la aplicacion iniializada
    return app