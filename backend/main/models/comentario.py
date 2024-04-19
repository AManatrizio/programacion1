from .. import db

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comentario = db.Column(db.String(300), nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable = False)
    libro_id = db.Column(db.Integer, db.ForeignKey("libro.id"), nullable = False)

    usuario = db.relationship("Usuario", back_populates = "comentarios", uselist = False, single_parent = True)
    libro = db.relationship("Libro", back_populates = "comentarios", uselist = False, single_parent = True)

    def __repr__(self):
        return ('<Comentario: %r >' % (self.comentario) )

    def to_json(self):
        comentario_json = {
            'id': self.id,
            'comentario': str(self.comentario),
            'usuario_id': int(self.usuario_id),
            'libro_id': int(self.libro_id)
        }
        return comentario_json
    
    @staticmethod
    def from_json(comentario_json):
        id = comentario_json.get('id')
        comentario = comentario_json.get('comentario')
        usuario_id = comentario_json.get('usuario_id')
        libro_id = comentario_json.get('libro_id')
        return Comentario(id = id,
                          comentario = comentario,
                          usuario_id = usuario_id,
                          libro_id = libro_id)