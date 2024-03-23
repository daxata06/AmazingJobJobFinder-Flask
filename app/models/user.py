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

def get_avatar(id_):
   photo = db.engine.execute(f'select photo_path from avatars where user_id={id_}').scalar()

   if photo:
   
    return f'static/avatars/{photo}'
   
   else:
     
     return 'static/avatars/4-26.jpg'
   
class users_employers(db.Model, UserMixin):
    id_ = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    company_name = db.Column(db.String(64))
    professions = db.Column(db.String(256))

    def get_id(self):
     return f'{self.id_}'
 

    def check_password(self, password):
      return check_password_hash(self.password, password)
 

    @property
    def authenticated(self):
        return True

    @property
    def active(self):
      return True

    @property
    def anonymous(self):
      return False

class Applications(db.Model):
   id_req = db.Column(db.Integer, primary_key=True)
   id_from = db.Column(db.Integer)
   id_to = db.Column(db.Integer)
   status = db.Column(db.String(64))

def create_new_id_application():
   all_ = db.engine.execute('select count(id_req) from Applications').scalar()

   return all_+1

def check_application(id_):
   data= db.engine.execute(f'select status from Applications where id_to={id_}').scalar()

   if data:

      return data
   
   else:

      return False
   
def get_company_name(id_):
   return db.engine.execute(f'select company_name from users_employers where id_={id_}').scalar()

def update_app_st(id_from, id_to, status):
   db.engine.execute(f"update applications set status='{status}' where id_from={id_from} and id_to={id_to}")
   db.session.commit()

def get_name(id_to):
   return db.engine.execute(f'select first_name from users where id_={id_to}').scalar()
