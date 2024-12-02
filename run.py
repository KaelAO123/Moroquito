# from flask import Flask, render_template
from flask_login import LoginManager

# Controladores
from controllers import panadero_controller,producto_controller, usuario_controller

# Base de datos
from database import db
from models.usuario_model import Usuario

# Inicializa la aplicacion Flask

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///panaderia.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SECRET_KEY"] = "clave-secreta"
#
# # Configuracion del Flask-login
# login_manager = LoginManager()
# login_manager.login_view = "usuario.login"
#
#



# Especifica la ruta de inicio de sesion
# @login_manager.user_loader
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# @app.route('/about')
# def about():
#     return render_template('about.html')
#
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
from website import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
