from flask import Flask, render_template, request, redirect, flash, get_flashed_messages
from app.models.user import *
from config import *
from . import views
import os
from flask_login import current_user


@views.route('/profile/<int:id_>', methods=['POST', 'GET'])
def profile_view(id_):
    name_username = users.query.filter_by(id_=id_).first()

    profile_info = profile.query.filter_by(id_user=id_).first()

    user_photo = avatars.query.filter_by(user_id=id_).first()

    if request.method == 'POST':

        if 'photo' in request.files and request.files['photo'].filename:
           
           print(request.files['photo'])
           if user_photo:
             db.session.delete(user_photo)
             os.remove(Config.UPLOAD_FOLDER+user_photo.photo_path)

           photo = request.files['photo']
  

           photo.save(os.path.join(Config.UPLOAD_FOLDER,
                                photo.filename))
          
           datas = avatars(user_id=id_,
                          photo_path=photo.filename)
            
          
           db.session.add(datas)
           db.session.commit()

           return redirect(f'/profile/{id_}')

        elif 'exp1' in request.form:

          id_ = id_
          description = request.form['descr']
          exp1 = request.form['exp1']
          exp2 = request.form['exp2']
          gr = request.form['gr']
          workac = request.form['workac']
          otherd = request.form['otherd']
          phone = request.form['phone']
          socn = request.form['socn']

          try:

           datas = profile(id_user=id_,
           profile_descr=description,
           work_exp_y=exp1,
           work_exp_p = exp2,
           citizen=gr,
           work_accept=workac,
           other_docs=otherd,
           phone=phone,
           nets=socn
           )

           if profile_info:
            db.session.delete(profile_info)
       
           db.session.add(datas)
           db.session.commit()

           return redirect(f'/profile/{id_}')
          
          except:
           flash('Что-то пошло не так!')
        else:

          flash("Фото не было загружено!")
        
    currentuser = int(current_user.get_id())

    if currentuser is None:
        currentuser=0
     
    return render_template("profile.html", 
                           name_username=name_username, 
                           profile_info=profile_info,
                           user_photo=user_photo,
                           id_=int(id_),
                           currentuser=currentuser)


@views.route('/delete_photo/<int:id_>', methods=['POST', 'GET'])
def delete_photo(id_):
  user_photo = avatars.query.filter_by(user_id=id_).first()
  
  if user_photo:
   db.session.delete(user_photo)
   db.session.commit()
   os.remove(Config.UPLOAD_FOLDER+user_photo.photo_path)
  
  return redirect(f'/profile/{id_}')
