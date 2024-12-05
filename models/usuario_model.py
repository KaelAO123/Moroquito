from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# `db.Model` es una clase base para todos los modelos de SQLAlchemy
# Define la clase `User` que hereda de `db.Model`
# `User` representa la tabla `users` en la base de datos
class Usuarios(UserMixin, db.Model):
    __tablename__ = "usuarios"
    # Define las columnas de la tabla `users`
    email = db.Column(db.String(200), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    direction = db.Column(db.String(200), nullable=False)
    celphone = db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="user")

    # Inicializa la clase `User`
    def __init__(self,email,first_name,last_name,password_hash,direction,celphone,role="user"):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.set_password(password_hash)
        self.role = role
        self.direction = direction
        self.celphone = celphone
        
    # Genera un hash seguro de la contraseña
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los usuarios de la base de datos
    @staticmethod
    def get_all():
        return Usuarios.query.all()

    # Obtiene un usuario por su id
    @staticmethod
    def get_by_id(id):
        return Usuarios.query.get(id)

    # Actualiza un usuario en la base de datos
    def update(self):
        db.session.commit()

    # Elimina un usuario de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def get_id(self):
        return self.email
    # Obtiene un usuario por su nombre de usuario
    @staticmethod
    def get_user_by_email(email):
        return Usuarios.query.filter_by(email=email).first()

    def has_role(self, role):
        return self.role == role