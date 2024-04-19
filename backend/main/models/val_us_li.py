from .. import db

class ValUsLib(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    valoracion_id = db.Column(db.Integer, db.ForeignKey("valoracion.id"), nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable = False)
    libro_id = db.Column(db.Integer, db.ForeignKey("libro.id"), nullable = False)

    valoracion = db.relationship("Valoracion", back_populates = "comentarios", uselist = False, single_parent = True)
    usuario = db.relationship("Usuario", back_populates = "valoraciones", uselist = False, single_parent = True)
    libro = db.relationship("Libro", back_populates = "comentarios", uselist = False, single_parent = True)


    def to_json(self):
        valuslib_json = {
            'id': self.id,
            'valoracion_id': int(self.valoracion_id),
            'usuario_id': int(self.usuario_id),
            'libro_id': int(self.libro_id),
        }
        return valuslib_json
    
    @staticmethod
    def from_json(valuslib_json):
        id = valuslib_json.get('id')
        valoracion_id = valuslib_json.get('valoracion_id')
        usuario_id = valuslib_json.get('usuario_id')
        libro_id = valuslib_json.get('libro_id')
        return ValUsLib(id = id,
                          valoracion_id = valoracion_id,
                          usuario_id = usuario_id,
                          libro_id = libro_id)