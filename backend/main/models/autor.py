from .. import db

class Autores(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return ('<Autor: %r >' % (self.autor) )

    def to_json(self):
        autor_json = {
            'id': self.id,
            'autor': str(self.nombre),
        }
        return autor_json
    
    def from_json(autor_json):
        id = autor_json.get('id')
        nombre = autor_json.get('nombre') 
        return Autores(id=id, nombre=nombre)


autor_libro = db.Table(
    'autor_libro',
    db.Column('autor', db.Integer, db.ForeignKey("autores.id"), nullable = False),
    db.Column('libro', db.Integer, db.ForeignKey("libros.id"), nullable = False)
    )