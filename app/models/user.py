from config import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask_login import UserMixin


class users(db.Model, UserMixin):
 id_ = db.Column(db.Integer, primary_key=True)
 first_name = db.Column(db.String(64))
 last_name = db.Column(db.String(64))
 email = db.Column(db.String(128))
 password = db.Column(db.String(128))
 profession = db.Column(db.String(64))


 def get_id(self):
  return f'{self.id_}'
 

 def check_password(self, password):
   return check_password_hash(self.password, password)
 

 @property
 def is_authenticated(self):
        return True

 @property
 def is_active(self):
     return True

 @property
 def is_anonymous(self):
    return False
 

class profile(db.Model):
   id_user = db.Column(db.Integer, primary_key=True)
   profile_descr = db.Column(db.String(1024))
   work_exp_y = db.Column(db.Float)
   work_exp_p = db.Column(db.String(1024))
   citizen = db.Column(db.String(64))
   other_docs = db.Column(db.String(256))
   work_accept = db.Column(db.String(256))
   phone = db.Column(db.String())
   nets = db.Column(db.String(256))
   
 
class avatars(db.Model):
   user_id = db.Column(db.Integer, primary_key=True)
   photo_path = db.Column(db.String())

   
def create_new_id():
   all_ = db.engine.execute('select count(id_) from users').scalar()

   return all_+1
