from .. import db

class Notificacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    notificacion = db.Column(db.String(300), nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable = False)

    usuario = db.relationship("Usuario", back_populates = "notificacion", uselist = False, single_parent = True)

    def __repr__(self):
        return ('<notificacion: %r >' % (self.notificacion) )

    def to_json(self):
        notificacion_json = {
            'id': self.id,
            'notificacion': str(self.notificacion),
            'usuario_id': int(self.usuario_id),
        }
        return notificacion_json
    
    def from_json(notificacion_json):
        id = notificacion_json.get('id')
        notificacion = notificacion_json.get('notificacion')
        usuario_id = notificacion_json.get('usuario_id')
        return Notificacion(id = id,
                            notificacion = notificacion,
                            usuario_id = usuario_id)