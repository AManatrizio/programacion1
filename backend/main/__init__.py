from flask import Flask
from dotenv import load_dotenv

#este metodo inicaliza la app y todos los modulos y librerias
def create_app():
    app = Flask(__name__)
    load_dotenv()

    return app

    