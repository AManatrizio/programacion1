from .. import db

class Notificacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    notificacion = db.Column(db.String(300), nullable = False)

    def __repr__(self):
        return ('<notificacion: %r >' % (self.notificacion) )

    def to_json(self):
        notificacion_json = {
            'id': self.id,
            'notificacion': str(self.notificacion),
        }
        return notificacion_json
    
    @staticmethod
    def from_json(notificacion_json):
        id = notificacion_json.get('id')
        notificacion = notificacion_json.get('notificacion')
        return Notificacion(id = id,
                          notificacion = notificacion,)