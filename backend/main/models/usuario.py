from .. import db
from datetime import datetime

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

    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')

    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)

    def validate_pass(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return ('<Usuario: %r >' % (self.nombre))

    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'email': str(self.email),
            'rol': str(self.rol),

        }
        return usuario_json

    def to_json_complete(self):
        usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'email': str(self.email),
            'telefono': str(self.telefono),
            'rol': str(self.rol),
        }
        return usuario_json

    @staticmethod
    def from_json(usuario_json):
        nombre = usuario_json.get('nombre')
        telefono = usuario_json.get('telefono')
        email = usuario_json.get('email')
        password = usuario_json.get('password')
        rol = usuario_json.get('rol')

        return Usuarios(
            nombre=nombre,
            telefono=telefono,
            email=email,
            plain_password=password,
            rol=rol)
