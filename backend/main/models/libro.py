from .. import db

autor_libro = db.Table(
    'autor_libro',
    db.Column('autor', db.Integer, db.ForeignKey("autores.id"), primary_key = True),
    db.Column('libro', db.Integer, db.ForeignKey("libros.id"), primary_key = True)
    )

class Libros(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    genero = db.Column(db.String(100), nullable = False)
    
    autores = db.relationship('Autores', secondary=autor_libro , backref=db.backref('libros', lazy='dynamic'))
    prestamo = db.relationship("Prestamos", back_populates = "libro", cascade = "all, delete-orphan")

    def __repr__(self):
        return ('<Libro: %r >' % (self.nombre) )

    def from_json(libro_json):
        id = libro_json.get('id')
        nombre = libro_json.get('nombre')
        genero = libro_json.get('genero')
        return Libros(id = id,
                    nombre = nombre,
                    genero = genero,
                    )


    def to_json(self):
        libro_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'genero': str(self.genero),
            'autores' : [autor.to_json() for autor in self.autores]
            
  }
        return libro_json
