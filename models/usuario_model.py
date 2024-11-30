from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    __tablename__ = "usuario"
    correo_electronico = db.Column(db.String(50),primary_key=True, nullable = False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(50), nullable = False)
    apellido_materno = db.Column(db.String(50), nullable = False)
    contrasenia = db.Column(db.String(300), nullable = False)
    rol = db.Column(db.String(50), nullable = False, default = "user")
    
    def __init__(self,nombre, apellido_paterno, apellido_materno, contrasenia,rol="user"):
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
        return Usuario.query.all()
    
    @staticmethod
    def obtener_por_correo(correo):
        return Usuario.query.get(correo)
    
    def actualizar(self):
        db.session.commit()
        
    def borrar(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def has_role(self,role):
        return self.role == role