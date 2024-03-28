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

    api.add_resource(resources.UsuariosResource, "/usuarios") #Hacerlo con minuscula

    api.add_resource(resources.UsuarioResource, "/usuario/<id>")

    
    api.init_app(app)

    return app