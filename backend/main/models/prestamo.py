from .. import db

class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    prestamo = db.Column(db.String(20), nullable = False) ###Estado, activo, inactivo, vencido
    fecha = db.Column(db.String(100), nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable = False)
    libro_id = db.Column(db.Integer, db.ForeignKey("libro.id"), nullable = False)

    usuario = db.relationship("Usuario", back_populates = "prestamo", uselist = False, single_parent = True)
    libro = db.relationship("Libro", back_populates = "prestamo", uselist = False, single_parent = True)

    def __repr__(self):
        return ('<Prestamo: %r >' % (self.fecha) )

    def to_json(self):
        prestamo_json = {
            'id': self.id,
            'prestamo': str(self.prestamo),
            'fecha': str(self.fecha),
            'usuario_id': int(self.usuario_id),
            'libro_id': int(self.libro_id),
            }
        return prestamo_json
    
    @staticmethod
    def from_json(prestamo_json):
        id = prestamo_json.get('id')
        prestamo = prestamo_json.get('prestamo')
        fecha = prestamo_json.get('fecha')
        usuario_id = prestamo_json.get('usuario_id')
        libro_id = prestamo_json.get('libro_id')
        return Prestamo(id = id,
                        prestamo = prestamo,
                        fecha = fecha,
                        usuario_id = usuario_id,
                        libro_id = libro_id,
                        )