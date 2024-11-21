from .. import db
from flask import request, jsonify, Blueprint


class Prestamos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(10), nullable=False, default="En uso")
    fecha_inicio = db.Column(db.String(100), nullable=False)
    fecha_vencimiento = db.Column(db.String(100), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey(
        "usuarios.id"), nullable=False)
    libro_id = db.Column(db.Integer, db.ForeignKey(
        "libros.id"), nullable=False)

    usuario = db.relationship(
        "Usuarios", back_populates="prestamo", uselist=False, single_parent=True)
    libro = db.relationship(
        "Libros", back_populates="prestamo", uselist=False, single_parent=True)
    opinion = db.relationship("Opiniones", uselist=False, back_populates="prestamos",
                              cascade="all, delete-orphan", single_parent=True)

    def __repr__(self):
        return ('<Prestamo: %r >' % (self.prestamo))

    def to_json(self):
        prestamo_json = {
            'id': int(self.id),
            'estado': str(self.estado),
            'fecha_inicio': str(self.fecha_inicio),
            'fecha_vencimiento': str(self.fecha_vencimiento),
            'usuario_id': int(self.usuario_id),
            'libro_id': int(self.libro_id),
        }
        return prestamo_json

    def to_json_short(self):
        prestamo_json = {
            'usuario_id': self.usuario_id,
            'libro_id': self.libro_id,
        }
        return prestamo_json

    @staticmethod
    def from_json(prestamo_json):
        fecha_inicio = prestamo_json.get('fecha_inicio')
        fecha_vencimiento = prestamo_json.get('fecha_vencimiento')
        usuario_id = prestamo_json.get('usuario_id')
        libro_id = prestamo_json.get('libro_id')
        return Prestamos(
            fecha_inicio=fecha_inicio,
            fecha_vencimiento=fecha_vencimiento,
            usuario_id=usuario_id,
            libro_id=libro_id,
        )
