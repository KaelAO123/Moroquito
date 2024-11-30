from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Panadero(UserMixin, db.Model):
    __tablename__ = "panaderos"
    ci = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(50), nullable = False)
    apellido_materno = db.Column(db.String(50), nullable = False)
    contrasenia = db.Column(db.String(300), nullable = False)
    rol = db.Column(db.String(50), nullable = False, default = "panadero")
    
    def __init__(self,nombre, apellido_paterno, apellido_materno, contrasenia,rol="panadero"):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.contrasenia = generate_password_hash(contrasenia)
        self.rol = rol
    
    def guardar(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def obtener_todo():
        return Panadero.query.all()
    
    @staticmethod
    def obtener_por_ci(ci):
        return Panadero.query.get(ci)
    
    def actualizar(self):
        db.session.commit()
        
    def borrar(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def has_role(self,role):
        return self.role == role