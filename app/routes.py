from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from .models import User  # Modelo User, representa Herencia de db.Model (Pilar: Herencia)
from app import db
from .forms import LoginForm, RegistrationForm, EditProfileForm

# Pilar: Abstracción
# Uso de un blueprint para agrupar las rutas relacionadas con la funcionalidad principal de la aplicación.
main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Pilar: Abstracción
    # Se abstrae la validación del formulario y las operaciones sobre el usuario.
    form = EditProfileForm() if current_user.is_authenticated else None

    if form and form.validate_on_submit():
        # Encapsulamiento: La modificación de los atributos del usuario está protegida mediante métodos específicos.
        current_user.name = form.name.data
        current_user.role = form.role.data
        current_user.description = form.description.data
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('main.index'))
    
    elif form and request.method == 'GET':
        # Pilar: Encapsulamiento
        # Acceso controlado a los datos del usuario para prellenar el formulario.
        form.name.data = current_user.name
        form.role.data = current_user.role
        form.description.data = current_user.description

    return render_template('index.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Abstracción y Encapsulamiento
        # Se accede a los datos del usuario a través del modelo User.
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):  # Encapsulamiento en `check_password`
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Pilar: Abstracción
        # La creación del usuario está abstraída en el modelo User.
        user = User(email=form.email.data)
        user.set_password(form.password.data)  # Encapsulamiento: Método para establecer contraseña
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/logout')
@login_required
def logout():
    # Abstracción: `logout_user` maneja la lógica interna de cerrar sesión.
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()

    if form.validate_on_submit():
        # Pilar: Encapsulamiento
        # Modificación controlada de los atributos del usuario autenticado.
        current_user.name = form.name.data
        current_user.role = form.role.data
        current_user.description = form.description.data
        db.session.commit()
        return redirect(url_for('main.index'))

    # Abstracción: Acceso simplificado a los datos del usuario para prellenar el formulario.
    form.name.data = current_user.name
    form.role.data = current_user.role
    form.description.data = current_user.description

    return render_template('edit_profile.html', form=form)
