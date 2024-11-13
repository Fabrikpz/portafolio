from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from app import db
from .forms import LoginForm, RegisterForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))  # Redirige al inicio si el usuario ya está autenticado
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Buscar por email
        
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))  # Redirige al inicio después de un login exitoso
        else:
            flash('Invalid email or password.', 'danger')
    
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))  # Redirige al inicio si el usuario ya está autenticado
    
    form = RegisterForm()
    if form.validate_on_submit():
        # Crear un nuevo usuario y almacenar la contraseña de forma segura
        new_user = User(email=form.email.data, full_name="")  # Asume que puedes agregar un nombre completo si lo deseas
        new_user.set_password(form.password.data)
        
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('main.login'))  # Redirige a la página de login después de crear la cuenta
    
    return render_template('register.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))  # Redirige al inicio después de cerrar sesión
