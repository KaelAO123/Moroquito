from flask import Flask
from flask_login import LoginManager

# Importamos el controlador de usuarios
from controllers import usuario_controller

# Importamos el controlador de animales
from controllers import producto_controller

# Importamos el controlador de panaderos
from controllers import panadero_controller

# Importamos la base de datos
from database import db
from models.usuario_model import Usuarios

# Inicializa la aplicación Flask
app = Flask(__name__)
# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Moroquito.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "clave-secreta"
# Configuración de Flask-Login
login_manager = LoginManager()
# Especifica la ruta de inicio de sesión
login_manager.login_view = "user.login"
login_manager.init_app(app)




# Función para cargar un usuario basado en su ID
@login_manager.user_loader
def load_user(user_email):
    return Usuarios.query.get((user_email))

    
# Inicializa `db` con la aplicación Flask
db.init_app(app)
# Registra el Blueprint de usuarios
app.register_blueprint(usuario_controller.user_bp)


if __name__ == "__main__":
    # Crea las tablas si no existen
    with app.app_context():
        db.create_all()
    app.run(debug=True)
