import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .routes import main

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Crear la instancia de la base de datos
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurar la base de datos con las variables de entorno
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+mysqlconnector://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Inicializar la base de datos
    db.init_app(app)

    app.register_blueprint(main)

    return app
