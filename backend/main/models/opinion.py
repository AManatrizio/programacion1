from .. import db

class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comentario = db.Column(db.String(300), nullable = False)
    valoracion = db.Column(db.String(5), nullable = False)
    prestamo_id = db.Column(db.Integer, db.ForeignKey("prestamo.id"), nullable = False)
    
    prestamo = db.relationship("Prestamo", uselist = False, back_populates = "opinion", cascade="all, delete-orphan", single_parent = True)

    def __repr__(self):
        return ('<Comentario: %r >' % (self.comentario) )

    def to_json(self):
        opinion_json = {
            'id': self.id,
            'comentario': str(self.comentario),
            'valoracion': str(self.valoracion),
            'prestamo_id': str(self.prestamo_id)
        }
        return opinion_json
    
    @staticmethod
    def from_json(opinion_json):
        id = opinion_json.get('id')
        comentario = opinion_json.get('comentario')
        valoracion = opinion_json.get("valoracion")
        prestamo_id = opinion_json.get('prestamo_id')
        return Opinion(id = id,
                       comentario = comentario,
                       valoracion = valoracion,
                       prestamo_id = prestamo_id,
                       )