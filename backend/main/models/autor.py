from .. import db

autor_libro = db.Table(
    'autor_libro',
    db.Column('autor', db.Integer, db.ForeignKey("autores.id"), primary_key = True),
    db.Column('libro', db.Integer, db.ForeignKey("libros.id"), primary_key = True)
    )

class Autores(db.Model): #e
    id = db.Column(db.Integer, primary_key = True)
    autor = db.Column(db.String(100), nullable = False)
    
    libros = db.relationship('Libros', secondary=autor_libro , backref=db.backref('autor', lazy='dynamic'))

    def __repr__(self):
        return ('<Autor: %r >' % (self.autor) )

    def to_json(self):
        autor_json = {
            'id': self.id,
            'autor': str(self.autor),
            'libros' : [libro.to_json() for libro in self.libros]

        }
        return autor_json
    
    def from_json(autor_json):
        id = autor_json.get('id')
        autor = autor_json.get('autor')
        return Autores(id = id,
                    autor = autor,)

