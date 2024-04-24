from .. import db

class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    prestamo = db.Column(db.String(20), nullable = False) ###Estado, activo, inactivo, vencido --> enviar notificacion
    fecha_inicio = db.Column(db.String(100), nullable = False)
    fecha_vencimiento = db.Column(db.String(100), nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable = False)
    libro_id = db.Column(db.Integer, db.ForeignKey("libro.id"), nullable = False)

    usuario = db.relationship("Usuario", back_populates = "prestamo", uselist = False, single_parent = True)
    libro = db.relationship("Libro", back_populates = "prestamo", uselist = False, single_parent = True)
    opinion = db.relationship("Opinion", uselist = False, back_populates = "prestamo", cascade="all, delete-orphan", single_parent = True)

    def __repr__(self):
        return ('<Prestamo: %r >' % (self.prestamo) )

    def to_json(self):
        prestamo_json = {
            'id': self.id,
            'prestamo': str(self.prestamo),
            'fecha_inicio': str(self.fecha_inicio),
            'fecha_vencimiento': str(self.fecha_vencimiento),
            'usuario_id': int(self.usuario_id),
            'libro_id': int(self.libro_id),
            }
        return prestamo_json
    
    def from_json(prestamo_json):
        id = prestamo_json.get('id')
        prestamo = prestamo_json.get('prestamo')
        fecha_inicio = prestamo_json.get('fecha_inicio')
        fecha_vencimiento = prestamo_json.get('fecha_vencimiento')
        usuario_id = prestamo_json.get('usuario_id')
        libro_id = prestamo_json.get('libro_id')
        return Prestamo(id = id,
                        prestamo = prestamo,
                        fecha_inicio = fecha_inicio,
                        fecha_vencimiento = fecha_vencimiento,
                        usuario_id = usuario_id,
                        libro_id = libro_id,
                        )