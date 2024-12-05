from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin





class Usuarios(UserMixin, db.Model):
    __tablename__ = "usuarios"
    
    email = db.Column(db.String(200), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    direction = db.Column(db.String(200), nullable=False)
    celphone = db.Column(db.String(15), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="user")

    
    def __init__(self,email,first_name,last_name,password_hash,direction,celphone,role="user"):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.set_password(password_hash)
        self.role = role
        self.direction = direction
        self.celphone = celphone
        
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    
    def save(self):
        db.session.add(self)
        db.session.commit()

    
    @staticmethod
    def get_all():
        return Usuarios.query.all()

    
    @staticmethod
    def get_by_id(id):
        return Usuarios.query.get(id)

    
    def update(self):
        db.session.commit()

    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def get_id(self):
        return self.email
    
    @staticmethod
    def get_user_by_email(email):
        return Usuarios.query.filter_by(email=email).first()

    def has_role(self, role):
        return self.role == role