from flask import Blueprint


views = Blueprint('views', __name__)


from . import register, user_views, profile_views
