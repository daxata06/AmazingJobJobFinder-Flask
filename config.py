import os
from flask_sqlalchemy import SQLAlchemy


class Config:
    UPLOAD_FOLDER = 'app/static/avatars/'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI= 'postgresql://postgres:lolagreg100@localhost/users'

    

db = SQLAlchemy()

