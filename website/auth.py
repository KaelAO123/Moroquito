from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy.testing.pickleable import User
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user,current_user

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Inicio de Session Exitosa!!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

            else:
                flash("Correo Electronico o contraseña incorrecta, intenta de nuevo", category='error')

        else:
            flash("El correo Electronico no esta registrado", category='error')

    return render_template("login.html", boolean=True)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        email=request.form['email']
        first_name = request.form['first_name']
        password1 = request.form['password1']
        password2 = request.form['password2']
        user = User.query.filter_by(email=email).first()
        if user:
            flash('El correo electronico ya existe!!', category='error')
        elif len(email)<4:
            flash("El correo electronico debe tener mas de 4 caracteres", category='error')
        elif len(first_name)<2:
            flash('El nombre debe tener mas de 2 caracteres ', category='error')
        elif password1 != password2:
            flash('Las contraseñas no coinciden', category='error')
        elif len(password1)<7:
            flash('La contraseña deberia de tener al menos 7 caracteres', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)  # Solución

            flash('Cuenta creada!',category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")