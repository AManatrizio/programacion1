from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources

# iniciamos restful

api = Api()


#este metodo inicaliza la app y todos los modulos y librerias
def create_app():
    app = Flask(__name__)
    load_dotenv()

    api.add_resource(resources.UsuariosResource, '/usuarios')
    api.add_resource(resources.UsuarioResource, '/usuario/<id>')
    api.init_app(app)

    return app
    