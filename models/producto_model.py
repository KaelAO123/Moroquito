from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Productos(UserMixin, db.Model):
    __tablename__ = "productos"
    idProducto = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    image = db.Column(db.String, nullable=False)   
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(255), nullable=False)
    cant_disp = db.Column(db.Integer, nullable=False)
    
    def __init__(self,name,description,price,category,cant_disp,image):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.cant_disp = cant_disp
        self.image = image
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Productos.query.all()
    
    @staticmethod
    def get_by_id(idProducto):
        return Productos.query.get(idProducto)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()