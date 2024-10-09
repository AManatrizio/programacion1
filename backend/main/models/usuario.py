from .. import db
from datetime import datetime

# Importamos de python 2 funciones
from werkzeug.security import generate_password_hash, check_password_hash


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)

    password = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(10), nullable=False, server_default="null")

    prestamo = db.relationship(
        "Prestamos", back_populates="usuario", cascade="all, delete-orphan")
    notificacion = db.relationship(
        "Notificaciones", back_populates="usuario", cascade="all, delete-orphan")

  # Getter de la contraseña plana no permite leerla
    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')
    # Setter de la contraseña toma un valor en texto plano
    # calcula el hash y lo guarda en el atributo password

    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
    # compara una contraseña en texto plano con la hasheada para ver si son iguales

    def validate_pass(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return ('<Usuario: %r >' % (self.nombre))

    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'clave': str(self.clave),
            'telefono': str(self.telefono),
            'email': str(self.email),
        }
        return usuario_json

    def to_json_complete(self):
        usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'email': str(self.email),
        }
        return usuario_json

    @staticmethod
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        clave = usuario_json.get('clave')
        telefono = usuario_json.get('telefono')
        email = usuario_json.get('email')
        password = usuario_json.get('password')
        rol = usuario_json.get('rol')

        return Usuarios(id=id,
                        nombre=nombre,
                        clave=clave,
                        telefono=telefono,
                        email=email,
                        plain_password=password,
                        rol=rol)
