from .. import db

class Prestamo(db.Model):
    #Primaria
    id = db.Column(db.Integer, primary_key = True)
    #Atributos
    fecha_inicio = db.Column(db.String(100), nullable = False)
    fecha_vencimiento = db.Column(db.String(100), nullable = False)
    estado = db.Column(db.String(100), nullable = False)
  
    #Foranea PRESTAMO - OPINION (1:1)
    id_opinion = db.Column(db.Integer, db.ForeignKey("usuario.id"), primary_key = True)
    prestamo = db.relationship("Opinion", uselist = False, back_populates = "opinion", cascade="all, delete-orphan", single_parent=True) 
  
    #Foranea PRESTAMO - LIBRO (N:1)
    id_libro = db.Column(db.Integer, db.ForeignKey("libro.id"), primary_key = True)
    prestamo = db.relationship("Libro", uselist = False, back_populates = "libro", cascade="all, delete-orphan", single_parent=True)
  
    #Foranea PRESTAMO - USUARIO (N:1)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), primary_key = True)
    prestamo_usu = db.relationship("Usuario", uselist = False, back_populates = "usuario", cascade="all, delete-orphan", single_parent=True)    
    

    def __repr__(self):
        return ('<Prestamo: %r >' % (self.prestamo) )

    def to_json(self):
        prestamo_json = {
            'id': self.id,
            'prestamo': str(self.prestamo)
            }
        return prestamo_json
    
    @staticmethod
    def from_json(prestamo_json):
        id = prestamo_json.get('id')
        prestamo = prestamo_json.get('prestamo')
        return Prestamo(id = id,
                        prestamo = prestamo,
                        )