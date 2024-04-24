from .. import db

class Usuario(db.Model):
    #Primaria
    id = db.Column(db.Integer, primary_key = True)
    #Atributos
    nombre = db.Column(db.String(100), nullable = False)
    clave = db.Column(db.String(14), nullable = False)
    telefono = db.Column(db.String(14), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    #Foranea PRESTAMO - USUARIO (N:1)
    usuario = db.relationship("Prestamo", uselist = False, back_populates = "prestamo_usu", cascade="all, delete-orphan", single_parent=True)

    #Foranea USUARIO - NOTIFICACIONES (1:N)
    usuario_noti = db.relationship("Notificacion", uselist = False, back_populates = "notificacion", cascade="all, delete-orphan", single_parent=True)

    def __repr__(self):
        return ('<Usuario: %r >' % (self.nombre) )

    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'clave': str(self.clave),
            'telefono': str(self.telefono),
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
        return Usuario(id = id,
                       nombre = nombre,
                       clave = clave,
                       telefono = telefono,
                       email = email,)