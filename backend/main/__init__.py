from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import os





from flask_sqlalchemy import SQLAlchemy

api = Api()

db = SQLAlchemy()
#Este metodo create_app inicializa la app y todos los modulos
def create_app():
    app = Flask(__name__)
    load_dotenv()

#Si no existe el archivo de base de datos crearlo (solo valido si se usa SQLite)
    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
#URL de configuracion de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)

#Iniciamos restful
    import main.resources as resources
#Cargar a la api los recursos y especificar la ruta
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