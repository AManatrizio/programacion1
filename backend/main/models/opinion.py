from .. import db


class Opinion(db.Model):
    #Primaria
    id = db.Column(db.Integer, primary_key = True)
    #Atributos
    comentario = db.Column(db.String(300), nullable = False)
    valoracion = db.Column(db.Float(5), nullable = False)
    # Relacion para ser foranea en PRESTAMO
    opinion = db.relationship("Prestamo", uselist = False, back_populates = "prestamo_usu", cascade="all, delete-orphan", single_parent=True)

    def __repr__(self):
        return ('<Comentario: %r >' % (self.comentario) )

    def to_json(self):
        opinion_json = {
            'id': self.id,
            'comentario': str(self.comentario),
            'valoracion': float(self.valoracion),

        }
        return opinion_json
    
    @staticmethod
    def from_json(opinion_json):
        id = opinion_json.get('id')
        comentario = opinion_json.get('comentario')
        valoracion = opinion_json.get("valoracion")
        return Opinion(id = id,
                          comentario = comentario,
                          valoracion = valoracion)
