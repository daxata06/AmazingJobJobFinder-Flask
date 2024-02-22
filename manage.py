from app import create_app
from app.models.user import *
from app.views.user_views import *
from app.views.register import *

app = create_app()



if __name__== '__main__':
    app.run() 