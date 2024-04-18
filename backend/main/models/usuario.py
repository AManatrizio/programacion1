from .. import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return ('<Usuario: %r >' % (self.nombre) )

    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'email': str(self.email),
        }
        return usuario_json
    
    @staticmethod
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        email = usuario_json.get('email')
        return Usuario(id = id,
                       nombre = nombre,
                       apellido = apellido,
                       email = email,)
