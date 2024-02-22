from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from config import db
from flask_login import LoginManager
from app.views import views
from app.models.user import users, profile
from flask_migrate import Migrate




def create_app():
    App = Flask(__name__)
    login_manager = LoginManager()
    login_manager.init_app(App)

    @login_manager.user_loader
    def load_user(user_id):
     return db.session.query(users).get(user_id)
    
    App.config.from_object(Config)

    db.init_app(App)
    
    with App.app_context():
     db.create_all()
     print(1)

    migrate = Migrate(App, db)
    #manager = Manager(App)

    #manager.add_command('db')

    App.register_blueprint(views)
    return App


