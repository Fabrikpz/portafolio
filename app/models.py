from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Crear la instancia de la base de datos
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    # Método para establecer la contraseña (encriptada)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Método para verificar si la contraseña ingresada es correcta
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
