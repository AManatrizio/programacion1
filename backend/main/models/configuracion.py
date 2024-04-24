from .. import db

class Configuraciones(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    configuracion = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return ('<Configuracion: %r >' % (self.configuracion) )

    def to_json(self):
        configuracion_json = {
            'id': self.id,
            'configuracion': str(self.configuracion),
            }
        return configuracion_json
    
    def from_json(configuracion_json):
        id = configuracion_json.get('id')
        configuracion = configuracion_json.get('configuracion')
        return Configuraciones(id = id,
                             configuracion = configuracion,
                             )