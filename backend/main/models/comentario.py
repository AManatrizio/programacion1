from .. import db

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comentario = db.Column(db.String(300), nullable = False)

    def __repr__(self):
        return ('<Comentario: %r >' % (self.comentario) )

    def to_json(self):
        comentario_json = {
            'id': self.id,
            'comentario': str(self.comentario),
        }
        return comentario_json
    
    @staticmethod
    def from_json(comentario_json):
        id = comentario_json.get('id')
        comentario = comentario_json.get('comentario')
        return Comentario(id = id,
                          comentario = comentario,)