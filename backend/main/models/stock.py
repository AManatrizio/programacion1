from .. import db


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libro_id = db.Column(db.Integer, db.ForeignKey(
        'libros.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False, default=0)

    libro = db.relationship("Libros", back_populates="stock")

    def __repr__(self):
        return f'<Stock: Libro ID {self.libro_id}, Cantidad {self.cantidad}>'
