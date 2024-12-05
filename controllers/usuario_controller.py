from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash


from utils.decorators import role_required


from views import usuario_view


from models.usuario_model import Usuarios



user_bp = Blueprint("user", __name__)




@user_bp.route("/")
def index():
    admin = Usuarios.query.filter_by(email="admin@localHost").first()
    if current_user.is_authenticated:
        return usuario_view.principal()
    if not admin:
        
            admin = Usuarios(email="admin@localHost",
            first_name="Kae",
            last_name="Reyes",
            password_hash="k",
            direction="Villa Fatima",
            celphone="73299947",
            role="admin")
            admin.save()
    return redirect(url_for("user.login"))

@user_bp.route("/users")
@login_required
@role_required("admin")
def list_users():
    
    users = Usuarios.get_all()
    
    return usuario_view.usuarios(users)




@user_bp.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        password = request.form["password"]
        email = request.form["email"]
        direction = request.form["direction"]
        celphone = request.form["cellphone"]
        existing_user = Usuarios.query.filter_by(email=email).first()
        if existing_user:
            flash("El nombre de usuario ya está en uso", "error")
            return redirect(url_for("user.create_user"))
        
        user = Usuarios(first_name=first_name, last_name=last_name,email=email,password_hash=password,direction=direction,celphone=celphone)
        user.set_password(password)
        
        user.save()
        flash("Usuario registrado exitosamente", "success")
        return redirect(url_for("user.login"))
    
    return usuario_view.registro()






@user_bp.route("/users/<string:id>/update", methods=["GET", "POST"])
@login_required
def update_user(id):
    user:Usuarios = Usuarios.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    if request.method == "POST":
        
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        direction = request.form["direction"]
        celphone = request.form["cellphone"]
        role = request.form["role"]
        
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.direction = direction
        user.celphone = celphone
        user.role = role
        
        user.update()
        return redirect(url_for("user.list_users"))
    return usuario_view.actualizar(user)


@user_bp.route("/users/<string:id>/delete")
@login_required
@role_required("admin")
def delete_user(id):
    user = Usuarios.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    user.delete()
    return redirect(url_for("user.list_users"))



@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user:Usuarios = Usuarios.get_user_by_email(email)
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("user.index"))
        else:
            flash("Nombre de usuario o contraseña incorrectos", "error")
    return usuario_view.login()



@user_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for("user.login"))


@user_bp.route("/profile/<string:id>")
@login_required
def profile(id):
    user:Usuarios = Usuarios.get_user_by_email(id)
    return usuario_view.perfil(user)

@user_bp.route('/contact/')
@login_required
def contact():
    return usuario_view.contact()