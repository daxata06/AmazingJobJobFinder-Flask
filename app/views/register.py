from flask import Flask, render_template, request, redirect, flash, get_flashed_messages,  url_for 
from app.models.user import *
from config import *
from . import views
from app.views.user_views import *
from flask_login import login_user, current_user, logout_user


@views.route('/register', methods=['POST', 'GET'])
def reg():
   
    if request.method == 'POST':
      fname = request.form['fname'] 
      lname = request.form['lname']
      profession = request.form['prof']
      email = request.form['email']
      password = request.form['pas']
      repassword = request.form['repas']

      if password == repassword:
         hash = generate_password_hash(password)
         id_=create_new_id()

         try:
          items = users(id_=id_,
                      first_name=fname,
                      last_name=lname,
                      email = email,
                      password=hash,
                      profession=profession)
          
          db.session.add(items)

          db.session.commit()
          
          User = users.query.filter_by(id_=id_).first()

          login_user(User)

          return redirect('/')
      
         except Exception as e:
            print(e)
            
            flash('Что-то пошло не так')

      else:
         
         flash('Пароли не совпадают!')
         
              
    return render_template("register.html") 


@views.route('/login', methods=['POST', 'GET'])
def aut():
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['pas']

      if email and password:
         User = users.query.filter_by(email=email).first()

         if check_password_hash(User.password, password):

          login_user(User)

          return redirect("/")

   return render_template("auth.html")

@views.route('/logout', methods=['POST', 'GET'])
def logout():
   
   if current_user.is_authenticated:
     logout_user()

     return redirect('/')



