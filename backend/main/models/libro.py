from .. import db

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    autor = db.Column(db.String(100), nullable = False)
    genero = db.Column(db.String(100), nullable = False)
    estado = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return ('<Libro: %r >' % (self.nombre) )

    def to_json(self):
        libro_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'autor': str(self.autor),
            'genero': str(self.genero),
            'estado': str(self.estado),
        }
        return libro_json
    
    @staticmethod
    def from_json(libro_json):
        id = libro_json.get('id')
        nombre = libro_json.get('nombre')
        autor = libro_json.get('autor')
        genero = libro_json.get('genero')
        estado = libro_json.get('estado')
        return Libro(id = id,
                    nombre = nombre,
                    autor = autor,
                    genero = genero,
                    estado = estado,)
