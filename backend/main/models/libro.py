from .. import db

class Libros(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100), nullable = False)
    genero = db.Column(db.String(100), nullable = False)
    estado = db.Column(db.String(100), nullable = False)

    prestamo = db.relationship("Prestamos", back_populates = "libro", cascade = "all, delete-orphan")
    


    def __repr__(self):
        return ('<Libro: %r >' % (self.nombre) )

    def to_json(self):
        libro_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'genero': str(self.genero),
            'estado': str(self.estado),
        }
        return libro_json
    
    def from_json(libro_json):
        id = libro_json.get('id')
        nombre = libro_json.get('nombre')
        genero = libro_json.get('genero')
        estado = libro_json.get('estado')
        return Libros(id = id,
                    nombre = nombre,
                    genero = genero,
                    estado = estado,)
