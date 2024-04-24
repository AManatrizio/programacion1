from .. import db

class Libro(db.Model):
    #Primaria
    id = db.Column(db.Integer, primary_key = True)
    #Atributos
    nombre = db.Column(db.String(100), nullable = False)
    editorial = db.Column(db.String(100), nullable = False)
    genero = db.Column(db.String(100), nullable = False)
    #Foranea PRESTAMO - LIBRO (N:1)
    libro = db.relationship("Prestamo", uselist = False, back_populates = "prestamo", cascade="all, delete-orphan", single_parent=True)

    prestamo = db.relationship("Prestamo", back_populates = "libro", cascade = "all, delete-orphan")




    def __repr__(self): #Que hacen estas funciones?
        return ('<Libro: %r >' % (self.nombre) )

    def to_json(self):  #
        libro_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'autor': str(self.autor),
            'genero': str(self.genero),
            'estado': str(self.estado),
        }
        return libro_json
    
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

      
###comentarios = db.relationship("Comentario", back_populates = "libro", cascade = "all, delete-orphan")
###valoraciones = db.relationship("ValUsLib", back_populates = "libro", cascade = "all, delete-orphan")
