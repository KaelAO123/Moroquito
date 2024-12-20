from flask import Flask
from flask_login import LoginManager

from controllers import usuario_controller

from controllers import producto_controller

from controllers import pedido_controller

from database import db
from models.usuario_model import Usuarios

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Moroquito.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "clave-secreta"
login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_email):
    return Usuarios.query.get((user_email))

db.init_app(app)
app.register_blueprint(usuario_controller.user_bp)
app.register_blueprint(producto_controller.product_bp)
app.register_blueprint(pedido_controller.pedido_bp)

if __name__ == "__main__":

    with app.app_context():
        db.create_all()
    app.run(debug=True)
