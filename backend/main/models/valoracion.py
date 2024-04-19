from .. import db

class Valoracion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    valoracion = db.Column(db.String(300), nullable = False)

    valoraciones = db.relationship("ValUsLib", back_populates = "valoracion", cascade = "all, delete-orphan")


    def __repr__(self):
        return ('<Valoracion: %r >' % (self.valoracion) )

    def to_json(self):
        valoracion_json = {
            'id': self.id,
            'valoracion': str(self.valoracion),
        }
        return valoracion_json
    
    @staticmethod
    def from_json(valoracion_json):
        id = valoracion_json.get('id')
        valoracion = valoracion_json.get('valoracion')
        return Valoracion(id = id,
                          valoracion = valoracion,)
