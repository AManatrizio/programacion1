from .. import db

opinion_prestamo = db.Table(
    'opinion_prestamo',
    db.Column('opinion', db.Integer, db.ForeignKey("opiniones.id"), primary_key = True),
    db.Column('prestamo', db.Integer, db.ForeignKey("prestamos.id"), primary_key = True)
    )

class Opiniones(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comentario = db.Column(db.String(300), nullable = False)
    valoracion = db.Column(db.String(5), nullable = False)
    prestamo_id = db.Column(db.Integer, db.ForeignKey("prestamos.id"), nullable = False)
    
    prestamos = db.relationship('Prestamos', uselist = True, secondary = opinion_prestamo, backref = db.backref('opiniones', lazy = 'dynamic'))

    def __repr__(self):
        return ('<Comentario: %r >' % (self.comentario) )

    def to_json(self):
        opinion_json = {
            'id': self.id,
            'comentario': str(self.comentario),
            'valoracion': str(self.valoracion),
            'prestamo_id': int(self.prestamo_id),
            'libro_y_usuario': [prestamo.to_json_short() for prestamo in self.prestamos]

        }
        return opinion_json
    
    @staticmethod
    def from_json(opinion_json):
        id = opinion_json.get('id')
        comentario = opinion_json.get('comentario')
        valoracion = opinion_json.get('valoracion')
        prestamo_id = opinion_json.get('prestamo_id')
        return Opiniones(id = id,
                       comentario = comentario,
                       valoracion = valoracion,
                       prestamo_id = prestamo_id,)
