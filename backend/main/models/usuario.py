from .. import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    clave = db.Column(db.String(14), nullable = False)
    telefono = db.Column(db.String(14), nullable = False)
    email = db.Column(db.String(100), nullable = False)


    prestamo = db.relationship("Prestamo", back_populates = "usuario", cascade = "all, delete-orphan")
    notificacion = db.relationship("Notificacion", back_populates = "usuario", cascade = "all, delete-orphan")


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


###comentarios = db.relationship("Comentario", back_populates = "usuario", cascade = "all, delete-orphan")
###valoraciones = db.relationship("ValUsLib", back_populates = "usuario", cascade = "all, delete-orphan")
