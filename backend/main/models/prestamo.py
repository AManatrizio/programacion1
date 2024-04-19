from .. import db

class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return ('<Prestamo: %r >' % (self.prestamo) )

    def to_json(self):
        prestamo_json = {
            'id': self.id,
            'prestamo': str(self.prestamo)
            }
        return prestamo_json
    
    @staticmethod
    def from_json(prestamo_json):
        id = prestamo_json.get('id')
        prestamo = prestamo_json.get('prestamo')
        return Prestamo(id = id,
                        prestamo = prestamo,
                        )