from .. import db

autor_libro = db.Table(
    'autor_libro',
    db.Column('autor', db.Integer, db.ForeignKey(
        "autores.id"), primary_key=True),
    db.Column('libro', db.Integer, db.ForeignKey(
        "libros.id"), primary_key=True)
)


class Libros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    imagen_url = db.Column(db.String(255), nullable=True)

    autores = db.relationship(
        'Autores', secondary=autor_libro, backref=db.backref('libros', lazy='dynamic'))
    prestamo = db.relationship(
        "Prestamos", back_populates="libro", cascade="all, delete-orphan")

    def __repr__(self):
        return ('<Libro: %r >' % (self.nombre))

    @staticmethod
    def from_json(libro_json):
        nombre = libro_json.get('nombre')
        genero = libro_json.get('genero')
        imagen_url = libro_json.get('imagen_url')
        return Libros(
            nombre=nombre,
            genero=genero,
            imagen_url=imagen_url
        )

    def to_json(self):
        libro_json = {
            'id': self.id,
            'nombre': self.nombre,
            'genero': self.genero,
            'imagen_url': self.imagen_url,
        }
        return libro_json
