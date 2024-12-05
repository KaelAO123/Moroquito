from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Pedidos(UserMixin, db.Model):
    __tablename__ = "pedidos"
    idPedido = db.Column(db.Integer,primary_key=True,autoincrement=True)
    fecha_pedido = db.Column(db.DateTime, nullable=False)
    fecha_entrega = db.Column(db.DateTime, nullable=False)
    direction = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
    cantidadPedida = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    
    idProduct = db.Column(db.Integer,db.ForeignKey("productos.idProducto"),nullable=False)
    email = db.Column(db.String,db.ForeignKey("usuarios.email"),nullable=False)

    def __init__(self, fecha_entrega, fecha_pedido, email, idProduct,direction,message,cantidadPedida,estado="Pendiente"):
        self.fecha_entrega = fecha_entrega
        self.fecha_pedido = fecha_pedido
        self.email = email
        self.idProduct = idProduct
        self.direction = direction
        self.message = message
        self.cantidadPedida = cantidadPedida
        self.estado = estado
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los Pedidos de la base de datos
    @staticmethod
    def get_all():
        return Pedidos.query.all()

    # Obtiene un usuario por su id
    @staticmethod
    def get_by_id(id):
        return Pedidos.query.get(id)

    # Actualiza un usuario en la base de datos
    def update(self):
        db.session.commit()

    # Elimina un usuario de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def join(tabla,email):
        return (db.session.query(Pedidos, tabla)
        .join(tabla, Pedidos.idProduct == tabla.idProducto)
        .filter(Pedidos.email == email)
        .all())