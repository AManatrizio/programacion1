from .. import db


class Opiniones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.String(300), nullable=False)
    valoracion = db.Column(db.Integer, nullable=False)
    prestamo_id = db.Column(db.Integer, db.ForeignKey(
        "prestamos.id"), nullable=False)

    prestamos = db.relationship("Prestamos", back_populates="opinion")

    def __repr__(self):
        return f"<Opinion: {self.valoracion} - {self.comentario}>"

    def to_json(self):
        return {
            'id': self.id,
            'comentario': self.comentario,
            'valoracion': self.valoracion,
            'prestamo_id': self.prestamo_id
        }

    @staticmethod
    def from_json(opinion_json):
        valoracion = opinion_json.get('valoracion')
        if not isinstance(valoracion, int) or not (1 <= valoracion <= 5):
            raise ValueError(
                'La valoración debe ser un número entero entre 1 y 5.')

        return Opiniones(
            comentario=opinion_json.get('comentario'),
            valoracion=opinion_json.get('valoracion'),
            prestamo_id=opinion_json.get('prestamo_id')
        )
