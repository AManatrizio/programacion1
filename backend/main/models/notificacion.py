from .. import db

class Notificacion(db.Model):
    #Clave Primaria
    id = db.Column(db.Integer, primary_key = True)
    #Atributos
    notificacion = db.Column(db.String(300), nullable = False)

    #Foranea USUARIO - NOTIFICACIONES (1:N)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), primary_key = True)
    notificacion = db.relationship("Usuario", uselist = False, back_populates = "usuario_noti", cascade="all, delete-orphan", single_parent=True)    
    

    def __repr__(self):
        return ('<notificacion: %r >' % (self.notificacion) )

    def to_json(self):
        notificacion_json = {
            'id': self.id,
            'notificacion': str(self.notificacion),
        }
        return notificacion_json
    
    def from_json(notificacion_json):
        id = notificacion_json.get('id')
        notificacion = notificacion_json.get('notificacion')
        return Notificacion(id = id,
            notificacion = notificacion,)