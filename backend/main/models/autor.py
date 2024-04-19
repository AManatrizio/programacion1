from .. import db

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return ('<Autor: %r >' % (self.autor) )

    def to_json(self):
        autor_json = {
            'id': self.id,
            'autor': str(self.autor),
        }
        return autor_json
    
    @staticmethod
    def from_json(autor_json):
        id = autor_json.get('id')
        autor = autor_json.get('autor')
        return Autor(id = id,
                    autor = autor,)

autor_libro = db.Table(
    'autor_libro',
    db.Column('autor', db.Integer, db.ForeignKey("autor.id"), nullable = False),
    db.Column('libro', db.Integer, db.ForeignKey("libro.id"), nullable = False)

)