from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    username = 'ux0syfoiocjl9tmp'
    password = 'Kfl1HM7o3G6xwfC5jdpX'
    hostname = 'bm2rhm44eaghsqxpk3yr-mysql.services.clever-cloud.com'
    database = 'bm2rhm44eaghsqxpk3yr'
    app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600 
    app.config['SQLALCHEMY_POOL_SIZE'] = 10    
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20  
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'main.login'

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        #db.create_all()
        pass

    return app